class PDRuntimeRegistry:
    """Stores and retrieves Pure Data runtime mappings."""

    def __init__(self):
        self.mappings = {}

    def register(self, mapping):
        self.mappings[mapping.runtime.module] = mapping

    def get(self, module):
        return self.mappings.get(module)