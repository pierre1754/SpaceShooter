import tkinter as tk
import pygame
from tkinter import Tk, Canvas, PhotoImage
from entity import entity, vector
from pygame import mixer

fenetre=Tk()

fenetre.title("SpaceShooter")

width = 1600
height = 900

can=Canvas(fenetre, height = height ,  width = width ) 

can.pack()
can.focus_set()
pygame.init()

img = PhotoImage (file = "660.gif")

mechant1 = entity(can, can.create_rectangle(0, 0, 50, 50, fill = 'red'), vector(-20, 0))

vessel = entity(can, can.create_image(500, 0, image = img), vector(20, 0))

mechant1.move(vector(1500, 300))

vessel.move(vector(100, 300))

key_press = {"Left": False, "Right": False, "Up": False, "Down": False, "space":False}

def press(event):
    key_press[event.keysym] = True

def release(event):
    key_press[event.keysym] = False

for key in ["Up", "Left", "Right", "Down", "space"]:
    can.bind('<KeyPress-%s>' %key, press)
    can.bind('<KeyRelease-%s>' %key, release)

def loop():
    if key_press["Right"]:
        vessel.move(vector(10, 0))
    if key_press["Left"]:
        vessel.move(vector(-10, 0))
    if key_press["Up"]:
        vessel.move(vector(0, -10))
    if key_press["Down"]:
        vessel.move(vector(0, 10))
    if key_press["space"]:
        vessel.shot()
    vessel.update(16)
    mechant1.update(16)
    mechant1.movebad()
    mechant1.shotbad()
    fenetre.after(16, loop)

loop()

fenetre.mainloop()
