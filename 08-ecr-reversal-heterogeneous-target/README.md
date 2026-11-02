# ECR reversal fails with CZ on another target edge

### Environment

- Qiskit: 2.6.1 and 2.7.0.dev0 (main `0f2d7ddfd262b1fa3afbc27f733e5c9f6cc6426d`)
- Python: 3.13.12
- OS: Linux x86_64

### What is happening?

Compiling `ecr(2, 1)` fails with a target offering `ecr(1, 2)` and CZ on another edge. The error says that no reversal rules are known.

### How can we reproduce the issue?

```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.circuit.library import CZGate, ECRGate, RZGate, SXGate
from qiskit.transpiler import Target, generate_preset_pass_manager

target = Target(num_qubits=3)
for gate in (RZGate(Parameter('t')), SXGate()):
    target.add_instruction(gate, {(q,): None for q in range(3)})
target.add_instruction(CZGate(), {(0, 1): None, (1, 0): None})
target.add_instruction(ECRGate(), {(1, 2): None})
qc = QuantumCircuit(3)
qc.ecr(2, 1)
pm = generate_preset_pass_manager(optimization_level=0, target=target)
pm.run(qc)
# qiskit.transpiler.exceptions.TranspilerError: 'ecr would be supported on [Qubit(2), Qubit(1)] if the direction was swapped, but no rules are known to do that. ["cx", "cz", "ecr", "swap", "rzx", "rxx", "ryy", "rzz"] can be automatically flipped.'
```

### What should happen?

Compilation should express the reversed ECR using the supported ECR direction and target-supported single-qubit gates.
