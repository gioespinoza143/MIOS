from endpoint import Endpoint
from module import Module
from mios_signal import SignalType
from module_runtime import ModuleRuntime

from pd_runtime_mapping import PDRuntimeMapping
from pd_runtime_registry import PDRuntimeRegistry


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
unknown_module = Module(
    "Unknown",
    inputs=[],
    outputs=[]
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
# CREATE PD RUNTIME REGISTRY
# ============================================================

registry = PDRuntimeRegistry()


# ============================================================
# REGISTER PD RUNTIME MAPPING
# ============================================================

registry.register(gain_mapping)


# ============================================================
# RETRIEVE PD RUNTIME MAPPING
# ============================================================

retrieved_mapping = registry.get(gain)


# ============================================================
# VERIFY RETRIEVAL
# ============================================================

print(
    "Mapping retrieved:",
    retrieved_mapping is gain_mapping
)

print(
    "Retrieved runtime:",
    retrieved_mapping.runtime.module.name
)

print(
    "Gain Audio In PD port:",
    retrieved_mapping.get_input_port(gain_audio_in)
)

print(
    "Gain Audio Out PD port:",
    retrieved_mapping.get_output_port(gain_audio_out)
)

unknown_runtime = ModuleRuntime(
    module=gain,
    implementation="/fake/path.pd"
)

print(
    "Unknown runtime mapping:",
    registry.get(unknown_runtime)
)

print(
    "Unknown module mapping:",
    registry.get(unknown_module)
)