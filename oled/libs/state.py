import datetime as dt

import logging

logger = logging.getLogger(__name__)

class AlarmState():
    def __init__(self):
        logger.info("Created new alarmState")
        self.volume = 5
        self.alarm1_enabled = False
        self.alarm2_enabled = False
        self.alarm1 = dt.time(0,0,0)
        self.alarm2 = dt.time(0,0,0)
        self.editing_alarm_1 = False
        self.editing_alarm_2 = False
        self.alarm1held = False
        self.alarm2held = False

