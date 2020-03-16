import tkinter as tk
from tkinter import Tk, Canvas
from entity import entity, vector
import sound
import images
import world

window = Tk()

# window.attributes('-fullscreen', True)

sound.init()
images.init()
world.init()

window.title("SpaceShooter")

# width = window.winfo_screenwidth()
# height = window.winfo_screenheight()

width = 1366
height = 768

can = Canvas(window, height = height,  width = width)

can.pack()
can.focus_set()

world.addEntity(entity(can, can.create_image(width * 0.25, height * 0.5, image = images.clone(2)), vector(20, 0), 100))
world.addEntity(entity(can, can.create_image(width * 0.75, height * 0.5, image = images.clone(3)), vector(-20, 0), 100))

key_press = {"Left": False, "Right": False, "Up": False, "Down": False, "space":False, "Escape":False}

def press(event):
    key_press[event.keysym] = True

def release(event):
    key_press[event.keysym] = False

for key in ["Up", "Left", "Right", "Down", "space", "Escape"]:
    can.bind('<KeyPress-%s>' %key, press)
    can.bind('<KeyRelease-%s>' %key, release)

def loop():
    if key_press["Right"]:
        world.getVessel().move(vector(10, 0))
    if key_press["Left"]:
        world.getVessel().move(vector(-10, 0))
    if key_press["Up"]:
        world.getVessel().move(vector(0, -10))
    if key_press["Down"]:
        world.getVessel().move(vector(0, 10))
    if key_press["space"]:
        world.getVessel().shot()
    if key_press["Escape"]:
        world.destroy()
        window.destroy()
        return
    world.update(16)
    if world.end:
        world.destroy()
        window.destroy()
        return
    world.enemiesUpdate()
    window.after(16, loop)

loop()
window.mainloop()
