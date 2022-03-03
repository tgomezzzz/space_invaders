from graphics import *
from entity import *

Y_POS = 40

class Bullet(Entity):
    def __init__(self, x, y, w, h, x_dir, y_dir, color, win):
        super().__init__(x - w, y - h, w * 2, h * 2, win)
        self.rect = Rectangle(Point(x - w, y - h), Point(x + w, y + h))
        self.rect.setFill(color)
        self.rect.setOutline("")
        self.rect.draw(win)
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.is_dead = False

    def move(self):
        if self.top() > self.win.getHeight():
            self.kill()
        super().move(self.x_dir, self.y_dir)
        self.rect.move(self.x_dir, self.y_dir)

    def kill(self):
        super().kill()
        self.rect.undraw()

class ShieldBullet(Bullet):
    def __init__(self, x, ground, win):
        super().__init__(x, Y_POS, 8, 8, 0, 3, "red", win)
        self.ground = ground

    def move(self):
        if self.bottom() >= self.ground:
            return
        super().move()

class VerticalBurst(Bullet):
    def __init__(self, x, y, win):
        super().__init__(x, y, 8, 20, 0, -5, "cyan", win)
        self.rect.undraw()

    def move(self):
        if self.bottom() < 0:
            self.killTop()
        super().move()

    def moveWithPlayer(self, d_x):
        self.rect.move(d_x, 0)
        Entity.move(self, d_x, 0)

    def draw(self):
        self.rect.draw(self.win)

    def kill(self):
        pass

    def killTop(self):
        super().kill()