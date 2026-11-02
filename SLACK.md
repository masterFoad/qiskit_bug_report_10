Hi @arbel @shelly @alexi, I've prepared minimal reproductions of eleven more bugs (ten in Qiskit, one in Qiskit Aer). Each folder includes a short script and issue draft:

* ConstrainedReschedule overlaps sequential SX gates: https://github.com/masterFoad/qiskit_bug_report_10/tree/main/01-constrained-reschedule-overlap
* QASM 3 export corrupts a constant in a parameter expression: https://github.com/masterFoad/qiskit_bug_report_10/tree/main/02-qasm3-expr-pi-substitution
* InstructionDurationCheck misses an acquire-alignment violation: https://github.com/masterFoad/qiskit_bug_report_10/tree/main/03-instruction-duration-check-mixed-alignment
* Single-gate dynamical decoupling changes global phase: https://github.com/masterFoad/qiskit_bug_report_10/tree/main/04-dd-single-gate-global-phase
* QPY round trip makes a parameterized delay unreadable: https://github.com/masterFoad/qiskit_bug_report_10/tree/main/05-qpy-parameterized-delay-unloadable
* QPY cannot load a serialized HalfAdderGate: https://github.com/masterFoad/qiskit_bug_report_10/tree/main/06-qpy-arithmetic-gates
* QPY writes a 32-control MCX that it cannot load: https://github.com/masterFoad/qiskit_bug_report_10/tree/main/07-qpy-wide-mcx
* ECR reversal fails with CZ on another target edge: https://github.com/masterFoad/qiskit_bug_report_10/tree/main/08-ecr-reversal-heterogeneous-target
* Seeded compilation varies idle-wire initial layouts: https://github.com/masterFoad/qiskit_bug_report_10/tree/main/09-layout-initial-layout-variability
* num_basis_gates reports zero for a three-CX decomposition: https://github.com/masterFoad/qiskit_bug_report_10/tree/main/10-num-basis-gates-estimator-mismatch
* AerSimulator returns a density matrix with trace 2 after a statevector circuit (Qiskit Aer): https://github.com/masterFoad/qiskit_bug_report_10/tree/main/11-aer-noise-applied-twice

The Qiskit ones reproduce on 2.6.1 and main; the Aer one on qiskit-aer 0.18.2. Will appreciate your review, thanks!
