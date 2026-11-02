### Environment

- Qiskit: 2.6.1 and 2.7.0.dev0 (main `0f2d7ddfd262b1fa3afbc27f733e5c9f6cc6426d`)
- Python: 3.13.12
- OS: Linux 5.14.0-687.58.1.el9_8.x86_64 (x86_64)

### What is happening?

Padding the idle interval with `dd_sequence=[XGate()]` changes the operator's global phase by about -2.54 radians. The output is equivalent to the input up to global phase, but their operators are not equal.

### How can we reproduce the issue?

```python
import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import XGate
from qiskit.quantum_info import Operator
from qiskit.transpiler import InstructionDurations, PassManager
from qiskit.transpiler.passes import ALAPScheduleAnalysis, PadDynamicalDecoupling
qc = QuantumCircuit(1)
qc.u(.4, -.6, 1.3, 0)
qc.delay(300, 0)
d = InstructionDurations([('u', None, 50), ('x', None, 50)], dt=1e-9)
out = PassManager([ALAPScheduleAnalysis(d), PadDynamicalDecoupling(d, [XGate()])]).run(qc)
print(Operator(out).equiv(qc), np.angle(np.vdot(Operator(qc).data, Operator(out).data)))
# True -2.5415926535897935
```

### What should happen?

PadDynamicalDecoupling should preserve the input operator exactly, including global phase, as documented.
