import pygame
from tkinter import Canvas
from vector import vector
from pygame import mixer

class entity:
    def __init__(self, can: Canvas, shape, shootSpeed: vector):
        self.__can = can
        self.__shape = shape
        self.__onShot = False
        self.__onShotbad = False
        self.__timer = 0
        self.__timerShot = 0
        self.__shoots = []
        self.__shootSpeed = shootSpeed
        self.__dybad = -8
        self.__dxbad = -8
        self.__son = pygame.mixer.Sound("soundshot1.wav")

    def move(self, to_add: vector):
        x, y, w, h = self.__can.bbox(self.__shape)
        w -= x
        h -= y
        if self.__shootSpeed.x == 0 and self.__shootSpeed.y == 0:
            self.__can.move(self.__shape, to_add.x, to_add.y)
            return
        
        if -8 < x + to_add.x < 1608 - w:
            self.__can.move(self.__shape, to_add.x, 0)
        else:
            self.__can.move(self.__shape, 0, to_add.y)

        if -5 < y + to_add.y < 840 - h:
            self.__can.move(self.__shape, 0, to_add.y)
        else:
            self.__can.move(self.__shape, 0, 0)

    def movebad(self):
        x, y, w, h = self.__can.bbox(self.__shape)
        
        w -= x
        h -= y

        self.__can.move(self.__shape, self.__dxbad, self.__dybad)

        if y + self.__dybad < -5 or y + self.__dybad > 800:
            self.__dybad *= -1
        if x + self.__dxbad < 600 or x + self.__dxbad > 1550:
            self.__dxbad *= -1

    def shot(self):
        if self.__onShot == False:
            self.__onShot = True
            self.__timer = 0
            x, y, w, h = self.__can.bbox(self.__shape)
            w -= x
            h -= y
            self.__shoots.append(entity(self.__can, self.__can.create_rectangle(x, y, x - 50, y + 50, fill = 'yellow'), vector(0, 0)))
            self.__son.play()

    def shotbad(self):
        if self.__onShotbad == False:
            self.__onShotbad = True
            self.__timerShot = 0
            x, y, w, h = self.__can.bbox(self.__shape)
            w -= x
            h -= y
            self.__shoots.append(entity(self.__can, self.__can.create_rectangle(x, y, x - 50, y + 50, fill = 'black'), vector(0, 0)))

    def __readyToShot(self):
        self.__onShot = False
        self.__onShotbad = False

    def update(self, time):
        self.__timer += time
        if self.__timer > 300:
            self.__timer = 0
            self.__readyToShot()
        for i in self.__shoots:
            i.move(self.__shootSpeed)
        
    """ def update(self, time):
        self.__timerShot += time
        if self.__timerShot > 3000:
            self.__timerShot = 0
            self.__can.delete(self.__shoots) """
