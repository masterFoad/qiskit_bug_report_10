from qiskit import QuantumCircuit, transpile
from qiskit.circuit import Parameter
from qiskit.circuit.library import CZGate, ECRGate, RZGate, SXGate, XGate
from qiskit.transpiler import Target
target = Target(num_qubits=3)
for gate in (RZGate(Parameter("t")), SXGate(), XGate()):
    target.add_instruction(gate, {(q,): None for q in range(3)})
target.add_instruction(CZGate(), {(0, 1): None, (1, 0): None})
target.add_instruction(ECRGate(), {(1, 2): None})
qc = QuantumCircuit(3); qc.ecr(2, 1)
try: print(transpile(qc, target=target, optimization_level=0, initial_layout=[0, 1, 2]))
except Exception as exc: print(type(exc).__name__); print(*str(exc).split(", "), sep="\n")
