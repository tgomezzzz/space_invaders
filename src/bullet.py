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
        super().__init__(x, Y_POS, 8, 8, 0, 5, "red", win)
        self.ground = ground

    def move(self):
        if self.bottom() >= self.ground:
            return
        super().move()
