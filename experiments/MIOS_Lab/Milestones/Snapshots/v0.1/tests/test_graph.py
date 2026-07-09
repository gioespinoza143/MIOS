from signal_type import SignalType
from mios_signal import Signal
from endpoint import Endpoint
from module import Module
from connection import Connection
from mios_core import MIOSCore
from graph import Graph

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

false_connection = Connection(
    source_module=amp,
    source_output=delay_audio_out,
    destination_module=delay,
    destination_input=delay_audio_in
)

wrong_type_connection = Connection(
    source_module=amp,
    source_output=amp_audio_out,
    destination_module=delay,
    destination_input=delay_time
)

core = MIOSCore()
graph = Graph(core)

print("TEST 1: Connection before Modules enter Graph")

print(graph.add_connection(good_connection))
print(len(graph.connections))

print("TEST 2: Add Modules")
print(graph.add_module(amp))
print(graph.add_module(delay))
print(len(graph.modules))

print("TEST 3: Valid connection after modules enter Graph")
print(graph.add_connection(good_connection))
print(len(graph.connections))

print("TEST 4: False ownership")
print(graph.add_connection(false_connection))
print(len(graph.connections))

print("TEST 5: Wrong SignalType")
print(graph.add_connection(wrong_type_connection))
print(len(graph.connections))

print(graph.add_connection(good_connection))
print(len(graph.connections))

print(graph.add_connection(false_connection))
print(len(graph.connections))

print(graph.add_connection(wrong_type_connection))
print(len(graph.connections))