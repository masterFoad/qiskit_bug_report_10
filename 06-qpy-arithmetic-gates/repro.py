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
