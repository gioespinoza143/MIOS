from signal_type import SignalType
from mios_signal import MIOSSignal
from endpoint import Endpoint
from module import Module


# ============================================================
# CREATE ENDPOINTS
# ============================================================

audio_input_out = Endpoint(
    "Audio Out",
    SignalType.AUDIO
)

audio_output_in = Endpoint(
    "Audio In",
    SignalType.AUDIO
)


# ============================================================
# CREATE MODULES
# ============================================================

audio_input = Module(
    "Audio Input",
    inputs=[],
    outputs=[audio_input_out]
)

audio_output = Module(
    "Audio Output",
    inputs=[audio_output_in],
    outputs=[]
)


# ============================================================
# CREATE TEST SIGNAL
# ============================================================

audio_signal = MIOSSignal(
    signal_type=SignalType.AUDIO,
    data=None
)


# ============================================================
# TEST MODULE INPUT CAPABILITIES
# ============================================================

print(
    audio_input.name,
    "accepts AUDIO:",
    audio_input.accepts(audio_signal)
)

print(
    audio_output.name,
    "accepts AUDIO:",
    audio_output.accepts(audio_signal)
)