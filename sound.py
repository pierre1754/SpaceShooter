from pygame import mixer

# Son
def init():
    mixer.init()
    global allyshot, enemyshot
    allyshot = mixer.Sound("allyshot.wav")
    enemyshot = mixer.Sound("enemyshot.wav")

def play(type):
    if type == 1:
        allyshot.play()
    elif type == 2:
        enemyshot.play()
