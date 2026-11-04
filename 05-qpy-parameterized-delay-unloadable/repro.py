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
