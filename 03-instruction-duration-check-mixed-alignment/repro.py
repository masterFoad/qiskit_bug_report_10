from qiskit import QuantumCircuit
from qiskit.transpiler.passes import InstructionDurationCheck
from qiskit_ibm_runtime.fake_provider import FakePrague

qc = QuantumCircuit(1, 1)
qc.delay(100, 0)
qc.measure(0, 0)

check = InstructionDurationCheck(target=FakePrague().target)
check(qc)
print(check.property_set["reschedule_required"])
