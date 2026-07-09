class Comandante:
    """Translates MIOS Commands into a Camino realization plan for backend instructions."""

    def issue_commands(self, plan):
        commands = []

        for runtime in plan["modules"]:
            commands.append(
                {
                    "command": "create",
                    "module": runtime.module,
                    "runtime": runtime
                }
            )

        for connection in plan["connections"]:
            commands.append(
                {
                    "command": "connect",

                    "source_module": connection.source_module,
                    "source_endpoint": connection.source_output,
                    "destination_module": connection.destination_module,
                    "destination_endpoint": connection.destination_input
                }
            )

        return commands