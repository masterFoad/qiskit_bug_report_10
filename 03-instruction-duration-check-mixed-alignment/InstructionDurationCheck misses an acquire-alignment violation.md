### Environment

- Qiskit: 2.6.1 and 2.7.0.dev0 (main `0f2d7ddfd262b1fa3afbc27f733e5c9f6cc6426d`)
- Python: 3.13.12
- OS: Linux 5.14.0-687.58.1.el9_8.x86_64 (x86_64)

### What is happening?

InstructionDurationCheck reports `reschedule_required=False` for a 100 dt delay followed by measurement. It is configured with acquire alignment 16 and pulse alignment 1.

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

InstructionDurationCheck should set `reschedule_required` to True for this acquire-alignment violation.
