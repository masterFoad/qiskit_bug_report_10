# QPY cannot load a dumped MCXGate(32)

### Environment

- **Qiskit version**: 2.7.0.dev0, main cf46ab8dca
- **Python version**: 3.13.12
- **Operating system**: Linux x86_64

### What is happening?

qpy.dump accepts this 33-qubit circuit containing MCXGate(32), but qpy.load raises QpyError.
Only the 32-control case was tested.

### How can we reproduce the issue?

```python
import io
from qiskit import QuantumCircuit, qpy
from qiskit.circuit.library import MCXGate
qc = QuantumCircuit(33)
qc.append(MCXGate(32), range(33))
payload = io.BytesIO()
qpy.dump(qc, payload)
try: qpy.load(io.BytesIO(payload.getvalue()))
except Exception as exc: print(type(exc).__name__); print(str(exc))
# QpyError
# 'invalid instruction: Instruction has 32 but at most 31 are supported'
```

### What should happen?

qpy.load should read the payload produced by qpy.dump. If 32 controls are unsupported by QPY,
qpy.dump should reject this case before writing an unreadable payload.

Related:
- https://github.com/Qiskit/qiskit/issues/17040
- https://github.com/Qiskit/qiskit/issues/9684

### AI/LLM disclosure

- I found this as part of IBM Research's Spotlights project on AI-native software optimization.
