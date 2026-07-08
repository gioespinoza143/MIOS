class Module:
    """Base class for every MIOS Module."""

    def __init__(self, name, inputs, outputs):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs

    def process(self, signal):
        return signal

    def accepts(self, signal):
        return any(
            endpoint.signal_type == signal.signal_type
            for endpoint in self.inputs
        )

    def produces(self, signal):
        return any(
            endpoint.signal_type == signal.signal_type
            for endpoint in self.outputs
        )