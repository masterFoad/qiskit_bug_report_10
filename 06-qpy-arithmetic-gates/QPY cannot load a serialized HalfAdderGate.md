### Environment

- Qiskit: 2.6.1 and 2.7.0.dev0 (main `0f2d7ddfd262b1fa3afbc27f733e5c9f6cc6426d`)
- Python: 3.13.12
- OS: Linux 5.14.0-687.58.1.el9_8.x86_64 (x86_64)

### What is happening?

QPY successfully writes a circuit containing HalfAdderGate(2). Loading the buffer raises a TypeError about the required `num_state_qubits` argument.

### How can we reproduce the issue?

```python
import io
from qiskit import QuantumCircuit, qpy
from qiskit.circuit.library import HalfAdderGate
qc = QuantumCircuit(5)
qc.append(HalfAdderGate(2), range(5))
payload = io.BytesIO()
qpy.dump(qc, payload)
payload.seek(0)
qpy.load(payload)
# TypeError: HalfAdderGate.__init__() missing 1 required positional argument: 'num_state_qubits'
```

### What should happen?

QPY should load the circuit with HalfAdderGate(2) preserved.
