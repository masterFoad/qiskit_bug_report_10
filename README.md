# Ten Qiskit bug reproductions

Qiskit 2.6.1 and main 0f2d7ddfd2 (2.7.0.dev0).

01. [ConstrainedReschedule overlaps sequential SX gates](01-constrained-reschedule-overlap/) - Sequential SX gates overlap by 4 dt.
02. [QASM 3 export corrupts a constant in a parameter expression](02-qasm3-expr-pi-substitution/) - A constant changes value and becomes invalid syntax.
03. [InstructionDurationCheck misses an acquire-alignment violation](03-instruction-duration-check-mixed-alignment/) - An off-grid acquire leaves reschedule_required False.
04. [Single-gate dynamical decoupling changes global phase](04-dd-single-gate-global-phase/) - A one-gate DD sequence changes global phase.
05. [QPY round trip makes a parameterized delay unreadable](05-qpy-parameterized-delay-unloadable/) - A loaded symbolic delay cannot be accessed.
06. [QPY cannot load a serialized HalfAdderGate](06-qpy-arithmetic-gates/) - A dumped HalfAdderGate cannot be loaded.
07. [QPY writes a 32-control MCX that it cannot load](07-qpy-wide-mcx/) - A dumped MCX with 32 controls cannot be loaded.
08. [ECR reversal fails with CZ on another target edge](08-ecr-reversal-heterogeneous-target/) - CZ on another edge blocks ECR reversal.
09. [Seeded compilation varies idle-wire initial layouts](09-layout-initial-layout-variability/) - The same seed can vary idle-wire initial layouts.
10. [num_basis_gates reports zero for a three-CX decomposition](10-num-basis-gates-estimator-mismatch/) - The estimate is 0 when synthesis uses 3 CX gates.
