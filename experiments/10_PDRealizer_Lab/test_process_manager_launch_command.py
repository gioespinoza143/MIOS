from pathlib import Path

from camino_runtime import CaminoRuntime
from process_manager import ProcessManager
from launch_command import LaunchCommand


# ============================================================
# DUMMY CAMINO
# ============================================================

class DummyCamino:
    pass


# ============================================================
# CREATE CAMINO RUNTIME
# ============================================================

camino_runtime = CaminoRuntime(
    camino=DummyCamino(),
    runtimes=[],
    implementation="/home/patch/MIOS/pd/caminos/generated_camino.pd"
)


# ============================================================
# CREATE LAUNCH COMMAND
# ============================================================

launch_command = LaunchCommand(
    [
        "pd",
        "-path",
        "/home/patch/MIOS/pd/modules",
        camino_runtime.implementation
    ]
)


# ============================================================
# DISPLAY COMMAND
# ============================================================

print("\nLAUNCH COMMAND:\n")

for item in launch_command.command:
    print(item)


# ============================================================
# CREATE PROCESS MANAGER
# ============================================================

process_manager = ProcessManager()


# ============================================================
# VERIFY INITIAL STATE
# ============================================================

print(
    "\nInitial running state:",
    process_manager.is_running(camino_runtime)
)


# ============================================================
# START PROCESS
# ============================================================

print("\nSTARTING PROCESS...\n")

process_manager.start(
    camino_runtime,
    launch_command
)


# ============================================================
# VERIFY RUNNING
# ============================================================

print(
    "Running after start:",
    process_manager.is_running(camino_runtime)
)


# ============================================================
# PAUSE
# ============================================================

input(
    "\nPress Enter to stop..."
)


# ============================================================
# STOP PROCESS
# ============================================================

print("\nSTOPPING PROCESS...\n")

process_manager.stop(
    camino_runtime
)


# ============================================================
# VERIFY STOPPED
# ============================================================

print(
    "Running after stop:",
    process_manager.is_running(camino_runtime)
)