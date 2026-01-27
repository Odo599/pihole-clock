from .backend import create_device
from .framebuffer import FrameBuffer

def init_display():
    device = create_device()
    return FrameBuffer(device)

