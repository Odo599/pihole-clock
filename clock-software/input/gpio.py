from .config import *
from .virtual import ButtonManager

def setup_gpio(buttonManager: ButtonManager):
    press_play   = lambda : buttonManager.press("PLAY")
    press_vdown  = lambda : buttonManager.press("VDOWN")
    press_vup    = lambda : buttonManager.press("VUP")
    press_hour   = lambda : buttonManager.press("HOUR")
    press_minute = lambda : buttonManager.press("MINUTE")
    press_alarm1 = lambda : buttonManager.press("ALARM1")
    press_alarm2 = lambda : buttonManager.press("ALARM2")

    PLAY_BUTTON.when_activated = press_play
    VDOWN_BUTTON.when_activated = press_vdown
    VUP_BUTTON.when_activated = press_vup
    HOUR_BUTTON.when_activated = press_hour
    MINUTE_BUTTON.when_activated = press_minute
    ALARM1_BUTTON.when_activated = press_alarm1
    ALARM2_BUTTON.when_activated = press_alarm2

