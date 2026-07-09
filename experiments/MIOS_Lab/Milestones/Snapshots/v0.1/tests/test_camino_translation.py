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

from camino_planner import CaminoPlanner
from camino_translator import CaminoTranslator

# ============================================================
# CREATE ENDPOINTS
# ============================================================

audio_input_out = Endpoint(
    "Audio Out",
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

audio_output = Module(
    "Audio Output",
    inputs=[audio_output_in],
    outputs=[]
)


# ============================================================
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

# ============================================================
# CREATE CORE AND GRAPH
# ============================================================

core = MIOSCore()
graph = Graph(core)


# ============================================================
# ADD MODULES
# ============================================================

graph.add_module(audio_input)
graph.add_module(gain)
graph.add_module(delay)
graph.add_module(audio_output)


# ============================================================
# ADD CONNECTIONS
# ============================================================

graph.add_connection(input_to_gain)
graph.add_connection(gain_to_delay)
graph.add_connection(delay_to_output)


# ============================================================
# CREATE ENGINE
# ============================================================

engine = Engine(graph)

execution_order = engine.get_execution_order()

# ============================================================
# DISPLAY EXECUTION ORDER
# ============================================================

print("\nGRAPH EXECUTION ORDER:")

for module in execution_order:
    print(module.name)

# ============================================================
# CREATE MODULE RUNTIMES
# ============================================================

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

# ============================================================
# CREATE RUNTIME REGISTRY
# ============================================================

registry = RuntimeRegistry()


# ============================================================
# REGISTER MODULE RUNTIMES
# ============================================================

registry.register(audio_input_runtime)
registry.register(gain_runtime)
registry.register(delay_runtime)
registry.register(audio_output_runtime)


# ============================================================
# CREATE RUNTIME RESOLVER
# ============================================================

resolver = RuntimeResolver(registry)


# ============================================================
# RESOLVE EXECUTION ORDER
# ============================================================

resolved_runtimes = resolver.resolve(execution_order)

# ============================================================
# CREATE CAMINO PLANNER
# ============================================================

planner = CaminoPlanner()

# ============================================================
# CREATE REALIZATION PLAN
# ============================================================

plan = planner.create_plan(
    camino=graph,
    runtimes=resolved_runtimes
)

# ============================================================
# CREATE CAMINO TRANSLATOR
# ============================================================

translator = CaminoTranslator()

instructions = translator.translate(plan)

# ============================================================
# DISPLAY BACKEND INSTRUCTIONS
# ============================================================

print("\nMIOS BACKEND INSTRUCTIONS:")

for instruction in instructions:

    if instruction["operation"] == "create":
        print(
            "CREATE",
            instruction["module"].name,
            "USING",
            instruction["runtime"].implementation
        )

    elif instruction["operation"] == "connect":
        print(
            "CONNECT",
            instruction["source"].name,
            "TO",
            instruction["destination"].name
        )