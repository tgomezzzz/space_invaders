from graphics import *
from bullet import *
from random import randint

BLUE_ALIEN_PATH = "../images/blue_alien.png"
GREEN_ALIEN_PATH = "../images/green_alien.png"
ORANGE_ALIEN_PATH = "../images/orange_alien.png"
DEATH_PATH = "../images/explosion.png"

class Alien(Entity):
    def __init__(self, img_path, x, y, win):
        self.img = Image(Point(x, y), img_path)
        self.w = self.img.getWidth()
        self.h = self.img.getHeight()
        super().__init__(x - self.w / 2, y - self.h / 2, self.w, self.h, win)
        self.img.draw(self.win)

    def move(self, x_dir, y_dir):
        if self.isDead():
            return
        super().move(x_dir, y_dir)
        self.img.move(x_dir, y_dir)
    
    def pos(self):
        anchor = self.img.getAnchor()
        x = anchor.getX()
        y = anchor.getY() + self.h / 2
        return x, y

    def shoot(self):
        x, y = self.pos()
        b = Bullet(x, y, 4, 10, 0, 4, "blue", self.win)
        return [b]

    def kill(self):
        super().kill()
        self.img.undraw()
        anchor = self.img.getAnchor()
        self.img.undraw()

    def deathAttack(self):
        pass

class BlueAlien(Alien):
    def __init__(self, x, y, win):
        super().__init__(BLUE_ALIEN_PATH, x, y, win)

    def deathAttack(self):
        return Bullet(self.cX(), self.cY(), 12, 12, 0, 10, "light blue", self.win)

class GreenAlien(Alien):
    def __init__(self, x, y, win):
        super().__init__(GREEN_ALIEN_PATH, x, y, win)

    def shoot(self):
        x, y = self.pos()
        y_dir = randint(4, 8)
        b_left = Bullet(x, y, 4, 10, randint(-3, -1), y_dir, "green", self.win)
        b_down = Bullet(x, y, 4, 10, 0, y_dir, "green", self.win)
        b_right = Bullet(x, y, 4, 10, randint(1, 3), y_dir, "green", self.win)
        return [b_left, b_down, b_right]

class OrangeAlien(Alien):
    def __init__(self, x, y, win):
        super().__init__(ORANGE_ALIEN_PATH, x, y, win)

    def shoot(self):
        anchor = self.img.getAnchor()
        x, y = self.pos()
        b1 = Bullet(x, y, 4, 10, 0, 12, "orange", self.win)
        b2 = Bullet(x, y + 24, 4, 10, 0, 12, "orange", self.win)
        return [b1, b2]