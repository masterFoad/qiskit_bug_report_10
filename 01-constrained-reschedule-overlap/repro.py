from qiskit import QuantumCircuit
from qiskit.transpiler import Target, InstructionProperties, PassManager
from qiskit.transpiler.passes import ALAPScheduleAnalysis, ConstrainedReschedule
qc = QuantumCircuit(1); qc.delay(100, 0); qc.sx(0); qc.sx(0)
target = Target(num_qubits=1, dt=1e-9, granularity=1,
                pulse_alignment=16, acquire_alignment=16)
target.add_instruction(qc.data[1].operation, {(0,): InstructionProperties(duration=36e-9)})
pm = PassManager([ALAPScheduleAnalysis(target=target),
                  ConstrainedReschedule(target=target)])
pm.run(qc)
print(sorted(t for n, t in pm.property_set["node_start_time"].items() if n.op.name == "sx"))
