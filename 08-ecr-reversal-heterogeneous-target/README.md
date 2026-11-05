# Transpiling a reversed ECR fails on FakeCairoV2

### Environment

- **Qiskit version**: 2.7.0.dev0 (main cf46ab8dca)
- **qiskit-ibm-runtime version**: 0.51.0
- **Python version**: 3.13.12
- **Operating system**: Linux

### What is happening?

Transpiling an `ecr` gate in the reverse direction fails on `FakeCairoV2`. This backend has `ecr` on qubits (1, 2) but not on (2, 1), and uses `cx` on some of the other couplers.

### How can we reproduce the issue?

Here is a short reproducer:

```python
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime.fake_provider import FakeCairoV2

qc = QuantumCircuit(3)
qc.ecr(2, 1)
transpile(qc, target=FakeCairoV2().target, optimization_level=0, initial_layout=[0, 1, 2])
```

which raises:

```
qiskit.transpiler.exceptions.TranspilerError: 'ecr would be supported on [Qubit(2), Qubit(1)] if the direction was swapped, but no rules are known to do that. ["cx", "cz", "ecr", "swap", "rzx", "rxx", "ryy", "rzz"] can be automatically flipped.'
```

### What should happen?

The reversed `ecr` should be translated using `ecr` on (1, 2) and single-qubit gates. For comparison, a small 3-qubit target with only `ecr` on (1, 2), `rz`, `sx` and `x` transpiles the same circuit correctly.

### Any suggestions?

Possibly related: #10013, #10785.

### AI/LLM disclosure

- I developed this as part of IBM Research's Spotlights project on AI-native software optimization.
