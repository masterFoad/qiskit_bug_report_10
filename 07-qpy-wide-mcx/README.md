# QPY writes a 32-control MCX that it cannot load

### Environment

- Qiskit: 2.6.1 and 2.7.0.dev0 (main `0f2d7ddfd262b1fa3afbc27f733e5c9f6cc6426d`)
- Python: 3.13.12
- OS: Linux x86_64

### What is happening?

QPY successfully writes an MCX gate with 32 controls. Loading the buffer raises a QpyError stating that at most 31 are supported.

### How can we reproduce the issue?

```python
import io
from qiskit import QuantumCircuit, qpy
from qiskit.circuit.library import MCXGate

qc = QuantumCircuit(33)
qc.append(MCXGate(32), range(33))
payload = io.BytesIO()
qpy.dump(qc, payload)
payload.seek(0)
qpy.load(payload)
# qiskit.qpy.exceptions.QpyError: 'invalid instruction: Instruction has 32 but at most 31 are supported'
```

### What should happen?

QPY should load the 32-control MCX or reject that width during dumping instead of writing an unreadable file.
