from datetime import datetime as dt

def draw_time(draw):
    time = dt.now().strftime("%H:%M")
    draw.text(
        (64, 32), 
        time, 
        fill=255,
        anchor="mm",
        font_size=30)