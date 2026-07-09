class Connection:
	"""Represents a relationship between two module endpoints."""

	def __init__(
		self,
		source_module,
		source_output,
		destination_module,
		destination_input
	):
		self.source_module = source_module
		self.source_output = source_output
		self.destination_module = destination_module
		self.destination_input = destination_input