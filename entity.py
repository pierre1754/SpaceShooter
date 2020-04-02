import images
import world
from tkinter import Canvas
from vector import vector
from pygame import mixer
from sound import play

class entity:
    # Définition de toutes les variables utilisées par la suite
    def __init__(self, can: Canvas, shape, shootSpeed: vector, life):
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
        self.life = life
        x, y, w, h = self.__can.bbox(self.shape)
        if life > 0:
            self.__gauge = self.__can.create_text((w + x) / 2, h + 20, font = ("Arial", 32), text = self.life, fill = 'red')
        else:
            self.__gauge = None


    # Suppression de l'entitée du canevas (appelée une fois que l'entitée est supprimée de la liste)
    def __del__(self):
        self.__can.delete(self.shape)
        if self.__gauge != None:
            self.__can.delete(self.__gauge)

    # Définition des mouvements ainsi que des limites du vaisseau controlé (vector étant la fonction de déplacement)
    def move(self, to_add: vector):
        x, y, w, h = self.__can.bbox(self.shape)
        w -= x
        h -= y

        if self.__shootSpeed.x == 0 and self.__shootSpeed.y == 0:
            self.__can.move(self.shape, to_add.x, to_add.y)
            if self.__gauge != None:
                self.__can.move(self.__gauge, to_add.x, to_add.y)
            return

        if 0 < x + to_add.x < self.__can.winfo_width() - w:
            self.__can.move(self.shape, to_add.x, 0)
            if self.__gauge != None:
                self.__can.move(self.__gauge, to_add.x, 0)
        else:
            self.__can.move(self.shape, 0, to_add.y)
            if self.__gauge != None:
                self.__can.move(self.__gauge, 0, to_add.y)

        if 0 < y + to_add.y < self.__can.winfo_height() - h:
            self.__can.move(self.shape, 0, to_add.y)
            if self.__gauge != None:
                self.__can.move(self.__gauge, 0, to_add.y)

    # Définition des mouvements mouvement de l'ennemis
    def movebad(self):
        x, y, w, h = self.__can.bbox(self.shape)
        w -= x
        h -= y

        self.__can.move(self.shape, self.__dxbad, self.__dybad)
        if self.__gauge != None:
            self.__can.move(self.__gauge, self.__dxbad, self.__dybad)

        if x + self.__dxbad < self.__can.winfo_width() * 0.5 or x + self.__dxbad > self.__can.winfo_width() - w:
            self.__dxbad *= -1
        if y + self.__dybad < 0 - 5 or y + self.__dybad > self.__can.winfo_height() - h:
            self.__dybad *= -1

    # Tirs du vaisseau
    def shot(self):
        # Avec le timer on définis l'intervale entre chaques tirs
        if self.__onShot == False:
            self.__onShot = True
            self.__timer = 0
            # Récupération des coordonnées du vaisseau avec une bbox
            x, y, w, h = self.__can.bbox(self.shape)
            w -= x
            h -= y
            # Création des tirs
            self.shoots.append(entity(self.__can, self.__can.create_image(x + 150, y + 45, image = images.clone(4)), vector(0, 0), 0))
            # Le son 1 est appelé pour le tir allié
            play(1)

    # Définition des tirs ennemis
    def shotbad(self):
        # De même que pour le timer du tir allié
        if self.__onShotbad == False:
            self.__onShotbad = True
            self.__timerShot = 0
            # --
            x, y, w, h = self.__can.bbox(self.shape)
            w -= x
            h -= y
            # --
            self.shoots.append(entity(self.__can, self.__can.create_image(x, y + 52, image = images.clone(5)), vector(0, 0), 0))
            play(2)


    def __readyToShot(self):
        self.__onShot = False
        self.__onShotbad = False

    # Définition des hitbox
    def onHit(self, entity):
        # Récupération des coordonnées du vaisseau + ennemis
        xa, ya, wa, ha = self.__can.bbox(self.shape)
        xb, yb, wb, hb = self.__can.bbox(entity.shape)
        # Conditions pour les tirs:
        #   Si les coordonnées des tirs ne sont pas confondues avec celles des entitées alors ne rien return
        return xb <= wa <= wb + wa - xa and yb <= ha <= hb + ha - ya

    # Fonction pour enlever (amount) de PV +
    def takeDamage(self, amount):
        self.life -= amount
        self.__can.itemconfigure(self.__gauge, text = self.life)

    # Définition du timer
    def update(self, time):
        self.__timer += time
        # Tir toutes les 300 ms
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
                    entity.takeDamage(10)
                    if entity.life <= 0:
                        if entity == world.getVessel():
                            world.end = True
                        world.removeEntity(entity)
                    self.shoots.remove(shot)
                    return

            # Tir sort de l'écran
            x, y, w, h = self.__can.bbox(shot.shape)
            w -= x
            h -= y
            if x < 0 - w:
                self.shoots.remove(shot)
            if x > self.__can.winfo_width():
                self.shoots.remove(shot)
