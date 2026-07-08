from signal_type import SignalType
from mios_signal import Signal
from endpoint import Endpoint
from module import Module
from connection import Connection
from mios_core import MIOSCore
from graph import Graph
from engine import Engine

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

# CREATE TEST SIGNAL
# ============================================================

audio_signal = Signal(
    signal_type=SignalType.AUDIO,
    data=None
)



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

print(
    audio_input.name,
    "produces AUDIO:",
    audio_input.produces(audio_signal)
)

print(
    audio_output.name,
    "produces AUDIO:",
    audio_output.produces(audio_signal)
)

print(
    gain.name,
    "accepts AUDIO:",
    gain.accepts(audio_signal)
)

print(
    gain.name,
    "produces AUDIO:",
    gain.produces(audio_signal)
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

# CREATE ENGINE
# ============================================================

engine = Engine(graph)

execution_order = engine.get_execution_order()

# ============================================================
# DISPLAY CAMINO
# ============================================================

print("\nFIRST REAL MIOS CAMINO:")

for module in execution_order:
    print(module.name)