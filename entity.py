import images
import world
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
        self.shoots = []
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
            self.shoots.append(entity(self.__can, self.__can.create_image(x + 150, y + 45, image = images.clone(4)), vector(0, 0)))
            play(1)

    def shotbad(self):
        if self.__onShotbad == False:
            self.__onShotbad = True
            self.__timerShot = 0
            x, y, w, h = self.__can.bbox(self.shape)
            w -= x
            h -= y
            self.shoots.append(entity(self.__can, self.__can.create_image(x, y + 52, image = images.clone(5)), vector(0, 0)))
            play(2)

    def __readyToShot(self):
        self.__onShot = False
        self.__onShotbad = False

    def onHit(self, entity):
        xa, ya, wa, ha = self.__can.bbox(self.shape)
        xb, yb, wb, hb = self.__can.bbox(entity.shape)
        return xb <= wa <= wb + wa - xa and yb <= ha <= hb + ha - ya

    def update(self, time):
        self.__timer += time
        if self.__timer > 300:
            self.__timer = 0
            self.__readyToShot()
        for shot in self.shoots:
            # Bouge les tirs
            shot.move(self.__shootSpeed)
            
            # Tir qui touchent
            entities = world.getEntitiesList(self)
            for entity in entities:
                if shot.onHit(entity):
                    print("ALA AKBAR")
            
            # Tir sort de l'écran
            x, y, w, h = self.__can.bbox(shot.shape)
            w -= x
            h -= y
            if x < 0 - w:
                self.__can.delete(shot.shape)
                self.shoots.remove(shot)
            if x > self.__can.winfo_width():
                self.__can.delete(shot.shape)
                self.shoots.remove(shot)
            