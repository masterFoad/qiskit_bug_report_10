# InstructionDurationCheck misses acquire alignment when pulse_alignment is 1

### Environment

- **Qiskit version**: 2.7.0.dev0, main cf46ab8dca
- **Python version**: 3.13.12
- **Operating system**: Linux x86_64

### What is happening?

A measurement follows a delay of 100 dt. InstructionDurationCheck returns
reschedule_required=False with acquire_alignment=16 and pulse_alignment=1.

### How can we reproduce the issue?

```python
from qiskit import QuantumCircuit
from qiskit.transpiler.passes import InstructionDurationCheck
qc = QuantumCircuit(1, 1)
qc.delay(100, 0)
qc.measure(0, 0)
p = InstructionDurationCheck(acquire_alignment=16, pulse_alignment=1)
p(qc)
print(p.property_set['reschedule_required'])
# False
```

### What should happen?

reschedule_required should be True: 100 dt is not aligned to the 16-dt acquire grid.

Related:
- https://github.com/Qiskit/qiskit/pull/16482
- https://github.com/Qiskit/qiskit/pull/14700

### AI/LLM disclosure

- I found this as part of IBM Research's Spotlights project on AI-native software optimization.
