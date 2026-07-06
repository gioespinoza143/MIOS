One piece of information to hold onto: A SIGNAL - Represents musical information moving through MIOS.
Signal Types are a deeper implementation of Signal, helping **define** _which_ signals the Module is receiving.
## Conclusions
SignalType provides the shared architectural language of MIOS.

Signals transport musical information.

Modules declare compatibility using SignalTypes.

Modules can describe whether they accept a given Signal.

This contract prepares the architecture for future validation by the MIOS Core.