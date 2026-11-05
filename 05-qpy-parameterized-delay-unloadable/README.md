# Comment draft

Here is another example of the same problem, with a parameterized delay. The circuit can be dumped and loaded, but accessing the loaded delay fails:

```python
import io
from qiskit import QuantumCircuit, qpy
from qiskit.circuit import Parameter

qc = QuantumCircuit(1)
qc.delay(Parameter("t"), 0, "dt")

payload = io.BytesIO()
qpy.dump(qc, payload)
payload.seek(0)
loaded = qpy.load(payload)[0]
loaded.data[0].operation
```

```
qiskit.circuit.exceptions.CircuitError: 'Unknown unit expr is specified.'
```

Tested on main cf46ab8dca, Python 3.13.12, Linux.

### AI/LLM disclosure

- I developed this as part of IBM Research's Spotlights project on AI-native software optimization.
