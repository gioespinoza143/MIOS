import time
from module import Module
from module_runtime import ModuleRuntime
from process_manager import ProcessManager

test_tone = Module(
    "Test Tone",
    inputs=[],
    outputs=[]
)

test_tone_runtime = ModuleRuntime(
    module=test_tone,
    implementation="/home/patch/MIOS/pd/test_tone.pd"
)

process_manager = ProcessManager()

print(
    "Running before start:",
    process_manager.is_running(test_tone_runtime)
)

process = process_manager.start(test_tone_runtime)


print(
    test_tone.name,
    "started with PID:",
    process.pid
)

print(
    "Running after start:",
    process_manager.is_running(test_tone_runtime)
)

time.sleep(3)

process.terminate()
process.wait()

stopped = process_manager.stop(test_tone_runtime)

print(
    "Running after external termination:",
    process_manager.is_running(test_tone_runtime)
)

print(
    "Tracked processes:",
    len(process_manager.processes)
)
