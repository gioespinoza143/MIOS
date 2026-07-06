# Book III — Architecture

> The systems, responsibilities, and relationships that allow MIOS to behave as a unified instrument.

## The Architectural Question

What systems must exist for MIOS to honor its philosophy?

MIOS must be capable of receiving different forms of musical information and allowing them to travel independently, interact intentionally, and converge to create new sonic possibilities.

To accomplish this without sacrificing modularity, MIOS separates the rules of the instrument from the work performed within it.

The MIOS Core understands the fundamental types of musical signals and the rules that determine how they may connect.

Individual Modules declare the signals they are capable of receiving and producing while remaining responsible for their own internal behavior.

**MIOS understands the rules of connection. Modules understand the work they perform.**

## Questions of Architecture
**(The following questions guide the development of MIOS architecture. Their answers remain subject to revision as the responsibilities and relationships of the system become better understood.)**

- What is the MIOS Core?
The MIOS core is reliant on the Modules and how they communicate with each other in order to create a signal flow that can allow the musician to be truly expressive in their muscial ideas
- What is a Module?
A module is a unit within MIOS that can be strung together in order to facilitate a complete Camino. Modules that are grouped together are known as Juntas. Modules have independent responsibilities that when combined can create new and unique sounds/improvised compositions.
- What is an Engine?
An engine is a unit that must process information/data in order for it to be received by another Module. Consider UI engine, Audio engine, Synth engine, FX engine.
- What is a Camino?
A Camino is a user-defined signal path that carries musical information through MIOS.
- What is a Junta?
A Junta is a user-defined collection of related modules that together perform a single musical role.
- What systems own Audio, MIDI, and Control?
The DSP system is in charge of Audio generation and processing, the Routing system is in charge of MIDI and whether it is outputting to the audio generation, or outputting expression/CC commands.
- Who creates connections?
The Graph is in charge of facilitating all connections be they Audio, MIDI, Control, ETC.
- Who validates connections?
The Modules will define what inputs and outputs are designated in order to make all connections clean and satisfactory.
- Who executes the graph?
The Control Layer will implement the graph so that all connections are true and can communicate effectively.
- Who stores the state of the instrument?
The Session Layer will dedicate memory to recalling presets both upon bootup and upon encoder recall.
- Who communicates with hardware?
The modules/systems in place communicate with the hardware, the user should not have to interact with the hardware settings unless they decide to.
- Who communicates with the musician? 
The Unit is constantly reacting and adapting to what the musican is inputting both musically, as well as technically.

## Fundamental Architectural Objects

### Connection

A Connection defines the relationship between the Output of one Module and the Input of another.

Modules declare the types of Signals they are capable of receiving and producing. The MIOS Core understands these declarations and uses them to determine whether a requested Connection is valid.

A Connection does not determine the behavior of the Modules it joins. It only defines the path through which compatible Signals may travel between them.

**Modules declare their capabilities. Connections define their relationships. The MIOS Core enforces the rules between them.**

### Engine

An Engine is a specialized execution system responsible for performing work that requires continuous, coordinated, or time-sensitive processing.

While Modules define individual musical responsibilities, Engines provide the execution environments necessary for those responsibilities to be performed.

Multiple Modules may rely on the same Engine while remaining independent of one another.

Engines do not define the structure of the instrument. The Graph defines that structure, the MIOS Core governs it, and Engines execute the specialized work required to make it functional.

Engines execute time-sensitive behavior. Systems manage broader responsibilities. Modules define individual musical functions.

**Modules define musical behavior. Engines provide the systems that execute it.**

### Graph

The Graph is the complete structural representation of the Modules and Connections that define the current state of the instrument.

While individual Modules perform work and Connections establish relationships between them, the Graph represents these elements as a complete system.

The Graph does not determine the internal behavior of individual Modules. It defines how those Modules are organized and related throughout the instrument.

**Modules perform individually. Connections establish relationships. The Graph represents the instrument as a whole.**

### MIOS Core

The MIOS Core is the central governing system responsible for maintaining the integrity and coordination of the instrument.

The Core understands the fundamental architectural objects within MIOS and the rules that determine how they may participate in the instrument.

It validates Modules and Connections, maintains the coherence of the Graph, and coordinates the systems responsible for executing its structure.

The MIOS Core does not perform the specialized musical work of individual Modules or directly process every Signal traveling through the instrument. Instead, it ensures that the systems performing this work remain organized within a valid and coherent structure.

**The Core governs the instrument. The systems within it perform the work.**

### Module

A Module is an independent functional unit within MIOS that performs one defined musical responsibility and declares the signals it is capable of receiving and producing.

Modules remain responsible for their own internal behavior while the MIOS Core remains responsible for validating how Modules may connect.

**A Module understands the work it performs. The MIOS core understands how that Module may participate in the instrument.**

### Signal

Before there is MIOS, there is Signal.

A Signal is a representation of musical information that can be received, produced, transformed, and transmitted throughout the instrument.

Signals allow Modules to communicate while remaining independent of one another. A Module does not need to understand the internal behavior of another Module. It only needs to understand the types of Signals it can receive and produce.

Within MIOS, Signals may represent Audio, MIDI, or Control information.

**Signals carry information. Modules determine what that information becomes.**

### System

A System is responsible for managing a broader operational responsibility required for MIOS to function as a complete instrument.

Unlike Modules, Systems do not define individual musical behaviors. Unlike Engines, Systems do not exist primarily to execute time-sensitive processing.

Systems manage responsibilities that support the operation of the instrument, including interaction with the musician, communication with hardware, and the storage and restoration of instrument state.

Multiple Systems may communicate with the MIOS Core, Engines, and other Systems while remaining responsible for their own defined area of operation.

**Modules perform. Engines execute. Systems manage. The Core governs.**