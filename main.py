import os
import click_img
import sheet


def reg(data):
    print(data)
    os.mkdir("images/" + data)
    click_img.start(data)

    a = 1
    consumer_column = "Sheet1!A" + str(a) + ":A" + str(a + 1)

    sheet.write(data, consumer_column)

    a += 1
