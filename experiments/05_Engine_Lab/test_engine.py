from signal_type import SignalType
from mios_signal import Signal
from endpoint import Endpoint
from module import Module
from connection import Connection
from mios_core import MIOSCore
from graph import Graph
from engine import Engine

amp_audio_in = Endpoint(
    "Audio In",
    SignalType.AUDIO
)

amp_audio_out = Endpoint(
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

delay_time = Endpoint(
    "Delay Time",
    SignalType.CONTROL
)

amp = Module(
    "Amp",
    inputs=[amp_audio_in],
    outputs=[amp_audio_out]
)

delay = Module(
    "Delay",
    inputs=[delay_audio_in, delay_time],
    outputs=[delay_audio_out]
)

good_connection = Connection(
    source_module=amp,
    source_output=amp_audio_out,
    destination_module=delay,
    destination_input=delay_audio_in
)


core = MIOSCore()
graph = Graph(core)

graph.add_module(amp)
graph.add_module(delay)

graph.add_connection(good_connection)

engine = Engine(graph)

execution_order = engine.get_execution_order()

for module in execution_order:
	print(module.name)