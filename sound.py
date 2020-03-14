from pygame import mixer

def init():
    mixer.init()
    global sound
    sound = mixer.Sound("soundshot1.wav")

def play():
    sound.play()
