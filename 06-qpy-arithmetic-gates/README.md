I verified the HalfAdderGate(2) case listed here on current main.


### Environment

- **Qiskit version**: 2.7.0.dev0, main cf46ab8dca
- **Python version**: 3.13.12
- **Operating system**: Linux x86_64

### What is happening?

qpy.dump accepts the circuit containing HalfAdderGate(2), but qpy.load raises TypeError. This is
the HalfAdderGate case already listed in #17040.

### How can we reproduce the issue?

```python
import io
from qiskit import QuantumCircuit, qpy
from qiskit.circuit.library import HalfAdderGate
qc = QuantumCircuit(5)
qc.append(HalfAdderGate(2), range(5))
payload = io.BytesIO()
qpy.dump(qc, payload)
try: qpy.load(io.BytesIO(payload.getvalue()))
except Exception as exc: print(type(exc).__name__); print(str(exc))
# TypeError
# HalfAdderGate.__init__() missing 1 required positional argument: 'num_state_qubits'
```

### What should happen?

The circuit produced by qpy.dump should load with the HalfAdderGate constructor state preserved.

Related:
- https://github.com/Qiskit/qiskit/pull/16943

### AI/LLM disclosure

- I found this as part of IBM Research's Spotlights project on AI-native software optimization.
