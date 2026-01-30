from .config import USE_HARDWARE
from .gpio import setup_gpio
from .button_manager import ButtonManager

if USE_HARDWARE:
    setup_gpio(ButtonManager)
