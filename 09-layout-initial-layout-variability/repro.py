from qiskit import QuantumCircuit
from qiskit.transpiler import CouplingMap, generate_preset_pass_manager
qc = QuantumCircuit(6)
for a, b in ((0, 1), (1, 2), (0, 2)):
    qc.cx(a, b)
pm = generate_preset_pass_manager(optimization_level=2, basis_gates=['rz', 'sx', 'x', 'cz'],
                                  coupling_map=CouplingMap.from_line(6), seed_transpiler=1)
layouts = {tuple(pm.run(qc).layout.initial_index_layout()) for _ in range(20)}
print(sorted(layouts))
# [(1, 2, 0, 3, 4, 5), (1, 2, 0, 4, 3, 5)]
