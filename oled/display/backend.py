from luma.oled.device import ssd1306
from luma.core.interface.serial import noop, spi
from .config import (
    DISPLAY_WIDTH,
    DISPLAY_HEIGHT,
    USE_HARDWARE,
    SPI_PORT,
    SPI_DEVICE,
    GPIO_DC,
    GPIO_RST,
)

def create_device():
    if USE_HARDWARE:
        serial = spi(
            port=SPI_PORT,
            device=SPI_DEVICE,
            gpio_DC=GPIO_DC,
            gpio_RST=GPIO_RST,
        )
    else:
        serial = noop()

    return ssd1306(
        serial,
        width=DISPLAY_WIDTH,
        height=DISPLAY_HEIGHT,
    )
