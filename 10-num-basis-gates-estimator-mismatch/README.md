# num_basis_gates reports zero for a three-CX decomposition

### Environment

- Qiskit: 2.6.1 and 2.7.0.dev0 (main `0f2d7ddfd262b1fa3afbc27f733e5c9f6cc6426d`)
- Python: 3.13.12
- OS: Linux x86_64

### What is happening?

For H followed by SWAP, `num_basis_gates` returns 0. The same decomposer with basis fidelity 1.0 emits three CX gates.

### How can we reproduce the issue?

```python
from qiskit import QuantumCircuit
from qiskit.circuit.library import CXGate
from qiskit.quantum_info import Operator
from qiskit.synthesis import TwoQubitBasisDecomposer

qc = QuantumCircuit(2)
qc.h(0)
qc.swap(0, 1)
unitary = Operator(qc).data
decomposer = TwoQubitBasisDecomposer(CXGate(), basis_fidelity=1.0)

print(decomposer.num_basis_gates(unitary), decomposer(unitary).count_ops().get('cx', 0))
# 0 3
```

### What should happen?

num_basis_gates should report 3 for this unitary with the same exact-synthesis settings.
