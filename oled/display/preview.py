from PIL import Image
import time

def save_frame(framebuffer):
    framebuffer.image.show()

def timed_preview(device, seconds=5):
    time.sleep(seconds)
    save_frame(device)
