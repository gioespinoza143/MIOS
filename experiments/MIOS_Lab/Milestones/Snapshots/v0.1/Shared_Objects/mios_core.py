class MIOSCore:
	"""Validates architectural relationships within MIOS."""
	
	def validate_connection(self, connection):
		source_owned = (
			connection.source_output
			in connection.source_module.outputs
		)

		destination_owned = (
			connection.destination_input
			in connection.destination_module.inputs
		)

		signal_types_match = (
			connection.source_output.signal_type
			== connection.destination_input.signal_type
		)

		return (
			source_owned
			and destination_owned
			and signal_types_match
		)