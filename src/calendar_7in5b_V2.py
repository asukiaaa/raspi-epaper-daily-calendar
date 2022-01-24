#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5b_V2
from PIL import Image
import time
import pytz
from create_calendar_image import create_calendar_image
import get_holiday
from datetime import datetime

jpt = pytz.timezone('Asia/Tokyo')
day = datetime.now(jpt)
# day = datetime(2022,1,23)
# day = datetime(2022,5,4)
logging.basicConfig(level=logging.DEBUG)

# https://www.waveshare.com/7.5inch-e-paper-hat-b.htm
width = 800
height = 480

try:
    logging.info("calendar for epd7in5b_V2")

    epd = epd7in5b_V2.EPD()
    epd.init()
    image_blank = Image.new('1', (epd.height, epd.width), 255)

    name_holiday = get_holiday.get_name(day)
    image_texts = create_calendar_image(epd.height, epd.width, day, name_holiday)

    # Drawing on the Horizontal image
    if name_holiday is None and day.weekday() != 6:
        epd.display(epd.getbuffer(image_texts), epd.getbuffer(image_blank))
    else:
        epd.display(epd.getbuffer(image_blank), epd.getbuffer(image_texts))
    time.sleep(2)
    epd.sleep()
    time.sleep(2)

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd7in5b_V2.epdconfig.module_exit()
    exit()
