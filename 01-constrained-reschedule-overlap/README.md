# Comment for https://github.com/Qiskit/qiskit/issues/16186 (ConstrainedReschedule start times overlap)

Here is another case on main where the start times overlap, this time for two consecutive gates. On `FakePrague`, `sx` on qubit 0 takes 7 dt, and the pulse and acquire alignments are 1 and 16 dt.

```python
from qiskit import QuantumCircuit
from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import ALAPScheduleAnalysis, ConstrainedReschedule
from qiskit_ibm_runtime.fake_provider import FakePrague

qc = QuantumCircuit(1)
qc.delay(100, 0)
qc.sx(0)
qc.sx(0)

target = FakePrague().target
pm = PassManager([ALAPScheduleAnalysis(target=target), ConstrainedReschedule(target=target)])
pm.run(qc)
start_times = pm.property_set["node_start_time"]
print(sorted(t for node, t in start_times.items() if node.op.name == "sx"))
```

```
[112, 112]
```

Both `sx` gates start at 112 dt, so they overlap by 7 dt.

With https://github.com/Qiskit/qiskit/issues/16482 applied on top of main, this example gives `[100, 107]`, which is correct. However, the overlap is still there with https://github.com/Qiskit/qiskit/issues/16482 when the pulse alignment really is 16, for example after setting `target.pulse_alignment = 16` in the snippet above: it still prints `[112, 112]`, while I would expect `[112, 128]`.

I think the problem is that the target branch adds the gate duration in seconds, cast with `as u64`, to a start time in dt. Since 7 dt is much less than one second, this adds zero:
https://github.com/Qiskit/qiskit/blob/cf46ab8dca2cbb79946d92b741b250fcc25dc2f6/crates/transpiler/src/passes/constrained_reschedule.rs#L123-L124

Tested on main cf46ab8dca, Python 3.13.12, Linux, qiskit-ibm-runtime 0.51.0.

### AI/LLM disclosure

- I developed this as part of IBM Research's Spotlights project on AI-native software optimization.
