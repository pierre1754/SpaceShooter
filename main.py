from tkinter import Tk, Canvas, PhotoImage
import tkinter as tk
from entity import entity, vector

fenetre=Tk()

fenetre.title("SpaceShooter")

largeur=700
hauteur=700

can=Canvas(fenetre,height=hauteur,width=largeur)

can.pack()
can.focus_set()

mechant1 = entity(can, can.create_rectangle(0, 0, 50, 50, fill='red'), vector(-20, 0))

vessel = entity(can, can.create_oval(0, 0, 110, 50, fill = 'blue'), vector(20, 0))

mechant1.move(vector(400, 50))

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
    mechant1.shot()
    fenetre.after(16, loop)

loop()




# def deplacement():
#     global dx, dy, largeur
#     if (can.coords(tir2)[0]>can.coords(mechant1)[0]) and (can.coords(tir2)[1]<can.coords(mechant1)[3]) and (can.coords(tir2)[1]>can.coords(mechant1)[1]):
#         can.delete(tir2)
#         can.delete(mechant1)
#     else:
#         if (can.coords(tir2)[0]>largeur):
#             can.delete(tir2)
#         else:
#             can.move(tir2,dx,dy)
#             #print(can.coords(tir2))
#             fenetre.after(20,deplacement)



# def espace(event):
#     global tir2, dx, dy
#     dx=5
#     dy=0
#     tir2=can.create_image(x1+50,y1+20,image=img)
#     deplacement()


# move()
# fenetre.bind("<space>",espace)
fenetre.mainloop()
