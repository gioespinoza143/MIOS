class CaminoRuntime:
    """Associates a Camino with its resolved runtimes and implementation."""

    def __init__(self, camino, runtimes, implementation):
        self.camino = camino
        self.runtimes = runtimes
        self.implementation = implementation

    @property
    def identity(self):
        return self.camino