from graphics import *
from entity import *
from bullet import *

MOTHERSHIP_PATH = "../images/mothership.png"
WIDTH = 90
HEIGHT = 43
Y_POS = 40

class Mothership(Entity):
    def __init__(self, side, win):
        if side == 0:
            self.x = -WIDTH
            self.speed = 2
        else:
            self.x = win.getWidth() + WIDTH
            self.speed = -2
        self.img = Image(Point(self.x, Y_POS), MOTHERSHIP_PATH)
        super().__init__(self.x - self.img.getWidth() / 2, Y_POS - self.img.getHeight() / 2, self.img.getWidth(), self.img.getHeight(), win)
        self.img.draw(self.win)

    def move(self):
        if self.right() < -WIDTH or self.left() > self.win.getWidth() + WIDTH:
            self.kill()
            return

        super().move(self.speed, 0)
        self.img.move(self.speed, 0)

    def kill(self):
        super().kill()
        self.img.undraw()

    def spawnShieldBullet(self, bottom):
        return ShieldBullet(self.x + self.w / 2, bottom, self.win)
