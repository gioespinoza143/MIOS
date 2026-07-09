class Graph:
	"""Represents the Modules and Connections that form a MIOS instrument."""
	
	def __init__(self, core):
		self.core = core
		self.modules = []
		self.connections = []

	def add_module(self, module):
		self.modules.append(module)
		return True

	def add_connection(self, connection):
		source_in_graph = (
			connection.source_module in self.modules
		)

		destination_in_graph = (
			connection.destination_module in self.modules
		)

		connection_is_valid = (
			self.core.validate_connection(connection)
		)
		
		
		if (
			source_in_graph
			and destination_in_graph
			and connection_is_valid
		):
			self.connections.append(connection)
			return True

		return False