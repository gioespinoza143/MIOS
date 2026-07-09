class RuntimeResolver:
    """Resolves ordered MIOS Modules to usable runtime implementations."""

    def __init__(self, registry):
        self.registry = registry

    def resolve(self, modules):
        resolved_runtimes = []

        for module in modules:
            runtime = self.registry.resolve(module)

            if runtime is None:
                raise ValueError(
                    f"No runtime registered for Module: {module.name}"
                )

            if not runtime.implementation_exists():
                raise ValueError(
                    f"Runtime implementation does not exist for Module: "
                    f"{module.name}"
                )

            resolved_runtimes.append(runtime)

        return resolved_runtimes