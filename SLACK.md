Hi @arbel @shelly @alexi, I've prepared minimal reproductions of ten more Qiskit bugs. Each folder includes a short script and issue draft:

* ConstrainedReschedule overlaps sequential SX gates.
* QASM 3 export corrupts a constant in a parameter expression.
* InstructionDurationCheck misses an acquire-alignment violation.
* Single-gate dynamical decoupling changes global phase.
* QPY round trip makes a parameterized delay unreadable.
* QPY cannot load a serialized HalfAdderGate.
* QPY writes a 32-control MCX that it cannot load.
* ECR reversal fails with CZ on another target edge.
* Seeded compilation varies idle-wire initial layouts.
* num_basis_gates reports zero for a three-CX decomposition.

All ten reproduce on Qiskit 2.6.1 and main. Will appreciate your review, thanks!
