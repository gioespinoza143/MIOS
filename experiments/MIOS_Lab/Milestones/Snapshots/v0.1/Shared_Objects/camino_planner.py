class CaminoPlanner:
    """Builds a realization plan from a Camino and its resolve runtimes."""

    def create_plan(self, camino, runtimes):
        return {
            "modules": runtimes,
            "connections": camino.connections
        }