class CaminoRuntime:
    """Associates a Camino with its runtime implementation."""

    def __init__(self, camino, implementation):
        self.camino = camino
        self.implementation = implementation