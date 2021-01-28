
from tkinter import *
from time import *

win = Tk()

xA = 0
yA = 0

x = 100
y = 100

keyUp = keyLeft = keyRight = False
keyUpCode = 111
keyLeftCode = 113
keyRightCode = 114

def keyPress(event):
   global keyUp, keyLeft, keyRight, keyUpCode, keyLeftCode, keyRightCode
   #print(event.keycode)
   code = event.keycode
   if code == keyUpCode: keyUp = True
   if code == keyLeftCode: keyLeft = True
   if code == keyRightCode: keyRight = True

def keyRelease(event):
   global keyUp, keyLeft, keyRight, keyUpCode, keyLeftCode, keyRightCode
   #print(event.keycode)
   code = event.keycode
   if code == keyUpCode: keyUp = False
   if code == keyLeftCode: keyLeft = False
   if code == keyRightCode: keyRight = False

win.bind("<KeyPress>", keyPress)
win.bind("<KeyRelease>", keyRelease)

pic = Canvas(width=800, height=600, bg="white")
pic.pack()

while 1:
    yA += .098
    x += xA
    y += yA
    if keyRight: xA += .1
    if keyLeft: xA -= .1
    if keyUp and y>573: yA = 10
    if y < 25:
        yA = (-yA)/1.5
        y = 25
        xA -= xA/5
    if y > 575:
        yA = (-yA)/1.5
        y = 575
        xA -= xA/100
    if x < 25:
        xA = (-xA)/1.5
        x = 25
        yA -= yA/5
    if x > 775:
        xA = (-xA)/1.5
        x = 775
        yA -= yA/5


    #print(y)
    pic.delete("all")
    pic.create_oval(x-25, y-25, x+25, y+25, fill="black")
    pic.update()
    sleep(.01)

win.mainloop()







