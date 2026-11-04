from qiskit import QuantumCircuit
from qiskit.circuit.library import XGate
from qiskit.quantum_info import Operator
from qiskit.transpiler import InstructionDurations, PassManager
from qiskit.transpiler.passes import ALAPScheduleAnalysis, PadDynamicalDecoupling
qc = QuantumCircuit(1); qc.u(.4, -.6, 1.3, 0); qc.delay(300, 0)
durations = InstructionDurations([("u", None, 50), ("x", None, 50)], dt=1e-9)
out = PassManager([ALAPScheduleAnalysis(durations),
                   PadDynamicalDecoupling(durations, [XGate()])]).run(qc)
print(Operator(out).equiv(qc), Operator(out) == Operator(qc))
