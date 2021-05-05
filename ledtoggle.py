from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
from gpiozero import LED
import time

win = Tk()
win.title("RGB GUI!")
myFont = tkinter.font.Font(family = 'Times', size = 12, weight = 'bold')

blue = LED(4)
red = LED(17)
green = LED(22)
GPIO.setmode(GPIO.BCM)

def BlueToggle():
    if blue.is_lit:
        blue.off()
        BlueButton["text"] = "Turn blue on"
        BlueOnlyButton["text"] = "Turn blue only on and others off"
    else:
        blue.on()
        BlueButton["text"] = "Turn blue off"
        BlueOnlyButton["text"] = "Turn blue only off and others off"

def RedToggle():
    if red.is_lit:
        red.off()
        RedButton["text"] = "Turn red on"
        RedOnlyButton["text"] = "Turn red only on and others off"
    else:
        red.on()
        RedButton["text"] = "Turn red off"
        RedOnlyButton["text"] = "Turn red only off and others off"
def GreenToggle():
    if green.is_lit:
        green.off()
        GreenButton["text"] = "Turn green on"
        GreenOnlyButton["text"] = "Turn green only on and others off"
    else:
        green.on()
        GreenButton["text"] = "Turn green off"
        GreenOnlyButton["text"] = "Turn green only off and others off"

def RedOnly():
    if red.is_lit:
        red.off()
        RedOnlyButton["text"] = "Turn red only on and others off"
        RedButton["text"] = "Turn red on"
        green.off()
        blue.off()
        BlueButton["text"] = "Turn blue on"
        GreenButton["text"] = "Turn green on"
        BlueOnlyButton["text"] = "Turn blue only on and others off"
        GreenOnlyButton["text"] = "Turn green only on and others off"
    else:
        red.on()
        green.off()
        blue.off()
        RedOnlyButton["text"] = "Turn red only off and others off"
        BlueButton["text"] = "Turn blue on"
        RedButton["text"] = "Turn red off"
        GreenButton["text"] = "Turn green on"
        BlueOnlyButton["text"] = "Turn blue only on and others off"
        GreenOnlyButton["text"] = "Turn green only on and others off"

def GreenOnly():
    if green.is_lit:
        green.off()
        GreenOnlyButton["text"] = "Turn green only on and others off"
        GreenButton["text"] = "Turn green on"
        red.off()
        blue.off()
        BlueButton["text"] = "Turn blue on"
        RedButton["text"] = "Turn red on"
        RedOnlyButton["text"] = "Turn red only on and others off"
        BlueOnlyButton["text"] = "Turn blue only on and others off"
    else:
        green.on()
        red.off()
        blue.off()
        GreenOnlyButton["text"] = "Turn green only off and others off"
        BlueButton["text"] = "Turn blue on"
        RedButton["text"] = "Turn red on"
        GreenButton["text"] = "Turn green off"
        RedOnlyButton["text"] = "Turn red only on and others off"
        BlueOnlyButton["text"] = "Turn blue only on and others off"

def BlueOnly():
    if blue.is_lit:
        blue.off()
        BlueOnlyButton["text"] = "Turn blue only on and others off"
        BlueButton["text"] = "Turn blue on"
        red.off()
        green.off()
        GreenButton["text"] = "Turn green on"
        RedButton["text"] = "Turn red on"
        RedOnlyButton["text"] = "Turn red only on and others off"
        GreenOnlyButton["text"] = "Turn green only on and others off"
    else:
        blue.on()
        red.off()
        green.off()
        BlueOnlyButton["text"] = "Turn blue only off and others off"
        GreenButton["text"] = "Turn green on"
        RedButton["text"] = "Turn red on"
        BlueButton["text"] = "Turn blue off"
        RedOnlyButton["text"] = "Turn red only on and others off"
        GreenOnlyButton["text"] = "Turn green only on and others off"

def close():
    GPIO.cleanup()
    win.destroy()

BlueButton = Button(win, text = 'Turn blue on', font = myFont, command = BlueToggle, bg = 'blue', height = 2, width = 30)
BlueButton.grid(row=0,column=1)

BlueOnlyButton = Button(win, text = 'Turn blue only on and others off', font = myFont, command = BlueOnly, bg = 'blue', height = 2, width = 30)
BlueOnlyButton.grid(row=1,column=1)

RedButton = Button(win, text = 'Turn red on', font = myFont, command = RedToggle, bg = 'red', height = 2, width = 30)
RedButton.grid(row=0,column=2)

RedOnlyButton = Button(win, text = 'Turn red only on and others off', font = myFont, command = RedOnly, bg = 'red', height = 2, width = 30)
RedOnlyButton.grid(row=1,column=2)

GreenButton = Button(win, text = 'Turn green on', font = myFont, command = GreenToggle, bg = 'green', height = 2, width = 30)
GreenButton.grid(row=0,column=3)

GreenOnlyButton = Button(win, text = 'Turn green only on and others off', font = myFont, command = GreenOnly, bg = 'green', height = 2, width = 30)
GreenOnlyButton.grid(row=1,column=3)

ExitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'white', height = 2, width = 30)
ExitButton.grid(row=2,column=2)

win.protocol("WM_DELETE_WINDOW", close)