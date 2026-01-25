from datetime import datetime as dt

from PIL.ImageDraw import ImageDraw

from .state import AlarmState

def draw_time(draw):
    time = dt.now().strftime("%H:%M")
    draw.text(
        (64, 32), 
        time, 
        fill=255,
        anchor="mm",
        font_size=30)

def draw_alarm_bells(draw: ImageDraw, state: AlarmState):
    print(draw.fill)
    if state.alarm1_enabled:
        f = 0
        if state.editing_alarm_1:
            f = 255
        draw.circle((8,8),4,f,255,2)
    if state.alarm2_enabled:
        f = 0
        if state.editing_alarm_2:
            f = 255
        draw.circle((24,8),4,f, 255,2)
