import display
import display.preview as preview

fb = display.init_display()

def draw_ui(draw):
    draw.text((0, 0), "07:30", fill=255)
    draw.text((0, 16), "ALARM SET", fill=255)

fb.draw(draw_ui)

preview.save_frame(fb)