class RuntimeRegistry:
    """Registers and resolves ModuleRuntime objects."""

    def __init__(self):
        self.runtime = []

    def register(self, runtime):
        self.runtime.append(runtime)

    def resolve(self, module):
        for runtime in self.runtime:
            if runtime.module == module:
                return runtime

        return None