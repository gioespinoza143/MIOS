from pathlib import Path


class PDRealizer:
    """Realizes MIOS commands as a Pure Data patch."""

    def __init__(self, runtime_registry):
        self.runtime_registry = runtime_registry


    def realize(self, commands, output_path):
        output_path = Path(output_path)

        patch_lines = [
            "#N canvas 100 100 800 600 10;"
        ]

        module_indices = {}

        self._create_modules(
            commands,
            patch_lines,
            module_indices
        )

        self._create_initialization(
            patch_lines,
            module_indices
        )

        self._create_connections(
            commands,
            patch_lines,
            module_indices
        )

        output_path.write_text(
            "\n".join(patch_lines) + "\n"
        )

        return output_path


    def _create_modules(
        self,
        commands,
        patch_lines,
        module_indices
    ):
        y_position = 100

        for command in commands:

            if command["command"] != "create":
                continue

            module = command["module"]
            runtime = command["runtime"]

            object_name = Path(
                runtime.implementation
            ).stem

            object_index = len(module_indices)

            module_indices[module] = object_index

            patch_lines.append(
                f"#X obj 100 {y_position} {object_name};"
            )

            y_position += 100


    def _create_initialization(
        self,
        patch_lines,
        module_indices
    ):
        loadbang_index = len(module_indices)

        patch_lines.append(
            "#X obj 500 100 loadbang;"
        )

        dsp_message_index = loadbang_index + 1

        patch_lines.append(
            "#X msg 500 150 \\; pd dsp 1;"
        )

        patch_lines.append(
            f"#X connect "
            f"{loadbang_index} 0 "
            f"{dsp_message_index} 0;"
        )


    def _create_connections(
        self,
        commands,
        patch_lines,
        module_indices
    ):
        for command in commands:

            if command["command"] != "connect":
                continue

            source_module = command["source_module"]
            source_endpoint = command["source_endpoint"]

            destination_module = command["destination_module"]
            destination_endpoint = command["destination_endpoint"]

            source_index = module_indices[source_module]

            destination_index = module_indices[
                destination_module
            ]

            source_mapping = self.runtime_registry.get(
                source_module
            )

            destination_mapping = self.runtime_registry.get(
                destination_module
            )

            source_port = source_mapping.get_output_port(
                source_endpoint
            )

            destination_port = destination_mapping.get_input_port(
                destination_endpoint
            )

            patch_lines.append(
                f"#X connect "
                f"{source_index} {source_port} "
                f"{destination_index} {destination_port};"
            )