from pathlib import Path

class ModuleRuntime:
    """Associates a MIOS Module with its executable implementation."""

    def __init__(self, module, implementation):
        self.module = module
        self.implementation = implementation

    def implementation_exists(self):
        return Path(self.implementation).is_file()

    @property
    def identity(self):
        return self.module