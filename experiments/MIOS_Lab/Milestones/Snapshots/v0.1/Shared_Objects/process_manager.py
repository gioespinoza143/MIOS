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

        self.processes[runtime.identity] = process

        return process

    def is_running(self, runtime):
        process = self.processes.get(runtime.identity)

        if process is None:
            return False

        if process.poll() is not None:
            del self.processes[runtime.identity]
            return False

        return True

    def stop(self, runtime):
        process = self.processes.get(runtime.identity)

        if process is None:
            return False

        process.terminate()
        process.wait()

        del self.processes[runtime.identity]

        return True