from pathlib import Path

from endpoint import Endpoint
from module import Module
from mios_signal import SignalType
from module_runtime import ModuleRuntime

from pd_runtime_mapping import PDRuntimeMapping
from pd_runtime_registry import PDRuntimeRegistry
from pd_realizer import PDRealizer


# ============================================================
# CREATE SOURCE ENDPOINTS
# ============================================================

source_out_0 = Endpoint(
    "Output 0",
    SignalType.AUDIO
)

source_out_1 = Endpoint(
    "Output 1",
    SignalType.AUDIO
)


# ============================================================
# CREATE DESTINATION ENDPOINTS
# ============================================================

destination_in_0 = Endpoint(
    "Input 0",
    SignalType.AUDIO
)

destination_in_1 = Endpoint(
    "Input 1",
    SignalType.AUDIO
)

destination_in_2 = Endpoint(
    "Input 2",
    SignalType.AUDIO
)


# ============================================================
# CREATE MODULES
# ============================================================

source_module = Module(
    "Multi Output Source",
    inputs=[],
    outputs=[
        source_out_0,
        source_out_1
    ]
)

destination_module = Module(
    "Multi Input Destination",
    inputs=[
        destination_in_0,
        destination_in_1,
        destination_in_2
    ],
    outputs=[]
)


# ============================================================
# CREATE MODULE RUNTIMES
# ============================================================

source_runtime = ModuleRuntime(
    module=source_module,
    implementation="/fake/source.pd"
)

destination_runtime = ModuleRuntime(
    module=destination_module,
    implementation="/fake/destination.pd"
)


# ============================================================
# CREATE PD RUNTIME MAPPINGS
# ============================================================

source_mapping = PDRuntimeMapping(
    runtime=source_runtime,
    input_ports={},
    output_ports={
        source_out_0: 0,
        source_out_1: 1
    }
)

destination_mapping = PDRuntimeMapping(
    runtime=destination_runtime,
    input_ports={
        destination_in_0: 0,
        destination_in_1: 1,
        destination_in_2: 2
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

pd_runtime_registry.register(source_mapping)
pd_runtime_registry.register(destination_mapping)


# ============================================================
# CREATE MIOS COMMANDS
# ============================================================

commands = [
    {
        "command": "create",
        "module": source_module,
        "runtime": source_runtime
    },

    {
        "command": "create",
        "module": destination_module,
        "runtime": destination_runtime
    },

    {
        "command": "connect",
        "source_module": source_module,
        "source_endpoint": source_out_1,
        "destination_module": destination_module,
        "destination_endpoint": destination_in_2
    }
]


# ============================================================
# VERIFY MAPPINGS
# ============================================================

print("\nPD MULTIPORT MAPPINGS:")

print(
    "Source Output 1 PD port:",
    pd_runtime_registry
    .get(source_module)
    .get_output_port(source_out_1)
)

print(
    "Destination Input 2 PD port:",
    pd_runtime_registry
    .get(destination_module)
    .get_input_port(destination_in_2)
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

generated_patch = Path(
    "/home/patch/MIOS/pd/caminos/generated_multiport_test.pd"
)


# ============================================================
# REALIZE MIOS COMMANDS
# ============================================================

result = pd_realizer.realize(
    commands=commands,
    output_path=generated_patch
)


# ============================================================
# VERIFY GENERATED PATCH
# ============================================================

print("\nPD MULTIPORT REALIZATION COMPLETE:")

print(
    "Generated patch exists:",
    result.exists()
)

print(
    "Generated patch:",
    result
)


# ============================================================
# DISPLAY GENERATED PD PATCH
# ============================================================

print("\nGENERATED PD PATCH:")

print(result.read_text())