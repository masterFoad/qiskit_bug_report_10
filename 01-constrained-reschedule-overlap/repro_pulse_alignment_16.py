from qiskit import QuantumCircuit
from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import ALAPScheduleAnalysis, ConstrainedReschedule
from qiskit_ibm_runtime.fake_provider import FakePrague

qc = QuantumCircuit(1)
qc.delay(100, 0)
qc.sx(0)
qc.sx(0)

target = FakePrague().target
target.pulse_alignment = 16
pm = PassManager([ALAPScheduleAnalysis(target=target), ConstrainedReschedule(target=target)])
pm.run(qc)
start_times = pm.property_set["node_start_time"]
print(sorted(t for node, t in start_times.items() if node.op.name == "sx"))
