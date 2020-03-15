from tkinter import PhotoImage

def init():
    global background, vessel, enemy, allyshot, enemyshot
    background = PhotoImage (file = "background.gif")
    vessel = PhotoImage (file = "vessel.gif")
    enemy = PhotoImage (file = "enemy.gif")
    allyshot = PhotoImage (file = "allyshot.gif")
    enemyshot = PhotoImage (file = "enemyshot.gif")

def clone(type):
    if type == 1:
        return background
    elif type == 2:
        return vessel
    elif type == 3:
        return enemy
    elif type == 4:
        return allyshot
    elif type == 5:
        return enemyshot
