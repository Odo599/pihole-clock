import display
import display.preview as preview
from drawing.draw_time import draw_time

fb = display.init_display()

def draw_ui(draw):
    draw_time(draw)

fb.draw(draw_ui)

preview.save_frame(fb)