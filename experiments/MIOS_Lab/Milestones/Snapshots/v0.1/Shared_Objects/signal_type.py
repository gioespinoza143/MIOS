from enum import Enum


class SignalType(Enum):
	"""
	The shared language through which architectural objects communicate the kind of Signal being exchanged.
	"""

	AUDIO = "Audio"
	MIDI = "MIDI"
	CONTROL = "Control"