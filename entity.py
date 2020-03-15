import images
from tkinter import Canvas
from vector import vector
from pygame import mixer
from sound import play

class entity:
    def __init__(self, can: Canvas, shape, shootSpeed: vector):
        self.__can = can
        self.shape = shape
        self.__onShot = False
        self.__onShotbad = False
        self.__timer = 0
        self.__timerShot = 0
        self.__shoots = []
        self.__shootSpeed = shootSpeed
        self.__dybad = -8
        self.__dxbad = -8
        
    def move(self, to_add: vector):
        x, y, w, h = self.__can.bbox(self.shape)
        w -= x
        h -= y
        if self.__shootSpeed.x == 0 and self.__shootSpeed.y == 0:
            self.__can.move(self.shape, to_add.x, to_add.y)
            return

        if 0 < x + to_add.x < self.__can.winfo_width() - w:
            self.__can.move(self.shape, to_add.x, 0)
        else:
            self.__can.move(self.shape, 0, to_add.y)

        if 0 < y + to_add.y < self.__can.winfo_height() - h:
            self.__can.move(self.shape, 0, to_add.y)
        else:
            self.__can.move(self.shape, 0, 0)

    def movebad(self):
        x, y, w, h = self.__can.bbox(self.shape)

        w -= x
        h -= y

        self.__can.move(self.shape, self.__dxbad, self.__dybad)

        if x + self.__dxbad < self.__can.winfo_width() * 0.5 or x + self.__dxbad > self.__can.winfo_width() - w:
            self.__dxbad *= -1
        if y + self.__dybad < 0 - 5 or y + self.__dybad > self.__can.winfo_height() - h:
            self.__dybad *= -1

    def shot(self):
        if self.__onShot == False:
            self.__onShot = True
            self.__timer = 0
            x, y, w, h = self.__can.bbox(self.shape)
            w -= x
            h -= y
            self.__shoots.append(entity(self.__can, self.__can.create_image(x + 192, y + 45, image = images.clone(3)), vector(0, 0)))
            play(1)

    def shotbad(self):
        if self.__onShotbad == False:
            self.__onShotbad = True
            self.__timerShot = 0
            x, y, w, h = self.__can.bbox(self.shape)
            w -= x
            h -= y
            self.__shoots.append(entity(self.__can, self.__can.create_image(x, y + 52, image = images.clone(4)), vector(0, 0)))
            play(2)

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
            x, y, w, h = self.__can.bbox(i.shape)
            w -= x
            h -= y
            if x < 0 - w:
                self.__can.delete(i.shape)
                self.__shoots.remove(i)
            if x > self.__can.winfo_width():
                self.__can.delete(i.shape)
                self.__shoots.remove(i)



    """ def update(self, time):
        self.__timerShot += time
        if self.__timerShot > 3000:
            self.__timerShot = 0
            self.__can.delete(self.__shoots) """
