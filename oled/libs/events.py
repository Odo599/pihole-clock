import logging
import datetime as dt

from .state import AlarmState
from .time_funcs import add_time

logger = logging.getLogger(__name__)
logger.debug("loaded")

def print_events(buttons):
    for event in buttons.poll():
        print(event.name, event.type)

def check_alarms(poll, state: AlarmState):
    logger.debug("checking alarm events")
    held1 = False
    held2 = False
    pressed1 = False
    pressed2 = False
    released1 = False
    released2 = False
    hour_pressed = False
    minute_pressed = False
    for event in poll:
        if event.name in ["ALARM1","ALARM2"]:
            if event.type == "HOLD":
                if event.name == "ALARM1":
                    held1 = True
                else:
                    held2 = True
            elif event.type == "PRESS":
                if event.name == "ALARM1":
                    pressed1 = True
                else:
                    pressed2 = True
            elif event.type == "RELEASE":
                if event.name == "ALARM1":
                    released1 = True
                else:
                    released2 = True
        elif event.name == "HOUR" and event.type == "PRESS":
            hour_pressed = True
        elif event.name == "MINUTE" and event.type == "PRESS":
            minute_pressed = True


    if held1 and held2:
        logger.info("Both alarm buttons held, exiting")
        return

    if held1:
        logger.info("Alarm 1 button held, setting to editing state")
        state.editing_alarm_1 = True
        state.editing_alarm_2 = False
        if hour_pressed and minute_pressed:
            logger.info("Minute and hour pressed, resetting alarm 1 to midnight")
            state.alarm1 = dt.time()
        elif hour_pressed:
            state.alarm1 = add_time(state.alarm1,dt.timedelta(hours=1))
            logger.info(f"Adding hour to Alarm 1, new time {state.alarm1}")
        elif minute_pressed:
            state.alarm1 = add_time(state.alarm1,dt.timedelta(minutes=1))
            logger.info(f"Adding minute to Alarm 1, new time {state.alarm1}")
        return
    elif held2:
        logger.info("Alarm 2 button held, setting to editing state")
        state.editing_alarm_2 = True
        state.editing_alarm_1 = False
        return
    else:
        state.editing_alarm_1 = False
        state.editing_alarm_2 = False

    if pressed1 and released1:
        logger.info(f"Alarm 1 pressed and released, set to {not state.alarm1_enabled}")
        state.alarm1_enabled = not state.alarm1_enabled

    if pressed2 and released2:
        logger.info(f"Alarm 2 pressed and released, set to {not state.alarm2_enabled}")
        state.alarm2_enabled = not state.alarm2_enabled


