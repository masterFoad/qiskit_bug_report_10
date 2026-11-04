from qiskit import QuantumCircuit
from qiskit.circuit.library import CXGate
from qiskit.quantum_info import Operator
from qiskit.synthesis import TwoQubitBasisDecomposer
qc = QuantumCircuit(2); qc.h(0); qc.swap(0, 1)
unitary = Operator(qc).data
decomposer = TwoQubitBasisDecomposer(CXGate(), basis_fidelity=1.0)
print(decomposer.num_basis_gates(unitary), decomposer(unitary).count_ops().get("cx", 0))
