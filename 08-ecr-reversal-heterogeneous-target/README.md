# Reversed ECR raises TranspilerError with a mixed ECR/CZ target

### Environment

- **Qiskit version**: 2.7.0.dev0, main cf46ab8dca
- **Python version**: 3.13.12
- **Operating system**: Linux x86_64

### What is happening?

The target has ECR on (1, 2), CZ on (0, 1) and (1, 0), and the one-qubit gates shown below on
all three qubits. Transpiling ECR(2, 1) at optimization_level=0 raises TranspilerError.

### How can we reproduce the issue?

```python
from qiskit import QuantumCircuit, transpile
from qiskit.circuit import Parameter
from qiskit.circuit.library import CZGate, ECRGate, RZGate, SXGate, XGate
from qiskit.transpiler import Target
target = Target(num_qubits=3)
for gate in (RZGate(Parameter("t")), SXGate(), XGate()):
    target.add_instruction(gate, {(q,): None for q in range(3)})
target.add_instruction(CZGate(), {(0, 1): None, (1, 0): None})
target.add_instruction(ECRGate(), {(1, 2): None})
qc = QuantumCircuit(3); qc.ecr(2, 1)
try: print(transpile(qc, target=target, optimization_level=0, initial_layout=[0, 1, 2]))
except Exception as exc: print(type(exc).__name__); print(*str(exc).split(", "), sep="\n")
# TranspilerError
# 'ecr would be supported on [Qubit(2)
# Qubit(1)] if the direction was swapped
# but no rules are known to do that. ["cx"
# "cz"
# "ecr"
# "swap"
# "rzx"
# "rxx"
# "ryy"
# "rzz"] can be automatically flipped.'
```

### What should happen?

The reversed ECR should be translated using ECR(1, 2) and the available one-qubit gates.

Related:
- https://github.com/Qiskit/qiskit/issues/10013
- https://github.com/Qiskit/qiskit/issues/10785

### AI/LLM disclosure

- I found this as part of IBM Research's Spotlights project on AI-native software optimization.
