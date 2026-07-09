from signal_type import SignalType


class Signal:
	"""Base class for every MIOS Signal."""
	def __init__(self, signal_type, data):
		self.signal_type = signal_type
		self.data = data