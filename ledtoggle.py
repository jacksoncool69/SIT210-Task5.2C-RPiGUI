from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
from gpiozero import LED
import time
win = Tk()
win.title("RGB GUI!")
win.geometry("300x300")


blue = LED(4)
red = LED(17)
green = LED(22)
GPIO.setmode(GPIO.BCM)

v = IntVar()

def clicked(value):
    MyLabel = Label(win, text=value)
def BlueToggle():
    if blue.is_lit:
        blue.off()
        BlueButton["text"] = "turn blue on"
    else:
        blue.on()
        BlueButton["text"] = "turn blue off"

def RedToggle():
    if red.is_lit:
        red.off()
        RedButton["text"] = "turn red on"
    else:
        red.on()
        RedButton["text"] = "turn red off"
        
def GreenToggle():
    if green.is_lit:
        green.off()
        GreenButton["text"] = "turn green on"
    else:
        green.on()
        GreenButton["text"] = "turn green off"

def BlueOnly():
        blue.on()
        green.off()
        red.off()
        BlueButton["text"] = "turn blue off"
        GreenButton["text"] = "turn green on"
        RedButton["text"] = "turn red on"

def RedOnly():
        red.on()
        green.off()
        blue.off()
        RedButton["text"] = "turn red off"
        GreenButton["text"] = "turn green on"
        BlueButton["text"] = "turn blue on"

def GreenOnly():
        green.on()
        red.off()
        blue.off()
        GreenButton["text"] = "turn green off"
        RedButton["text"] = "turn red on"
        BlueButton["text"] = "turn blue on"
        
def which(value):
    if value == 1:
        BlueToggle()
    elif value == 2:
        RedToggle()
    elif value == 3:
        GreenToggle()
    elif value == 4:
        BlueOnly()
    elif value == 5:
        RedOnly()
    elif value == 6:
        GreenOnly()
    
def close():
    GPIO.cleanup()
    win.destroy()


BlueButton = Radiobutton(win, variable= v, value = 1, text = 'Turn blue on', command = lambda: [clicked(v.get())])
BlueOnlyButton = Radiobutton(win, variable= v, value = 4, text = 'Turn blue only on and others off', command = lambda: [clicked(v.get())])

RedButton = Radiobutton(win, variable= v, value = 2, text = 'Turn red on', command = lambda: [clicked(v.get())])
RedOnlyButton = Radiobutton(win, variable= v, value = 5, text = 'Turn red only on and others off', command = lambda: [clicked(v.get())])

GreenButton = Radiobutton(win, variable= v, value = 3, text = 'Turn green on',  command = lambda: [clicked(v.get())])
GreenOnlyButton = Radiobutton(win, variable= v, value = 6, text = 'Turn green only on and others off', command = lambda: [clicked(v.get())])

ToggleButton = Button(win, text = "toggle", command = lambda: which(v.get()))

ExitButton = Button(win, text = 'Exit', command = close, bg = 'red')



BlueButton.pack()
RedButton.pack()
GreenButton.pack()
BlueOnlyButton.pack()
RedOnlyButton.pack()
GreenOnlyButton.pack()
ToggleButton.pack()
ExitButton.pack()



win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()
