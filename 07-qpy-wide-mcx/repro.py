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
