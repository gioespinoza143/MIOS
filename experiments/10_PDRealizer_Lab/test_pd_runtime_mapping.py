from endpoint import Endpoint
from module import Module
from mios_signal import SignalType
from module_runtime import ModuleRuntime

from pd_runtime_mapping import PDRuntimeMapping


# ============================================================
# CREATE ENDPOINTS
# ============================================================

gain_audio_in = Endpoint(
    "Audio In",
    SignalType.AUDIO
)

gain_audio_out = Endpoint(
    "Audio Out",
    SignalType.AUDIO
)


# ============================================================
# CREATE MODULE
# ============================================================

gain = Module(
    "Gain",
    inputs=[gain_audio_in],
    outputs=[gain_audio_out]
)


# ============================================================
# CREATE MODULE RUNTIME
# ============================================================

gain_runtime = ModuleRuntime(
    module=gain,
    implementation="/home/patch/MIOS/pd/modules/gain.pd"
)


# ============================================================
# CREATE PD RUNTIME MAPPING
# ============================================================

gain_mapping = PDRuntimeMapping(
    runtime=gain_runtime,
    input_ports={
        gain_audio_in: 0
    },
    output_ports={
        gain_audio_out: 0
    }
)


# ============================================================
# VERIFY RUNTIME
# ============================================================

print(
    "Mapping runtime:",
    gain_mapping.runtime.module.name
)


# ============================================================
# VERIFY INPUT PORT
# ============================================================

print(
    "Gain Audio In PD port:",
    gain_mapping.get_input_port(gain_audio_in)
)


# ============================================================
# VERIFY OUTPUT PORT
# ============================================================

print(
    "Gain Audio Out PD port:",
    gain_mapping.get_output_port(gain_audio_out)
)