import time
import logging

logger = logging.getLogger(__name__)

## ALARM BUTTONS
# Press
def pressAlarm1(buttons):
    logger.info("Virtual ALARM1 button press")
    buttons.press("ALARM1")
    time.sleep(0.1)
    buttons.release("ALARM1")

def pressAlarm2(buttons):
    logger.info("Virtual ALARM2 button press")
    buttons.press("ALARM2")
    time.sleep(0.1)
    buttons.release("ALARM2")

# Hold
def startHoldAlarm1(buttons):
    logger.info("Virtual ALARM1 start hold")
    buttons.press("ALARM1")
    time.sleep(0.7)

def endHoldAlarm1(buttons):
    logger.info("Virtual ALARM1 end hold")
    buttons.release("ALARM1")

def startHoldAlarm2(buttons):
    logger.info("Virtual ALARM2 start hold")
    buttons.press("ALARM2")
    time.sleep(0.7)

def endHoldAlarm2(buttons):
    logger.info("Virtual ALARM2 end hold")
    buttons.release("ALARM2")

## HOUR & MINUTE
# Press
def pressHour(buttons):
    logger.info("Virtual HOUR button press")
    buttons.press("HOUR")
    time.sleep(0.1)
    buttons.release("HOUR")

def pressMinute(buttons):
    logger.info("Virtual MINUTE button press")
    buttons.press("MINUTE")
    time.sleep(0.1)
    buttons.release("MINUTE")