class Endpoint:
	"""A specific place where a Module receives or produces a SignalType."""
	
	def __init__(self, name, signal_type):
		self.name = name
		self.signal_type = signal_type
