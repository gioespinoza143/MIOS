# Principle I
## The Musician Thinks Musically
Technology has become an essential part of modern musical performance.

Audio interfaces, MIDI controllers, computers, plugins, routing software, and digital processors allow musicians to create sounds that were once unimaginable.
Yet every additional layer of technology introduces another language the musician must learn.

Drivers.

Buffers.

Ports.

MIDI channels.

Parameter IDs.

These concepts are necessary for computers.

They are not necessary for making music.

MIOS begins with the belief that musicians should think in musical ideas rather than technical implementation.

A guitarist should think:

"I want my picking dynamics to open the filter."

—not—

"I need to map CC74 to Parameter 18."

The responsibility of MIOS is to translate musical intention into technical implementation.

Never the other way around.

Every interface, every workflow, and every architectural decision should ask one question:

Does this allow the musician to continue thinking musically?

If the answer is no, the design should be reconsidered.

# Principle II
## Technology Is An Implementation
Ideas are allowed to evolve. Principles provide direction. Decisions create momentum. Evidence earns revision.

Pure Data is not MIOS.

Python is not MIOS.

Raspberry Pi is not MIOS.

Pisound is not MIOS.

These technologies are today's implementation of a larger idea.

The philosophy of MIOS should outlive every technology used to build it.

# Principle III
## One Responsibility Per Layer
Every layer and every module within MIOS exists for one reason: to perform a single responsibility well.

Systems with clear tasks/responsibilities are easier to understand, easier to expand, and easier to trust.

When responsibilities become blurred, complexity follows.

MIOS prefers many simple systems working together over one system attempting to do everything.

# Principle IV
## Every Signal Is Musical
No musical signal is considered more important than another. Every signal has the ability to be independent of one another and create musical ideas. They can also be used in sequence for the same purpose.

# Principle V
## Relationships Over Assignments
Musicians think in relationships, not parameter assignments.
A musician does not think about MIDI CC numbers, parameter IDs, or internal data structures. They think about expressive relationships:
Therefore, MIOS expresses connections as musical relationships rather than technical assignments.

# Principle VI
## Complexity Should Grow With The Musician
Depth should be available, never mandatory.

# Principle VII
## The Instrument Adapts To The Musician
Once the User has created their intended presets, they should feel like the instrument is actively participating in the perfomance just as much as the musician is. It might feel like the instrument is almost reading your thoughts or meeting you in the middle before you get there.