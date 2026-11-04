Another example for the missing-delay-unit issue, using a parameterized duration.


### Environment

- **Qiskit version**: 2.7.0.dev0, main cf46ab8dca
- **Python version**: 3.13.12
- **Operating system**: Linux x86_64

### What is happening?

After a QPY round trip, accessing the operation for a delay whose duration is Parameter("t")
raises CircuitError. qpy.load returns; the failure happens when accessing the loaded operation.

### How can we reproduce the issue?

```python
import io
from qiskit import QuantumCircuit, qpy
from qiskit.circuit import Parameter
qc = QuantumCircuit(1)
qc.delay(Parameter("t"), 0, "dt")
payload = io.BytesIO()
qpy.dump(qc, payload)
loaded = qpy.load(io.BytesIO(payload.getvalue()))[0]
try: print(loaded.data[0].operation)
except Exception as exc: print(type(exc).__name__); print(str(exc))
# CircuitError
# 'Unknown unit expr is specified.'
```

### What should happen?

The loaded delay should remain accessible with its parameter and dt unit.

Related:
- https://github.com/Qiskit/qiskit/pull/16806

### AI/LLM disclosure

- I found this as part of IBM Research's Spotlights project on AI-native software optimization.
