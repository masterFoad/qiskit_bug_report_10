# ConstrainedReschedule overlaps sequential SX gates

### Environment

- Qiskit: 2.6.1 and 2.7.0.dev0 (main `0f2d7ddfd262b1fa3afbc27f733e5c9f6cc6426d`)
- Python: 3.13.12
- OS: Linux x86_64

### What is happening?

After alignment rescheduling, the two SX gates start at 112 and 144 dt. Each SX lasts 36 dt, so they overlap by 4 dt on the same qubit.

### How can we reproduce the issue?

```python
from qiskit import QuantumCircuit
from qiskit.circuit.library import SXGate
from qiskit.transpiler import Target, InstructionProperties, PassManager
from qiskit.transpiler.passes import ALAPScheduleAnalysis, ConstrainedReschedule

target = Target(num_qubits=1, dt=1e-9, pulse_alignment=16, acquire_alignment=16)
target.add_instruction(SXGate(), {(0,): InstructionProperties(duration=36e-9)})
qc = QuantumCircuit(1)
qc.delay(100, 0)
qc.sx(0)
qc.sx(0)
pm = PassManager([ALAPScheduleAnalysis(target=target), ConstrainedReschedule(target=target)])
pm.run(qc)

print(sorted(t for n, t in pm.property_set['node_start_time'].items() if n.op.name == 'sx'))
# [112, 144]
```

### What should happen?

ConstrainedReschedule should satisfy start-time alignment while preserving non-overlap between sequential operations on one qubit.
