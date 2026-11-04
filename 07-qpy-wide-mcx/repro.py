import io
from qiskit import QuantumCircuit, qpy
from qiskit.circuit.library import MCXGate
qc = QuantumCircuit(33)
qc.append(MCXGate(32), range(33))
payload = io.BytesIO()
qpy.dump(qc, payload)
try: qpy.load(io.BytesIO(payload.getvalue()))
except Exception as exc: print(type(exc).__name__); print(str(exc))
