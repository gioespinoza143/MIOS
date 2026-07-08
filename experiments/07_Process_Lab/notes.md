OBSERVATIONS
============

The ProcessManager successfully started and stopped the Pure Data
implementation.

The implementation was assigned a process ID, remained active while
MIOS continued execution, and was successfully terminated by MIOS.

Two additional behaviors were observed:

1. Runtime Startup Delay

The five-second process lifetime did not produce five full seconds of
audio.

Pure Data required time to initialize, load the patch, initialize the
audio system, and begin DSP processing.

This demonstrated that process startup does not immediately imply that
a Module implementation is ready to perform musical work.

A distinction has emerged between:

PROCESS STARTED

and

MODULE READY


2. Abrupt Runtime Shutdown

When ProcessManager terminated the Pure Data process, an audible
artifact or pitch-like change occurred.

The implementation was stopped at the process level without first
performing a controlled musical shutdown.

This demonstrated that terminating a process does not necessarily
provide a clean shutdown of musical behavior.

A distinction has emerged between:

PROCESS TERMINATION

and

MODULE SHUTDOWN


EXPERIMENT RESULT

ProcessManager successfully demonstrated the first MIOS implementation
lifecycle:

RESOLVE
→ START
→ RUN
→ STOP

The experiment also exposed future architectural questions concerning
runtime readiness and graceful musical shutdown.

3. Observed Limitation: Abrupt termination of the Pure Data process produces repeated pdsend broken-pipe errors. ProcessManager correctly detects process death and removes stale internal records, but operating-system process termination does not guarantee clean shutdown of runtime communication resources. Graceful runtime shutdown remains a future responsibility.

### Experiment result
During external process termination testing, repeated pdsend errors were observed, suggesting that abrupt termination may leave runtime communication or cleanup behavior in an undesirable state.

first Test

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

time.sleep(5)

stopped = process_manager.stop(test_tone_runtime)

print(
    test_tone.name,
    "stopped:",
    stopped
)

print(
    "Running after stop:",
    process_manager.is_running(test_tone_runtime)
)

stopped_again = process_manager.stop(test_tone_runtime)

print(
    test_tone.name,
    "stopped again:",
    stopped_again
)

