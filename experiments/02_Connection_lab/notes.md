Observation 001: A Connection cannot truthfully describe a relationship between Modules alone, because Modules may expose multiple Inputs and Outputs of identical or differing SignalTypes. Therefore, Connections appear to require specific I/O Endpoints. An Endpoint minimally requires an identity and SignalType. Modules own and declare Endpoints; Connections declare relationships between them.

Latest tests have reached this process within MIOS lab experiments
Run this in a fresh Python session from Shared_Objects:

from signal_type import SignalType
from mios_signal import Signal
from endpoint import Endpoint
from module import Module

Then create the Signal:

audio = Signal(
    SignalType.AUDIO,
    "Guitar Data"
)

Create the Amp's endpoints:

audio_in = Endpoint(
    "Audio In",
    SignalType.AUDIO
)

audio_out = Endpoint(
    "Audio Out",
    SignalType.AUDIO
)

Now create the Amp:

amp = Module(
    "Amp",
    inputs=[audio_in],
    outputs=[audio_out]
)

A Connection is responsible only for declaring a relationship between specific Module Endpoints. A Connection may exist as a Python object without representing a valid MIOS relationship. Validity requires confirmation of Endpoint ownership, direction, and SignalType compatibility. These responsibilities require an architectural authority beyond Connection itself.