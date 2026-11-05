from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime.fake_provider import FakeCairoV2

qc = QuantumCircuit(3)
qc.ecr(2, 1)
transpile(qc, target=FakeCairoV2().target, optimization_level=0, initial_layout=[0, 1, 2])
