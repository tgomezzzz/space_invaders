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

class Powerup(Bullet):
    def __init__(self, x, y, w, h, x_dir, y_dir, color, win):
        super().__init__(x, y, w, h, x_dir, y_dir, color, win)
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

class VerticalBurst(Powerup):
    def __init__(self, x, y, win):
        super().__init__(x, y, 8, 20, 0, -5, "cyan", win)

class HorizontalBurst(Powerup):
    def __init__(self, x, y, x_dir, y_dir, do_burst, win):
        super().__init__(x, y, 8, 8, x_dir, y_dir, "light green", win)
        self.do_burst = do_burst
        if not self.do_burst:
            self.rect.draw(self.win)

    def move(self):
        if self.do_burst:
            if self.bottom() < 0:
                self.killTop()
        else:
            self.killSides()
        super().move()

    def kill(self):
        if self.do_burst:
            x = self.cX()
            y = self.top() - 10
            Bullet.kill(self)
            left = HorizontalBurst(x, y, -4, 0, False, self.win)
            right = HorizontalBurst(x, y, 4, 0, False, self.win)
            return [left, right]
    
    def killSides(self):
        if self.right() < 0 or self.left() > self.win.getWidth():
            super().kill()

class BombBurst(Powerup):
    def __init__(self, x, y, w, h, x_dir, y_dir, do_burst, win):
        super().__init__(x, y, w, h, x_dir, y_dir, "orange", win)
        self.do_burst = do_burst
        if not self.do_burst:
            self.rect.draw(self.win)

    def move(self):
        if self.do_burst:
            if self.bottom() < 0:
                self.killTop()
        else:
            self.killSides()
        super().move()

    def killSides(self):
        if self.right() < 0 or self.left() > self.win.getWidth() or self.bottom() < 0 or self.top() > self.win.getHeight():
            super().kill()

    def kill(self):
        if self.do_burst:
            x = self.cX()
            y = self.top() - 10
            Bullet.kill(self)
            top_left = BombBurst(x, y, 4, 4, -4, -4, False, self.win)
            top = BombBurst(x, y, 4, 4, 0, -4, False, self.win)
            top_right = BombBurst(x, y, 4, 4, 4, -4, False, self.win)
            left = BombBurst(x, y, 4, 4, -4, -0, False, self.win)
            right = BombBurst(x, y, 4, 4, 4, 0, False, self.win)
            bot_left = BombBurst(x, y, 4, 4, -4, 4, False, self.win)
            bot_right = BombBurst(x, y, 4, 4, 4, 4, False, self.win)
            return [top_left, top, top_right, left, right, bot_left, bot_right]
        else:
            Bullet.kill(self)

