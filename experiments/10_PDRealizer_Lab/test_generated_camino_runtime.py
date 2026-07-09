from pathlib import Path

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
from comandante import Comandante

from pd_runtime_mapping import PDRuntimeMapping
from pd_runtime_registry import PDRuntimeRegistry
from pd_realizer import PDRealizer

from camino_runtime import CaminoRuntime
from process_manager import ProcessManager


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


# ============================================================
# GET EXECUTION ORDER
# ============================================================

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
# CREATE MIOS RUNTIME REGISTRY
# ============================================================

runtime_registry = RuntimeRegistry()


# ============================================================
# REGISTER MODULE RUNTIMES
# ============================================================

runtime_registry.register(audio_input_runtime)
runtime_registry.register(gain_runtime)
runtime_registry.register(delay_runtime)
runtime_registry.register(audio_output_runtime)


# ============================================================
# CREATE RUNTIME RESOLVER
# ============================================================

resolver = RuntimeResolver(runtime_registry)


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
# CREATE COMANDANTE
# ============================================================

comandante = Comandante()


# ============================================================
# ISSUE MIOS COMMANDS
# ============================================================

commands = comandante.issue_commands(plan)


# ============================================================
# DISPLAY MIOS COMMANDS
# ============================================================

print("\nMIOS COMMANDS:")

for command in commands:

    if command["command"] == "create":
        print(
            "CREATE",
            command["module"].name,
            "USING",
            command["runtime"].implementation
        )

    elif command["command"] == "connect":
        print(
            "CONNECT",
            command["source_module"].name,
            ".",
            command["source_endpoint"].name,
            "TO",
            command["destination_module"].name,
            ".",
            command["destination_endpoint"].name
        )


# ============================================================
# CREATE PD RUNTIME MAPPINGS
# ============================================================

audio_input_mapping = PDRuntimeMapping(
    runtime=audio_input_runtime,
    input_ports={},
    output_ports={
        audio_input_out: 0
    }
)

gain_mapping = PDRuntimeMapping(
    runtime=gain_runtime,
    input_ports={
        gain_audio_in: 0
    },
    output_ports={
        gain_audio_out: 0
    }
)

delay_mapping = PDRuntimeMapping(
    runtime=delay_runtime,
    input_ports={
        delay_audio_in: 0
    },
    output_ports={
        delay_audio_out: 0
    }
)

audio_output_mapping = PDRuntimeMapping(
    runtime=audio_output_runtime,
    input_ports={
        audio_output_in: 0
    },
    output_ports={}
)


# ============================================================
# CREATE PD RUNTIME REGISTRY
# ============================================================

pd_runtime_registry = PDRuntimeRegistry()


# ============================================================
# REGISTER PD RUNTIME MAPPINGS
# ============================================================

pd_runtime_registry.register(audio_input_mapping)
pd_runtime_registry.register(gain_mapping)
pd_runtime_registry.register(delay_mapping)
pd_runtime_registry.register(audio_output_mapping)


# ============================================================
# DISPLAY PD RUNTIME MAPPINGS
# ============================================================

print("\nPD RUNTIME MAPPINGS:")

print(
    "Audio Input Audio Out:",
    pd_runtime_registry
    .get(audio_input)
    .get_output_port(audio_input_out)
)

print(
    "Gain Audio In:",
    pd_runtime_registry
    .get(gain)
    .get_input_port(gain_audio_in)
)

print(
    "Gain Audio Out:",
    pd_runtime_registry
    .get(gain)
    .get_output_port(gain_audio_out)
)

print(
    "Delay Audio In:",
    pd_runtime_registry
    .get(delay)
    .get_input_port(delay_audio_in)
)

print(
    "Delay Audio Out:",
    pd_runtime_registry
    .get(delay)
    .get_output_port(delay_audio_out)
)

print(
    "Audio Output Audio In:",
    pd_runtime_registry
    .get(audio_output)
    .get_input_port(audio_output_in)
)


# ============================================================
# CREATE PD REALIZER
# ============================================================

pd_realizer = PDRealizer(
    runtime_registry=pd_runtime_registry
)


# ============================================================
# DEFINE GENERATED PATCH PATH
# ============================================================

generated_patch_path = Path(
    "/home/patch/MIOS/pd/caminos/generated_camino.pd"
)


# ============================================================
# REALIZE MIOS COMMANDS
# ============================================================

generated_patch = pd_realizer.realize(
    commands=commands,
    output_path=generated_patch_path
)


# ============================================================
# VERIFY GENERATED CAMINO
# ============================================================

print("\nGENERATED CAMINO:")

print(
    "Generated patch exists:",
    generated_patch.exists()
)

print(
    "Generated patch:",
    generated_patch
)

print("\nGENERATED PD PATCH:")

print(generated_patch.read_text())


# ============================================================
# CREATE CAMINO RUNTIME
# ============================================================

camino_runtime = CaminoRuntime(
    camino=graph,
    runtimes=resolved_runtimes,
    implementation=str(generated_patch)
)


# ============================================================
# VERIFY CAMINO RUNTIME
# ============================================================

print("\nGENERATED CAMINO RUNTIME:")

print(
    "Camino implementation exists:",
    Path(camino_runtime.implementation).exists()
)

print(
    "Camino implementation:",
    camino_runtime.implementation
)


# ============================================================
# CREATE PROCESS MANAGER
# ============================================================

process_manager = ProcessManager()


# ============================================================
# VERIFY INITIAL RUNNING STATE
# ============================================================

print(
    "Initial running state:",
    process_manager.is_running(camino_runtime)
)


# ============================================================
# START GENERATED CAMINO
# ============================================================

print("\nSTARTING MIOS-GENERATED CAMINO...")

process_manager.start(camino_runtime)


# ============================================================
# VERIFY RUNNING STATE
# ============================================================

print(
    "Camino running after start:",
    process_manager.is_running(camino_runtime)
)


# ============================================================
# PHYSICAL AUDIO TEST
# ============================================================

input(
    "\nPLAY YOUR INSTRUMENT NOW.\n"
    "Press Enter to stop the MIOS-generated Camino..."
)


# ============================================================
# STOP GENERATED CAMINO
# ============================================================

print("\nSTOPPING MIOS-GENERATED CAMINO...")

process_manager.stop(camino_runtime)


# ============================================================
# VERIFY STOPPED STATE
# ============================================================

print(
    "Camino running after stop:",
    process_manager.is_running(camino_runtime)
)