import gpiozero

USE_HARDWARE = False

if USE_HARDWARE:
    PLAY_BUTTON = gpiozero.Button(5)
    VDOWN_BUTTON = gpiozero.Button(4)
    VUP_BUTTON = gpiozero.Button(14)
    HOUR_BUTTON = gpiozero.Button(15)
    MINUTE_BUTTON = gpiozero.Button(17)
    ALARM1_BUTTON = gpiozero.Button(22)
    ALARM2_BUTTON = gpiozero.Button(23)