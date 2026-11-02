from qiskit import QuantumCircuit
from qiskit.transpiler.passes import InstructionDurationCheck
qc = QuantumCircuit(1, 1)
qc.delay(100, 0)
qc.measure(0, 0)
p = InstructionDurationCheck(acquire_alignment=16, pulse_alignment=1)
p(qc)
print(p.property_set['reschedule_required'])
# False
