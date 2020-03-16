from tkinter import PhotoImage

def init():
    global vessel, enemy, allyshot, enemyshot
    vessel = PhotoImage (file = "vessel.gif")
    enemy = PhotoImage (file = "enemy.gif")
    allyshot = PhotoImage (file = "allyshot.gif")
    enemyshot = PhotoImage (file = "enemyshot.gif")

def clone(type):
    if type == 2:
        return vessel
    elif type == 3:
        return enemy
    elif type == 4:
        return allyshot
    elif type == 5:
        return enemyshot
