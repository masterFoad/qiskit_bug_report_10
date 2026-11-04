# Single-X dynamical decoupling changes global phase

### Environment

- **Qiskit version**: 2.7.0.dev0, main cf46ab8dca
- **Python version**: 3.13.12
- **Operating system**: Linux x86_64

### What is happening?

With the single-X sequence below, the output is equivalent up to global phase, but Operator(out)
== Operator(qc) is False. Only this U gate followed by a delay was tested.

### How can we reproduce the issue?

```python
from qiskit import QuantumCircuit
from qiskit.circuit.library import XGate
from qiskit.quantum_info import Operator
from qiskit.transpiler import InstructionDurations, PassManager
from qiskit.transpiler.passes import ALAPScheduleAnalysis, PadDynamicalDecoupling
qc = QuantumCircuit(1); qc.u(.4, -.6, 1.3, 0); qc.delay(300, 0)
durations = InstructionDurations([("u", None, 50), ("x", None, 50)], dt=1e-9)
out = PassManager([ALAPScheduleAnalysis(durations),
                   PadDynamicalDecoupling(durations, [XGate()])]).run(qc)
print(Operator(out).equiv(qc), Operator(out) == Operator(qc))
# True False
```

### What should happen?

The output should preserve the circuit including global phase, as stated in the
PadDynamicalDecoupling documentation.

Related:
- https://github.com/Qiskit/qiskit/issues/10569
- https://github.com/Qiskit/qiskit/pull/10631

### AI/LLM disclosure

- I found this as part of IBM Research's Spotlights project on AI-native software optimization.
