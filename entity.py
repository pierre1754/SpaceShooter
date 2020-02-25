from tkinter import Canvas
from vector import vector

class entity:
    def __init__(self, can: Canvas, shape, shootSpeed: vector):
        self.__can = can
        self.__shape = shape
        self.__onShot = False
        self.__timer = 0
        self.__shoots = []
        self.__shootSpeed = shootSpeed

    def move(self, to_add: vector):
        x, y, w, h = self.__can.bbox(self.__shape)
        w -= x
        h -= y
        if self.__shootSpeed.x == 0 and self.__shootSpeed.y == 0:
            self.__can.move(self.__shape, to_add.x, to_add.y)
            return
        
        if 0 < x + to_add.x < 700 - w:
            self.__can.move(self.__shape, to_add.x, 0)
        else:
            self.__can.move(self.__shape, 0, to_add.y)

        if 0 < y + to_add.y < 700 - h:
            self.__can.move(self.__shape, 0, to_add.y)
        else:
            self.__can.move(self.__shape, 0, 0)


    def shot(self):
        if self.__onShot == False:
            self.__onShot = True
            self.__timer = 0
            x, y, w, h = self.__can.bbox(self.__shape)
            w -= x
            h -= y
            self.__shoots.append(entity(self.__can, self.__can.create_rectangle(x, y, x - 50, y + 50, fill = 'yellow'), vector(0, 0)))

    def __readyToShot(self):
        self.__onShot = False

    def update(self, time):
        self.__timer += time
        if self.__timer > 300:
            self.__timer = 0
            self.__readyToShot()
        for i in self.__shoots:
            i.move(self.__shootSpeed)
