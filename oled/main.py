import time
import logging

import display
import display.preview as preview
import input
import libs

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("started main.py")

state = libs.AlarmState()

fb = display.init_display()
buttons = input.init_buttons()

# ui testing
def draw_ui(draw):
    libs.draw_time(draw)
    libs.draw_alarm_bells(draw,state)
fb.draw(draw_ui)
preview.save_frame(fb)

# button testing
libs.startHoldAlarm1(buttons)
libs.pressHour(buttons)
libs.pressMinute(buttons)

p = buttons.poll()
libs.check_alarms(p, state)

libs.endHoldAlarm1(buttons)
