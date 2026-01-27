from .config import USE_HARDWARE

if USE_HARDWARE:
    from .gpio import ButtonManager
else:
    from .virtual import ButtonManager