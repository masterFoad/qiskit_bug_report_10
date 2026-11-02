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
