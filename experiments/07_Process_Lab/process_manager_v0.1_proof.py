import subprocess

class ProcessManager:
    """Starts and stops executable Module implementations."""

    def __init__(self):
        self.processes = {}

    def start(self, runtime):
        process = subprocess.Popen([
            "pd",
            runtime.implementation
        ])

        self.processes[runtime.module] = process

        return process

    def is_running(self, runtime):
        process = self.processes.get(runtime.module)

        if process is None:
            return False

        if process.poll() is not None:
            del self.processes[runtime.module]
            return False

        return True

    def stop(self, runtime):
        process = self.processes.get(runtime.module)

        if process is None:
            return False

        process.terminate()
        process.wait()

        del self.processes[runtime.module]

        return True