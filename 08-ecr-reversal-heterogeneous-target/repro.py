from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.circuit.library import CZGate, ECRGate, RZGate, SXGate
from qiskit.transpiler import Target, generate_preset_pass_manager

target = Target(num_qubits=3)
for gate in (RZGate(Parameter('t')), SXGate()):
    target.add_instruction(gate, {(q,): None for q in range(3)})
target.add_instruction(CZGate(), {(0, 1): None, (1, 0): None})
target.add_instruction(ECRGate(), {(1, 2): None})
qc = QuantumCircuit(3)
qc.ecr(2, 1)
pm = generate_preset_pass_manager(optimization_level=0, target=target)
pm.run(qc)
# qiskit.transpiler.exceptions.TranspilerError: 'ecr would be supported on [Qubit(2), Qubit(1)] if the direction was swapped, but no rules are known to do that. ["cx", "cz", "ecr", "swap", "rzx", "rxx", "ryy", "rzz"] can be automatically flipped.'
