import io
from qiskit import QuantumCircuit, qpy
from qiskit.circuit.library import HalfAdderGate
qc = QuantumCircuit(5)
qc.append(HalfAdderGate(2), range(5))
payload = io.BytesIO()
qpy.dump(qc, payload)
try: qpy.load(io.BytesIO(payload.getvalue()))
except Exception as exc: print(type(exc).__name__); print(str(exc))
