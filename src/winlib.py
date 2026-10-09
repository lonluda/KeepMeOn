import ctypes

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002


def keep_awake():
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS |
        ES_SYSTEM_REQUIRED |
        ES_DISPLAY_REQUIRED
    )


def restore_normal_behavior():
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS
    )