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
