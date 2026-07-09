class Engine:
    """Interprets a MIOS Graph to determine execution requirements."""

    def __init__(self, graph):
        self.graph = graph

    def get_execution_order(self):
        order = []
        remaining_modules = list(self.graph.modules)

        while remaining_modules:
            module_scheduled = False

            for module in remaining_modules:
                has_unresolved_input = False

                for connection in self.graph.connections:
                    if (
                        connection.destination_module == module
                        and connection.source_module not in order
                    ):
                        has_unresolved_input = True

                if not has_unresolved_input:
                    order.append(module)
                    remaining_modules.remove(module)
                    module_scheduled = True
                    break

            if not module_scheduled:
                raise ValueError(
                    "Graph contains an unresolved dependencies."
                )

        return order
        
