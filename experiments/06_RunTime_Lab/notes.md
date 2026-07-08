Can an Engine take its proven execution order and resolve each Module to a runtime implementation?

Experiment Result: RuntimeRegistry successfully registered ModuleRuntime objects and resolved Modules from Engine-derived execution order to their associated implementations.

RUNTIME LAB NOTES
=================

PURPOSE

The purpose of the Runtime Lab was to begin bridging the abstract MIOS
architecture with real executable musical implementations.

Before this experiment, MIOS could:

- Define SignalTypes
- Define Module Endpoints
- Construct Modules
- Validate Connections through MIOSCore
- Admit valid Modules and Connections into the Graph
- Derive Module execution order through the Engine

However, Modules remained architectural descriptions.

A Module could describe WHAT musical capability existed, but MIOS had no
mechanism for associating that Module with the software responsible for
performing its work.


MODULE RUNTIME
==============

ModuleRuntime was introduced with one primary responsibility:

Associate a MIOS Module with its implementation.

Example:

Delay
    ↓
ModuleRuntime
    ↓
delay.pd


This established an important architectural distinction:

Module
→ Describes WHAT the musical object is.

ModuleRuntime
→ Describes HOW the musical object is implemented.


The first ModuleRuntime experiment successfully associated:

Delay → delay.pd

This proved that MIOS could connect an architectural Module with a description
of its implementation.


ENGINE AND RUNTIME INTEGRATION
==============================

The next experiment connected the previously proven Engine architecture with
ModuleRuntime.

The Engine derived the execution order:

Amp
Looper
Delay

Each Module was then associated with a ModuleRuntime:

Amp    → amp.pd
Looper → looper.pd
Delay  → delay.pd


This produced the first conceptual path from instrument structure toward
implementation:

Graph
    ↓
Engine
    ↓
Execution Order
    ↓
Module
    ↓
ModuleRuntime
    ↓
Implementation


RUNTIME REGISTRY
================

The Engine and ModuleRuntime integration exposed a new architectural problem:

Who is responsible for locating the ModuleRuntime associated with a Module?


Initially, test_runtime.py performed this responsibility using a nested loop.

For every Module in the Engine execution order, the test searched through all
known ModuleRuntime objects until it found a match.

Although this worked, runtime resolution did not belong to:

- Module
- MIOSCore
- Graph
- Engine
- ModuleRuntime

This responsibility earned the creation of a new specialist:

**RuntimeRegistry**


RuntimeRegistry has two primary responsibilities:

1. Register known ModuleRuntime objects.

2. Resolve a Module to its associated ModuleRuntime.


The resulting architecture became:

Graph
    ↓
Engine
    ↓
Execution Order
    ↓
Module
    ↓
RuntimeRegistry
    ↓
ModuleRuntime
    ↓
Implementation


The RuntimeRegistry experiment successfully registered and resolved:

Amp    → amp.pd
Looper → looper.pd
Delay  → delay.pd


REAL IMPLEMENTATION RESOLUTION
==============================

Until this point, implementation names such as:

amp.pd
delay.pd
looper.pd

were placeholder strings.

The next experiment connected ModuleRuntime to the real filesystem of the
Raspberry Pi.

A real Pure Data patch was created:

/home/patch/MIOS/pd/test_tone.pd


ModuleRuntime was given the ability to determine whether its associated
implementation exists.

The experiment proved:

Real implementation path
→ True

Nonexistent implementation path
→ False


This represented an important transition.

Before:

MIOS reasoned only about abstract software objects.

After:

MIOS could associate an architectural Module with a real implementation
resource existing on the physical system.


FIRST EXECUTABLE IMPLEMENTATION
===============================

The test_tone.pd patch was manually tested using Pure Data.

The patch contained:

osc~ 440
    ↓
*~ 0.1
    ↓
dac~


The patch successfully produced audio through the Raspberry Pi audio system.

This independently proved that the implementation resource associated with
ModuleRuntime was capable of performing real musical work.


FIRST MIOS VERTICAL SLICE
=========================

The next experiment used Python subprocess execution to launch the real
Pure Data implementation referenced by ModuleRuntime.

The resulting path was:

SignalType
    ↓
Endpoint
    ↓
Module
    ↓
Connection
    ↓
MIOSCore
    ↓
Graph
    ↓
Engine
    ↓
Execution Order
    ↓
RuntimeRegistry
    ↓
ModuleRuntime
    ↓
Real Pure Data Implementation
    ↓
Operating System Process
    ↓
Pure Data


The experiment successfully caused MIOS execution beginning in Python to open
the real test_tone.pd implementation.


MODULE ZERO
===========

The final Runtime Lab experiment added automatic DSP activation to the Pure
Data patch.

The patch used:

loadbang
    ↓
pd dsp 1


This allowed the Pure Data implementation to begin processing audio
automatically when launched.

The complete execution path became:

MIOS Python Process
    ↓
Graph
    ↓
Engine
    ↓
RuntimeRegistry
    ↓
ModuleRuntime
    ↓
test_tone.pd
    ↓
Pure Data
    ↓
Automatic DSP Activation
    ↓
440 Hz Oscillator
    ↓
Audio Output
    ↓
Physical Sound


For the first time, execution beginning within MIOS resulted in autonomous
musical behavior on the physical hardware.


EXPERIMENT RESULT
=================

The Runtime Lab successfully proved that MIOS can:

- Associate architectural Modules with implementations.

- Register and resolve ModuleRuntime objects.

- Connect Engine-derived execution order with runtime resolution.

- Associate a ModuleRuntime with a real implementation resource.

- Verify whether the implementation exists on the physical system.

- Launch a real Pure Data implementation.

- Cause the implementation to automatically begin audio processing.

- Produce physical sound as the result of execution beginning within MIOS.


PROVEN ARCHITECTURAL RESPONSIBILITIES
=====================================

Module
→ Defines WHAT musical capability exists.

MIOSCore
→ Determines whether architectural relationships are lawful.

Graph
→ Maintains the truthful structural state of the instrument.

Engine
→ Determines WHEN Module work must occur based on Graph dependencies.

ModuleRuntime
→ Associates a Module with HOW its work is implemented.

RuntimeRegistry
→ Registers and resolves known ModuleRuntime objects.


CURRENT MIOS ARCHITECTURE
=========================

SignalType
    ↓
Endpoint
    ↓
Module
    ↓
Connection
    ↓
MIOSCore
    ↓
Graph
    ↓
Engine
    ↓
RuntimeRegistry
    ↓
ModuleRuntime
    ↓
Executable Implementation
    ↓
Pure Data
    ↓
Audio Hardware
    ↓
Physical Sound


CONCLUSION
==========

The Runtime Lab marks the first complete vertical slice through the MIOS
architecture.

MIOS has crossed the boundary between describing an instrument and causing
musical work to occur.

The architecture remained specialized throughout the experiment.

No existing object was required to abandon its established responsibility.

Instead, new responsibilities were identified through experimentation and
assigned to specialized architectural roles.

The resulting system remains simple at the surface while allowing increasing
depth beneath the architecture.

The first MIOS Module successfully transitioned from an architectural
description into executable musical behavior.

Module Zero spoke its first word:
"dada?"