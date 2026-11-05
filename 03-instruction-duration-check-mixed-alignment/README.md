# InstructionDurationCheck misses acquire alignment on FakePrague

### Environment

- **Qiskit version**: 2.7.0.dev0 (main cf46ab8dca)
- **qiskit-ibm-runtime version**: 0.51.0
- **Python version**: 3.13.12
- **Operating system**: Linux

### What is happening?

`InstructionDurationCheck` does not flag a measurement that is not aligned to the acquire grid. On `FakePrague`, the pulse alignment is 1 dt and the acquire alignment is 16 dt. After a delay of 100 dt, the measurement starts at 100 dt, which is not a multiple of 16, but the pass returns `reschedule_required=False`.

### How can we reproduce the issue?

Here is a short reproducer:

```python
from qiskit import QuantumCircuit
from qiskit.transpiler.passes import InstructionDurationCheck
from qiskit_ibm_runtime.fake_provider import FakePrague

qc = QuantumCircuit(1, 1)
qc.delay(100, 0)
qc.measure(0, 0)

check = InstructionDurationCheck(target=FakePrague().target)
check(qc)
print(check.property_set["reschedule_required"])
```

This prints `False`.

### What should happen?

`reschedule_required` should be `True`, since 100 dt is not aligned to the 16 dt acquire grid.

### Any suggestions?

The Python version of the check (before #14700) required both remainders to be zero, while the Rust version uses `||`:
https://github.com/Qiskit/qiskit/blob/cf46ab8dca2cbb79946d92b741b250fcc25dc2f6/crates/transpiler/src/passes/instruction_duration_check.rs#L74-L76

### AI/LLM disclosure

- I developed this as part of IBM Research's Spotlights project on AI-native software optimization.
