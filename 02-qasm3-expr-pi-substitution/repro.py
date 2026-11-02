from math import pi
from qiskit import QuantumCircuit, qasm3
from qiskit.circuit import Parameter
qc = QuantumCircuit(1)
qc.rz(Parameter('th') * pi + 23.141592653589793, 0)
print(next(line for line in qasm3.dumps(qc).splitlines() if line.startswith('rz')))
# rz(2pi + pi*th) q[0];
