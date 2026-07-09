from endpoint import Endpoint
from module import Module
from connection import Connection
from mios_core import MIOSCore
from graph import Graph
from engine import Engine
from mios_signal import SignalType

from module_runtime import ModuleRuntime
from runtime_registry import RuntimeRegistry
from runtime_resolver import RuntimeResolver

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

gain_audio_in = Endpoint(
    "Audio In",
    SignalType.AUDIO
)

gain_audio_out = Endpoint(
    "Audio Out",
    SignalType.AUDIO
)

delay_audio_in = Endpoint(
    "Audio In",
    SignalType.AUDIO
)

delay_audio_out = Endpoint(
    "Audio Out",
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

gain = Module(
    "Gain",
    inputs=[gain_audio_in],
    outputs=[gain_audio_out]
)

delay = Module(
    "Delay",
    inputs=[delay_audio_in],
    outputs=[delay_audio_out]
)


# CREATE CONNECTIONS
# ============================================================

input_to_gain = Connection(
    source_module=audio_input,
    source_output=audio_input_out,
    destination_module=gain,
    destination_input=gain_audio_in
)

gain_to_delay = Connection(
    source_module=gain,
    source_output=gain_audio_out,
    destination_module=delay,
    destination_input=delay_audio_in
)

delay_to_output = Connection(
    source_module=delay,
    source_output=delay_audio_out,
    destination_module=audio_output,
    destination_input=audio_output_in
)


# CREATE CORE AND GRAPH
# ============================================================

core = MIOSCore()
graph = Graph(core)


# ADD MODULES
# ============================================================

graph.add_module(audio_input)
graph.add_module(gain)
graph.add_module(audio_output)
graph.add_module(delay)


# ADD CONNECTIONS
# ============================================================

graph.add_connection(input_to_gain)
graph.add_connection(gain_to_delay)
graph.add_connection(delay_to_output)

# VERIFY GRAPH TRUTH

engine = Engine(graph)

execution_order = engine.get_execution_order()

registry = RuntimeRegistry()

audio_input_runtime = ModuleRuntime(
    module=audio_input,
    implementation="/home/patch/MIOS/pd/modules/audio_input.pd"
)

gain_runtime = ModuleRuntime(
    module=gain,
    implementation="/home/patch/MIOS/pd/modules/gain.pd"
)

delay_runtime = ModuleRuntime(
    module=delay,
    implementation="/home/patch/MIOS/pd/modules/delay.pd"
)

audio_output_runtime = ModuleRuntime(
    module=audio_output,
    implementation="/home/patch/MIOS/pd/modules/audio_output.pd"
)



# CREATE RUNTIME REGISTRY

registry = RuntimeRegistry()

# REGISTER MODULE RUNTIMES

registry.register(audio_input_runtime)
registry.register(gain_runtime)
registry.register(delay_runtime)
registry.register(audio_output_runtime)

resolver = RuntimeResolver(registry)
resolved_runtimes = resolver.resolve(execution_order)


print("\nRESOLVED MIOS RUNTIMES:")

for runtime in resolved_runtimes:
    print(
        runtime.module.name,
        "->",
        runtime.implementation
    )
