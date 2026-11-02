# Seeded compilation varies idle-wire initial layouts

### Environment

- Qiskit: 2.6.1 and 2.7.0.dev0 (main `0f2d7ddfd262b1fa3afbc27f733e5c9f6cc6426d`)
- Python: 3.13.12
- OS: Linux x86_64

### What is happening?

Repeated compilation with the same seed can give different initial-layout mappings for the idle wires. The active-wire mappings remain unchanged.

### How can we reproduce the issue?

```python
from qiskit import QuantumCircuit
from qiskit.transpiler import CouplingMap, generate_preset_pass_manager

qc = QuantumCircuit(6)
for a, b in ((0, 1), (1, 2), (0, 2)):
    qc.cx(a, b)
pm = generate_preset_pass_manager(optimization_level=2, basis_gates=['rz', 'sx', 'x', 'cz'],
                                  coupling_map=CouplingMap.from_line(6), seed_transpiler=1)
layouts = {tuple(pm.run(qc).layout.initial_index_layout()) for _ in range(20)}

print(sorted(layouts))
# [(1, 2, 0, 3, 4, 5), (1, 2, 0, 4, 3, 5)]
```

### What should happen?

With fixed inputs, environment and seed, the seeded pipeline should return consistent initial-layout metadata, including idle-wire mappings.
