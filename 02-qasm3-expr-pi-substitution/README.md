# QASM 3 export corrupts a constant in a parameter expression

### Environment

- Qiskit: 2.6.1 and 2.7.0.dev0 (main `0f2d7ddfd262b1fa3afbc27f733e5c9f6cc6426d`)
- Python: 3.13.12
- OS: Linux x86_64

### What is happening?

The exported RZ expression contains `2pi + pi*th`. Its constant should represent `20 + pi`. The output is invalid OpenQASM 3 and does not preserve that constant.

### How can we reproduce the issue?

```python
from math import pi
from qiskit import QuantumCircuit, qasm3
from qiskit.circuit import Parameter

qc = QuantumCircuit(1)
qc.rz(Parameter('th') * pi + 23.141592653589793, 0)

print(next(line for line in qasm3.dumps(qc).splitlines() if line.startswith('rz')))
# rz(2pi + pi*th) q[0];
```

### What should happen?

QASM 3 export should preserve the parameter expression's value and emit valid OpenQASM 3 syntax.
