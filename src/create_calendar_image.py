#!/usr/bin/python
# -*- coding:utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import locale

text_dates = [u'月曜日', u'火曜日', u'水曜日', u'木曜日', u'金曜日', u'土曜日', u'日曜日']

def create_calendar_image(
    width, height, target_day, nameHoliday=None
) -> Image:
    year = target_day.year
    month = target_day.month
    day = target_day.day
    textDate = text_dates[target_day.weekday()]
    fontNotoYear = ImageFont.truetype(
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 70
    )
    fontNotoDay = ImageFont.truetype(
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 400
    )
    fontNotoDate = fontNotoYear
    fontNotoHoliday = ImageFont.truetype(
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 60
    )

    Himage = Image.new("1", (width, height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    textYM = u"%d年 %d月" % (year, month)
    wYM, hYM = draw.textsize(textYM, font=fontNotoYear)
    draw.text((width / 2 - wYM / 2, 0), textYM, font=fontNotoYear, fill=0)
    textDay = "%d" % day
    wDay, hDay = draw.textsize(textDay, font=fontNotoDay)
    draw.text((width / 2 - wDay / 2, 30), textDay, font=fontNotoDay, fill=0)
    bottomDay = 100 + hDay
    wDate, hDate = draw.textsize(textDate, font=fontNotoDate)
    draw.text(
        (width / 2 - wDate / 2, bottomDay + 10), textDate, font=fontNotoDate, fill=0
    )
    if nameHoliday is not None:
        wHoliday, hHoliday = draw.textsize(nameHoliday, font=fontNotoHoliday)
        draw.text(
            (width / 2 - wHoliday / 2, bottomDay + hDate + 20),
            nameHoliday,
            font=fontNotoHoliday,
            fill=0,
        )
    return Himage

if __name__ == '__main__':
    from datetime import datetime
    day = datetime(2022,5,4,10,00)
    image = create_calendar_image(
        480, 800, target_day=day, nameHoliday=u"みどりの日"
    )
    image.save("test.png")
