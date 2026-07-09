class PDRuntimeRegistry:
    """Stores and retrieves Pure Data runtime mappings."""

    def __init__(self):
        self.mappings = {}

    def register(self, mapping):
        self.mappings[mapping.runtime] = mapping

    def get(self, runtime):
        return self.mappings.get(runtime)