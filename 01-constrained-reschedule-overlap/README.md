# Two sequential SX gates overlap after ConstrainedReschedule

### Environment

- **Qiskit version**: 2.7.0.dev0, main cf46ab8dca
- **Python version**: 3.13.12
- **Operating system**: Linux x86_64

### What is happening?

Two sequential SX gates each last 36 dt. After ALAPScheduleAnalysis and ConstrainedReschedule
with 16-dt alignment, their start times are 112 and 144 dt. The first ends at 148 dt,
overlapping the second by 4 dt. The target has granularity=1 and pulse_alignment=16; 36 dt
satisfies the duration granularity, while both reported starts satisfy the pulse-start
alignment.

36 dt is not a multiple of pulse_alignment=16; the 4-dt overlap equals 36 mod 16. Only this
duration was tested. #16186 also reports overlapping start times; #16482 was not tested here.

### How can we reproduce the issue?

```python
from qiskit import QuantumCircuit
from qiskit.transpiler import Target, InstructionProperties, PassManager
from qiskit.transpiler.passes import ALAPScheduleAnalysis, ConstrainedReschedule
qc = QuantumCircuit(1); qc.delay(100, 0); qc.sx(0); qc.sx(0)
target = Target(num_qubits=1, dt=1e-9, granularity=1,
                pulse_alignment=16, acquire_alignment=16)
target.add_instruction(qc.data[1].operation, {(0,): InstructionProperties(duration=36e-9)})
pm = PassManager([ALAPScheduleAnalysis(target=target),
                  ConstrainedReschedule(target=target)])
pm.run(qc)
print(sorted(t for n, t in pm.property_set["node_start_time"].items() if n.op.name == "sx"))
# [112, 144]
```

### What should happen?

The second SX should start at least 36 dt after the first, without overlap.

Related:
- https://github.com/Qiskit/qiskit/issues/16186
- https://github.com/Qiskit/qiskit/pull/16482
- https://github.com/Qiskit/qiskit/pull/10076

### AI/LLM disclosure

- I found this as part of IBM Research's Spotlights project on AI-native software optimization.
