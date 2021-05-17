import eel
import os
import sys
import click_img
import sheet

eel.init('web')


@eel.expose
def a():
    print("Pizza")
    sheet.write("Pizza", "Sheet1!B1:B1")


@eel.expose
def b():
    print("Chapatti")
    sheet.write("Chapatti", "Sheet1!B1:B1")


@eel.expose
def c():
    print("Roti")
    sheet.write("Roti", "Sheet1!B1:B1")


@eel.expose
def d():
    print("Burger")
    sheet.write("Burger", "Sheet1!B1:B1")


@eel.expose
def e():
    print("Activate")
    os.system("python3 Face.py")


@eel.expose
def reg(data):
    print(data)
    os.mkdir("images/" + data)
    click_img.start(data)

    a = 1
    consumer_column = "Sheet1!A" + str(a) + ":A" + str(a + 1)

    sheet.write(data, consumer_column)

    a += 1


eel.start('index.html', size=(1000, 600))
