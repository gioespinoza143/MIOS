from pathlib import Path
import time

from process_manager import ProcessManager
from camino_runtime import CaminoRuntime
from camino_planner import CaminoPlanner

from endpoint import Endpoint
from module import Module
from connection import Connection
from mios_core import MIOSCore
from graph import Graph
from engine import Engine
from mios_signal import SignalType

from module_runtime import ModuleRuntime
from runtime_resolver import RuntimeResolver
from runtime_registry import RuntimeRegistry


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
# VERIFY GRAPH TRUTH
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
# DEFINE PROVEN CAMINO IMPLEMENTATION
# ============================================================

camino_patch = Path(
    "/home/patch/MIOS/pd/caminos/first_camino.pd"
)


# ============================================================
# TEST CAMINO IMPLEMENTATION EXISTS
# ============================================================

print(
    "\nCamino implementation exists:",
    camino_patch.exists()
)

print(
    "Camino implementation:",
    camino_patch
)


# ============================================================
# CREATE CAMINO RUNTIME
# ============================================================

camino_runtime = CaminoRuntime(
    camino=graph,
    runtimes=resolved_runtimes,
    implementation=str(camino_patch)
)


# ============================================================
# VERIFY CAMINO RUNTIME GRAPH
# ============================================================

print(
    "\nCamino uses actual Graph:",
    camino_runtime.camino is graph
)


# ============================================================
# VERIFY CAMINO RUNTIME MODULES
# ============================================================

print("\nCAMINO RUNTIME MODULES:")

for runtime in camino_runtime.runtimes:
    print(
        runtime.module.name,
        "->",
        runtime.implementation
    )


# ============================================================
# VERIFY CAMINO IMPLEMENTATION
# ============================================================

print(
    "\nRuntime implementation:",
    camino_runtime.implementation
)

# ============================================================
# CREATE CAMINO PLANNER
# ============================================================

planner = CaminoPlanner()

# ============================================================
# CREATE REALIZATION PLAN
# ============================================================

plan = planner.create_plan(
    camino=camino_runtime.camino,
    runtimes=camino_runtime.runtimes
)

# ============================================================
# DISPLAY CAMINO REALIZATION PLAN
# ============================================================

print("\nMIOS CAMINO REALIZATION PLAN:")

print("\nMODULES:")

for runtime in plan["modules"]:
    print(
        runtime.module.name,
        "->",
        runtime.implementation
    )

print("\nCONNECTIONS:")

for connection in plan["connections"]:
    print(
        connection.source_module.name,
        "->",
        connection.destination_module.name
    )

# ============================================================
# CREATE PROCESS MANAGER
# ============================================================

process_manager = ProcessManager()

print(
    "\nProcessManager created:",
    process_manager is not None
)

print(
    "Initial managed processes:",
    len(process_manager.processes)
)


# ============================================================
# START CAMINO
# ============================================================

process_manager.start(camino_runtime)


# ============================================================
# TEST RUNNING STATE
# ============================================================

print(
    "Camino running after start:",
    process_manager.is_running(camino_runtime)
)


# ============================================================
# ALLOW CAMINO TO RUN
# ============================================================

time.sleep(10)


# ============================================================
# STOP CAMINO
# ============================================================

camino_stopped = process_manager.stop(camino_runtime)

print(
    "Camino stopped:",
    camino_stopped
)


# ============================================================
# TEST FINAL RUNNING STATE
# ============================================================

print(
    "Camino running after stop:",
    process_manager.is_running(camino_runtime)
)