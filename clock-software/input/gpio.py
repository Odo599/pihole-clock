from .config import *
from .button_manager import ButtonManager

def setup_gpio(buttonManager: ButtonManager):
    press_play   = lambda : buttonManager.press("PLAY")
    press_vdown  = lambda : buttonManager.press("VDOWN")
    press_vup    = lambda : buttonManager.press("VUP")
    press_hour   = lambda : buttonManager.press("HOUR")
    press_minute = lambda : buttonManager.press("MINUTE")
    press_alarm1 = lambda : buttonManager.press("ALARM1")
    press_alarm2 = lambda : buttonManager.press("ALARM2")
    release_play   = lambda : buttonManager.release("PLAY")
    release_vdown  = lambda : buttonManager.release("VDOWN")
    release_vup    = lambda : buttonManager.release("VUP")
    release_hour   = lambda : buttonManager.release("HOUR")
    release_minute = lambda : buttonManager.release("MINUTE")
    release_alarm1 = lambda : buttonManager.release("ALARM1")
    release_alarm2 = lambda : buttonManager.release("ALARM2")

    PLAY_BUTTON.when_activated = press_play
    VDOWN_BUTTON.when_activated = press_vdown
    VUP_BUTTON.when_activated = press_vup
    HOUR_BUTTON.when_activated = press_hour
    MINUTE_BUTTON.when_activated = press_minute
    ALARM1_BUTTON.when_activated = press_alarm1
    ALARM2_BUTTON.when_activated = press_alarm2

    PLAY_BUTTON.when_deactivated = release_play
    VDOWN_BUTTON.when_deactivated = release_vdown
    VUP_BUTTON.when_deactivated = release_vup
    HOUR_BUTTON.when_deactivated = release_hour
    MINUTE_BUTTON.when_deactivated = release_minute
    ALARM1_BUTTON.when_deactivated = release_alarm1
    ALARM2_BUTTON.when_deactivated = release_alarm2

