from pathlib import Path

from camino_runtime import CaminoRuntime
from pd_launcher import PDLauncher


# ============================================================
# DUMMY CAMINO
# ============================================================

class DummyCamino:
    pass


# ============================================================
# DEFINE PATHS
# ============================================================

modules_path = Path(
    "/home/patch/MIOS/pd/modules"
)

implementation_path = Path(
    "/home/patch/MIOS/pd/caminos/generated_camino.pd"
)


# ============================================================
# CREATE CAMINO RUNTIME
# ============================================================

camino_runtime = CaminoRuntime(
    camino=DummyCamino(),
    runtimes=[],
    implementation=str(implementation_path)
)


# ============================================================
# CREATE PD LAUNCHER
# ============================================================

pd_launcher = PDLauncher(
    modules_path=modules_path
)


# ============================================================
# CREATE LAUNCH COMMAND
# ============================================================

launch_command = pd_launcher.create_launch_command(
    camino_runtime
)


# ============================================================
# DISPLAY RESULTS
# ============================================================

print("\nPD LAUNCHER TEST:")

print(
    "Runtime implementation:",
    camino_runtime.implementation
)

print(
    "PD modules path:",
    pd_launcher.modules_path
)

print("\nGENERATED LAUNCH COMMAND:")

for item in launch_command.command:
    print(item)


# ============================================================
# VERIFY COMMAND CONTENTS
# ============================================================

print("\nCOMMAND VALIDATION:")

print(
    "Executable is PD:",
    launch_command.command[0] == "pd"
)

print(
    "Search path flag exists:",
    "-path" in launch_command.command
)

print(
    "Modules path is correct:",
    str(modules_path) in launch_command.command
)

print(
    "Runtime implementation is correct:",
    str(implementation_path) in launch_command.command
)