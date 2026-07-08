Engine derives Module execution order from Graph dependency structure independently of Connection insertion order.

Experiment Result 01: Engine successfully derived execution order independently of Connection insertion order and raised an explicit error when no valid execution order could be derived from cyclic dependencies.

Experiment Result 02: 
VALID BUT UNEXECUTABLE GRAPH

Amp → Delay → Looper
 ↑               │
 └───────────────┘

Engine derives:

ValueError:
Graph contains unresolved dependencies.

Experiment Result 03:
POTENTIAL MIOS BRANCHING CONFIGURATIONS
        ┌──→ Delay
Amp ────┤
        └──→ Looper

or:

TriplePlay
    │
    ├──→ Synth
    │
    └──→ Control Mapper

### engine_v0_1_proof is a success
The engine is able to process connections between modules independent of one another or converging.