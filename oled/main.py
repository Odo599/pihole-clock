import time

import display
import display.preview as preview
from drawing.draw_time import draw_time
import input

from button_libs.check_events import check_events

fb = display.init_display()
buttons = input.init_buttons()

# ui testing
def draw_ui(draw):
    draw_time(draw)
fb.draw(draw_ui)
preview.save_frame(fb)


# button testing
buttons.press("PLAY")
check_events(buttons)
time.sleep(1)
check_events(buttons)
buttons.release("PLAY")
check_events(buttons)
