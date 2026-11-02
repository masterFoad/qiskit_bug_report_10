import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import XGate
from qiskit.quantum_info import Operator
from qiskit.transpiler import InstructionDurations, PassManager
from qiskit.transpiler.passes import ALAPScheduleAnalysis, PadDynamicalDecoupling
qc = QuantumCircuit(1)
qc.u(.4, -.6, 1.3, 0)
qc.delay(300, 0)
d = InstructionDurations([('u', None, 50), ('x', None, 50)], dt=1e-9)
out = PassManager([ALAPScheduleAnalysis(d), PadDynamicalDecoupling(d, [XGate()])]).run(qc)
print(Operator(out).equiv(qc), np.angle(np.vdot(Operator(qc).data, Operator(out).data)))
# True -2.5415926535897935
