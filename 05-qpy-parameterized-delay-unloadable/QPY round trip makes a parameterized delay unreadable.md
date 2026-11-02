### Environment

- Qiskit: 2.6.1 and 2.7.0.dev0 (main `0f2d7ddfd262b1fa3afbc27f733e5c9f6cc6426d`)
- Python: 3.13.12
- OS: Linux 5.14.0-687.58.1.el9_8.x86_64 (x86_64)

### What is happening?

QPY writes and loads a circuit containing a symbolic delay with unit `dt`. Accessing the loaded delay operation then raises `CircuitError: 'Unknown unit expr is specified.'`.

### How can we reproduce the issue?

```python
import io
from qiskit import QuantumCircuit, qpy
from qiskit.circuit import Parameter
qc = QuantumCircuit(1)
qc.delay(Parameter('t'), 0, 'dt')
payload = io.BytesIO()
qpy.dump(qc, payload)
payload.seek(0)
loaded = qpy.load(payload)[0]
print(loaded.data[0].operation)
# qiskit.circuit.exceptions.CircuitError: 'Unknown unit expr is specified.'
```

### What should happen?

The loaded delay should remain readable with its original symbolic duration and `dt` unit.
