
import eel
import os
import sys
import click_img
from web import sheet
from googleAPI import *
eel.init('web')

@eel.expose
def a():
    print("pizza")
@eel.expose
def b():
    print("chapatti")
@eel.expose
def c():
    print("roti")
@eel.expose
def d():
    print("burger")
@eel.expose
def e():
    print("Activate")
    os.system("python3 Face.py")

@eel.expose
def reg(data):
    print(data)
    os.mkdir("/home/jacob3006/Desktop/edith/images/"+data)
    click_img.start(data)
    sheet.read("Sheet1!A1:B5")


eel.start('index.html', size=(1000, 600))
