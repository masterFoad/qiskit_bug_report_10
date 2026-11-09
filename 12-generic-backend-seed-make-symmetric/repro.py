from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.transpiler import CouplingMap

for _ in range(20):
    coupling = CouplingMap([(0, 1), (1, 2)])
    coupling.make_symmetric()
    backend = GenericBackendV2(
        3, basis_gates=["u", "cz"], coupling_map=coupling, seed=11
    )
    prop = backend.target["cz"][(1, 0)]
    print(prop.duration, prop.error)
