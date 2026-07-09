The Runtime Lab taught MIOS how to give a Module a body.
The Process Lab teaches MIOS how to keep track of whether that body is alive.

The unresolved question is:

Who is responsible for turning a resolved implementation into a living process—and managing that process afterward?

Right now, test_runtime.py does this:

subprocess.run([
    "pd",
    test_tone_runtime.implementation
])

It works. Module Zero speaks.

But architecturally, test_runtime.py is doing a job that clearly needs a home.

That is how the Process_Manager was created.

Module
→ WHAT exists

Graph
→ WHAT belongs to the instrument

Engine
→ WHEN work occurs

ModuleRuntime
→ HOW a Module is implemented

RuntimeRegistry
→ WHERE that implementation is found

ProcessManager
→ STARTS and STOPS the implementation

07_Process_Lab
        ↓
ProcessManager
        ↓
start(ModuleRuntime)
        ↓
subprocess.Popen()
        ↓
living PD process
        ↓
PID returned
        ↓
SOUND