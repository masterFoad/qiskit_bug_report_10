# PadDynamicalDecoupling with a one-gate sequence changes the global phase

### Environment

- **Qiskit version**: 2.7.0.dev0 (main cf46ab8dca)
- **Python version**: 3.13.12
- **Operating system**: Linux

### What is happening?

`PadDynamicalDecoupling` with a single-gate sequence `[XGate()]` changes the global phase of the circuit. The output is equivalent to the input only up to global phase.

### How can we reproduce the issue?

Here is a short reproducer:

```python
from qiskit import QuantumCircuit
from qiskit.circuit.library import XGate
from qiskit.quantum_info import Operator
from qiskit.transpiler import InstructionDurations, PassManager
from qiskit.transpiler.passes import ALAPScheduleAnalysis, PadDynamicalDecoupling

qc = QuantumCircuit(1)
qc.u(0.4, -0.6, 1.3, 0)
qc.delay(300, 0)

durations = InstructionDurations([("u", None, 50), ("x", None, 50)], dt=1e-9)
pm = PassManager([ALAPScheduleAnalysis(durations), PadDynamicalDecoupling(durations, [XGate()])])
out = pm.run(qc)
print(Operator(out).equiv(qc), Operator(out) == Operator(qc))
```

This prints `True False`.

### What should happen?

The global phase should be preserved, as stated in the `PadDynamicalDecoupling` documentation:
https://github.com/Qiskit/qiskit/blob/cf46ab8dca2cbb79946d92b741b250fcc25dc2f6/qiskit/transpiler/passes/scheduling/padding/dynamical_decoupling.py#L51-L52

### AI/LLM disclosure

- I developed this as part of IBM Research's Spotlights project on AI-native software optimization.
