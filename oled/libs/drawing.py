from datetime import datetime as dt

def draw_time(draw):
    time = dt.now().strftime("%H:%M")
    draw.text(
        (64, 32), 
        time, 
        fill=255,
        anchor="mm",
        font_size=30)

def draw_alarm_bells(draw, state):

    draw.circle((8,8),4,255,2)
    draw.circle((24,8),4,255,2)