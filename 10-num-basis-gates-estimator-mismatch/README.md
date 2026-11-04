# num_basis_gates returns 0 for a three-CX decomposition

### Environment

- **Qiskit version**: 2.7.0.dev0, main cf46ab8dca
- **Python version**: 3.13.12
- **Operating system**: Linux x86_64

### What is happening?

For the unitary below, TwoQubitBasisDecomposer.num_basis_gates returns 0, while the same
decomposer returns a circuit with 3 CX gates. basis_fidelity is 1.0.

### How can we reproduce the issue?

```python
from qiskit import QuantumCircuit
from qiskit.circuit.library import CXGate
from qiskit.quantum_info import Operator
from qiskit.synthesis import TwoQubitBasisDecomposer
qc = QuantumCircuit(2); qc.h(0); qc.swap(0, 1)
unitary = Operator(qc).data
decomposer = TwoQubitBasisDecomposer(CXGate(), basis_fidelity=1.0)
print(decomposer.num_basis_gates(unitary), decomposer(unitary).count_ops().get("cx", 0))
# 0 3
```

### What should happen?

For this unitary, num_basis_gates should return 3, matching the returned decomposition.

Related:
- https://github.com/Qiskit/qiskit/pull/11019
- https://github.com/Qiskit/qiskit/pull/12010

### AI/LLM disclosure

- I found this as part of IBM Research's Spotlights project on AI-native software optimization.
