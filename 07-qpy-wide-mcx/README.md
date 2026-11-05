# QPY cannot load a dumped MCXGate(32)

### Environment

- **Qiskit version**: 2.7.0.dev0 (main cf46ab8dca)
- **Python version**: 3.13.12
- **Operating system**: Linux

### What is happening?

QPY can dump a circuit with an `MCXGate` with 32 controls, but cannot load it back.

### How can we reproduce the issue?

Here is a short reproducer:

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
```

which raises:

```
qiskit.qpy.exceptions.QpyError: 'invalid instruction: Instruction has 32 but at most 31 are supported'
```

### What should happen?

`qpy.load` should be able to read what `qpy.dump` writes. If 32 controls are not supported by QPY, then `qpy.dump` should raise an error instead of writing a file that cannot be loaded.

Possibly related: #17040, #9684.

### AI/LLM disclosure

- I developed this as part of IBM Research's Spotlights project on AI-native software optimization.
