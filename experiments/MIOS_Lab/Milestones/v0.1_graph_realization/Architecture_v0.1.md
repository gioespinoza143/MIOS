# MIOS Prototype v0.1
## Graph Realization

Mission:

Prove that MIOS can describe a Camino,
plan its realization,
generate backend commands,
generate a Pure Data patch,
and launch that patch.

Status:

SUCCESS

Architecture
------------
Graph
↓
Engine
↓
RuntimeResolver
↓
CaminoPlanner
↓
Comandante
↓
PDRealizer
↓
Generated Camino
↓
ProcessManager
↓
Pure Data

# Architecture Terms
Graph
Represents signal flow.
---
RuntimeResolver
Maps Modules to backend implementations.
---
CaminoPlanner
Produces realization plan.
---
Comandante
Produces backend-independent commands.
---
PDRealizer
Translates commands into Pure Data.
---
ProcessManager
Launches backend implementations.