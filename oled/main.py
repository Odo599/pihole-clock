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

def update_screen():
    fb.draw(draw_ui)
    preview.save_frame(fb)

def check_buttons():
    libs.check_alarms(buttons.poll(), state)

update_screen()

# testing
libs.pressAlarm1(buttons)
check_buttons()
update_screen()

libs.pressAlarm2(buttons)
check_buttons()
update_screen()

libs.startHoldAlarm1(buttons)
check_buttons()
update_screen()

libs.endHoldAlarm1(buttons)
check_buttons()
update_screen()

