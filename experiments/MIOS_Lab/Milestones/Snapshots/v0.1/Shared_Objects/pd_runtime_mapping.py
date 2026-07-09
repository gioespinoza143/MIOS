class PDRuntimeMapping:
    """Maps MIOS endpoints to Pure Data inlet and outlet indices."""

    def __init__(
        self,
        runtime,
        input_ports,
        output_ports
    ):
        self.runtime = runtime
        self.input_ports = input_ports
        self.output_ports = output_ports

    def get_input_port(self, endpoint):
        return self.input_ports.get(endpoint)

    def get_output_port(self, endpoint):
        return self.output_ports.get(endpoint)