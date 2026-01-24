# display/framebuffer.py

from PIL import Image, ImageDraw


class FrameBuffer:
    def __init__(self, device):
        self.device = device
        self.width = device.width
        self.height = device.height
        self.image = Image.new("1", (self.width, self.height))

    def draw(self, draw_fn):
        self.image = Image.new("1", (self.width, self.height))
        draw = ImageDraw.Draw(self.image)
        draw_fn(draw)
        self.device.display(self.image)

    def clear(self):
        self.image = Image.new("1", (self.width, self.height))
        self.device.display(self.image)
