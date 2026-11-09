# GenericBackendV2 with a fixed seed gives different properties after CouplingMap.make_symmetric

### Environment

- **Qiskit version**: 2.7.0.dev0, main 9ab2106352
- **rustworkx version**: 0.18.1
- **Python version**: 3.13.16
- **Operating system**: Linux x86_64

### What is happening?

Building the same backend from the same coupling map with the same seed gives different CZ error
rates and durations. This happens within one process. The reproducer only builds backends and reads
their properties.

### How can we reproduce the issue?

```python
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.transpiler import CouplingMap

for _ in range(20):
    coupling = CouplingMap([(0, 1), (1, 2)])
    coupling.make_symmetric()
    backend = GenericBackendV2(3, basis_gates=["u", "cz"], coupling_map=coupling, seed=11)
    prop = backend.target["cz"][(1, 0)]
    print(prop.duration, prop.error)
```

The loop builds the same backend 20 times. With `PYTHONHASHSEED=0`, it printed two different
lines, 12 times the first and 8 times the second:

```text
2.4753e-07 0.002773114510697487
5.301360000000001e-07 0.004904759060093554
```

The forward edges keep their properties. The random values move between the reverse edges.

### What should happen?

The same coupling map and the same seed should give the same backend properties.

### Any suggestions?

`CouplingMap.make_symmetric` calls rustworkx `PyDiGraph.make_symmetric`. That method adds the
missing reverse edges by iterating a hash map, so their order changes from call to call.
`GenericBackendV2` assigns its seeded random values in edge order.

Sorting the edges first, with `CouplingMap(sorted(coupling.get_edges()))`, gave the same properties
in all 128 trials. `GenericBackendV2` could sort the edges before it draws the properties.

This looks like a regression from https://github.com/Qiskit/qiskit/pull/16742. That PR replaced the
Python implementation of `CouplingMap.make_symmetric` with the rustworkx one. Both add the same
edges, in a different order. With Qiskit 2.5.2, from before that PR, and the same rustworkx 0.18.1,
the reproducer prints the same line all 20 times.

https://github.com/Qiskit/qiskit/issues/16490 reported a related non-determinism with symmetric
coupling maps. https://github.com/Qiskit/qiskit/pull/16732 fixed it in the VF2Layout error sums.

https://github.com/Qiskit/qiskit/issues/11768 is about the simulator seed used by `run`. This issue
is about the properties of the backend itself.

### AI/LLM disclosure

- I developed this as part of IBM Research's Spotlights project on AI-native software optimization.
