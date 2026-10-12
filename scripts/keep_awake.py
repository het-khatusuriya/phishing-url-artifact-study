"""Ask Windows not to idle-sleep while experiments run (non-persistent; ends with this process).
Does not override lid-close or battery-saver standby. Usage: python scripts/keep_awake.py"""
import ctypes, time
ES_CONTINUOUS, ES_SYSTEM_REQUIRED = 0x80000000, 0x00000001
while True:
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)
    time.sleep(60)
