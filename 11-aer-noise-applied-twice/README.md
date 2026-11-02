# AerSimulator returns a density matrix with trace 2 after a statevector circuit

### Environment

- qiskit-aer: 0.18.2
- Qiskit: 2.6.1
- Python: 3.13.12
- OS: Linux x86_64

### What is happening?

An automatic mixed-method run puts a statevector save first, then a noisy density-matrix save. The saved trace is 2, while running alone or in reversed order gives trace 1.

### How can we reproduce the issue?

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, phase_amplitude_damping_error

noise = NoiseModel()
noise.add_all_qubit_quantum_error(phase_amplitude_damping_error(.2, 0), ['x'])
sv = QuantumCircuit(1)
sv.save_statevector()
dm = QuantumCircuit(1)
dm.x(0)
dm.save_density_matrix()
result = AerSimulator(noise_model=noise).run([sv, dm]).result()

print(round(result.data(1)['density_matrix'].trace().real, 6))
# 2.0
```

### What should happen?

The saved density matrix trace should remain 1 regardless of batch order.
