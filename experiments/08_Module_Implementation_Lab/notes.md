PHYSICAL WORLD PERSPECTIVE

Audio Input
→ audio enters the instrument

Audio Output
→ audio leaves the instrument

### Why Implement PureData?
MIOS                    PURE DATA

Module          ↔       Abstraction
Endpoint        ↔       inlet / outlet
Connection      ↔       Patch Cord
Graph           ↔       Patch
Engine          ↔       Execution Planning
ModuleRuntime   ↔       Implementation Binding
ProcessManager  ↔       Running PD Instance

# Goal for implementation
MIOS ARCHITECTURE          PD IMPLEMENTATION

AudioInput                 audio_input.pd
     ↓                           ↓
Gain                       gain.pd
     ↓                           ↓
AudioOutput                audio_output.pd

### MIOS MODULE IMPLEMENTATION LAB — v0.1

PURPOSE

The purpose of the Module Implementation Lab was to begin applying the
existing MIOS architecture to real musical Modules and physical audio
implementations.

Previous experiments proved the shared MIOS architecture using abstract Modules such as Amp, Delay, and Looper.

This Lab asked a new question:
Can the existing MIOS architecture truthfully describe real musical Modules and correspond to a working physical signal path?


--------------------------------------------------
MODULE CAPABILITY LANGUAGE
--------------------------------------------------

The existing Module class originally understood:

accepts(signal)

This allowed a Module to determine whether one of its input Endpoints matched the SignalType carried by a Signal.

During the implementation of AudioInput and AudioOutput, the need for an opposite capability became clear:

produces(signal)

The Module class was extended with produces().

The resulting Module capability vocabulary is:

accepts(signal)
    → examines Module input Endpoints

produces(signal)
    → examines Module output Endpoints


--------------------------------------------------
FIRST REAL MODULE ROLES
--------------------------------------------------

Three fundamental Module roles were proven.


SOURCE

AudioInput

inputs:
    []

outputs:
    AUDIO

accepts AUDIO:
    False

produces AUDIO:
    True


PROCESSOR

Gain

inputs:
    AUDIO

outputs:
    AUDIO

accepts AUDIO:
    True

produces AUDIO:
    True


SINK

AudioOutput

inputs:
    AUDIO

outputs:
    []

accepts AUDIO:
    True

produces AUDIO:
    False


These results demonstrated that Module behavior is described relative
to the MIOS Graph.

AudioInput does not accept AUDIO from another MIOS Module. It produces AUDIO into the Graph.

AudioOutput accepts AUDIO from the Graph.
It does not produce AUDIO to another downstream MIOS Module.


--------------------------------------------------
FIRST REAL MIOS CAMINO
--------------------------------------------------

The first real MIOS Camino was constructed using:

AudioInput
    ↓
Gain
    ↓
Delay
    ↓
AudioOutput

Each Module was represented using the existing MIOS shared language:

SignalType
Signal
Endpoint
Module
Connection
MIOSCore
Graph
Engine

The Graph admitted the Modules and Connections.

MIOSCore validated the requested Connections.

Engine derived the correct execution order:

Audio Input
Gain
Delay
Audio Output


--------------------------------------------------
PURE DATA MODULE IMPLEMENTATIONS
--------------------------------------------------

Reusable Pure Data abstractions were created:

audio_input.pd
gain.pd
delay.pd
audio_output.pd

These abstractions were hosted by:

first_camino.pd

The resulting Pure Data topology was:

audio_input
    ↓
gain
    ↓
delay
    ↓
audio_output


--------------------------------------------------
PHYSICAL AUDIO PROOF
--------------------------------------------------

A physical bass guitar signal was connected to the Pisound input.

The signal traveled through:

Bass Guitar
    ↓
Pisound Input
    ↓
audio_input.pd
    ↓
gain.pd
    ↓
delay.pd
    ↓
audio_output.pd
    ↓
Pisound Output

Real processed audio was successfully heard.

This proved that reusable Pure Data abstractions can represent the same
fundamental musical topology described by the MIOS Graph.


--------------------------------------------------
DELAY IMPLEMENTATION DISCOVERY
--------------------------------------------------

The first Delay implementation produced the Pure Data warning:

mios_delay: multiply defined

The delay buffer was changed from:

mios_delay

to:

$0-mios_delay

This gave each Delay abstraction instance its own private delay memory.

This experiment revealed an important future requirement:

Reusable Module implementations must support instance-local resources.


--------------------------------------------------
CHANNEL CONFIGURATION DISCOVERY
--------------------------------------------------

The physical bass input was mono.
Sending the signal to only one physical output resulted in audio from
only one side.

The current physical Camino duplicates the mono signal at the
AudioOutput implementation and sends it to both hardware outputs.

This creates dual mono output.

The experiment revealed a future architectural question:

How should MIOS represent channel configuration?

Possible future concepts include:

MONO
DUAL MONO
STEREO
MULTICHANNEL

No architectural changes were made yet.

The current MIOS architecture continues to represent SignalType.AUDIO
independently from future channel-layout behavior.


--------------------------------------------------
MAJOR ARCHITECTURAL DISCOVERY
--------------------------------------------------

The experiment established an important distinction:

Module Implementation
    ≠
Operating System Process

The emerging runtime model is:

Each Module
    ↓
owns or resolves to a reusable implementation

Entire Camino
    ↓
is hosted inside one managed runtime environment

For the current implementation:

Module
    ↓
Pure Data abstraction

Camino
    ↓
Pure Data host patch

Running Camino
    ↓
one Pure Data process


--------------------------------------------------
CURRENT ARCHITECTURAL TRUTH
--------------------------------------------------

MIOS ARCHITECTURE

AudioInput
    ↓
Gain
    ↓
Delay
    ↓
AudioOutput


PURE DATA IMPLEMENTATION

audio_input.pd
    ↓
gain.pd
    ↓
delay.pd
    ↓
audio_output.pd


PHYSICAL REALITY

Bass
    ↓
Pisound
    ↓
Gain
    ↓
Delay
    ↓
Pisound Output
    ↓
Sound


The same fundamental topology now exists at three levels:

1. Architectural truth
2. Runtime implementation
3. Physical musical reality


--------------------------------------------------
KNOWN FUTURE QUESTIONS
--------------------------------------------------

The following problems were deliberately NOT solved in this Lab:

- Dynamic generation of Pure Data Caminos
- Runtime modification of a living Camino
- MIDI parameter control
- Channel-layout representation
- Stereo and multichannel routing
- Runtime readiness
- Graceful Pure Data shutdown
- GUI implementation
- Preset management
- Module parameter systems

These responsibilities remain future work.


--------------------------------------------------
MODULE IMPLEMENTATION LAB v0.1 CONCLUSION
--------------------------------------------------

The Module Implementation Lab proved that the existing MIOS architecture
can describe real musical Modules.

It also proved that reusable Pure Data abstractions can implement those
Modules inside a physical working audio Camino.

Most importantly, the same topology now exists as:

MIOS Graph Truth
    ↓
Pure Data Implementation
    ↓
Physical Sound

The missing responsibility is now clear:

How does MIOS cause a runtime implementation to become alive based on
the Graph it understands?

This question becomes the foundation of the next experiment:

CAMINO RUNTIME LAB