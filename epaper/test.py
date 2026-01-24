import sys
import os
import time
import logging

import epd1in54_V2
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.INFO)

logging.info("Testing display")

epd = epd1in54_V2.EPD()

logging.info("Init and clear")
epd.init(0)
epd.Clear(0xFF)
time.sleep(1)

logging.info("Starting...")
image = Image.new('1', (epd.width, epd.height), 255)
font = ImageFont.truetype('Font.ttc', 24)
draw = ImageDraw.Draw(image)

draw.text((8, 12), 'Starting...', font = font, fill = 0)

epd.display(epd.getbuffer(image.rotate(180)))


logging.info("Goto Sleep...")
epd.sleep()
