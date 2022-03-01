from graphics import *
from bullet import *
from entity import *
from shield import *

PLAYER_PATH = "../images/player.png"
DEATH_PATH = "../images/explosion.png"
GROUND = 50

class Player(Entity):
    def __init__(self, win):
        self.img = Image(Point(win.getWidth() / 2, win.getHeight() - 50), PLAYER_PATH)
        self.w = self.img.getWidth()
        self.h = self.img.getHeight()
        super().__init__(win.getWidth() / 2 - self.w / 2, win.getHeight() - GROUND - self.h / 2, self.w, self.h, win)
        self.img.draw(self.win)
        self.speed = 20
        self.shield = None
        self.score = 0
        self.score_text = Text(Point(self.cX(), self.cY() + 6), str(self.score))
        self.score_text.setSize(15)
        self.score_text.setTextColor("black")
        self.score_text.draw(self.win)

    def moveLeft(self):
        if self.left() - self.speed < 0:
            return
        self.moveShield(-self.speed)
        self.score_text.move(-self.speed, 0)
        super().move(-self.speed, 0)
        self.img.move(-self.speed, 0)

    def moveRight(self):
        if self.right() + self.speed > self.win.getWidth():
            return
        self.moveShield(self.speed)
        self.score_text.move(self.speed, 0)
        super().move(self.speed, 0)
        self.img.move(self.speed, 0)

    def moveShield(self, d_x):
        if self.hasShield():
            self.shield.move(d_x, 0)

    def hasShield(self):
        return not self.shield == None

    def setShield(self):
        if self.hasShield():
            return
        self.shield = Shield(self.cX(), self.cY(), self.win)

    def shoot(self):
        anchor = self.img.getAnchor()
        x = anchor.getX()
        y = anchor.getY() - self.img.getHeight() / 2
        return Bullet(x, y, 4, 10, 0, -7, "white", self.win)

    def addScore(self, inc):
        self.score += inc
        self.score_text.setText(str(self.score))

    def getScore(self):
        return str(self.score)

    def kill(self):
        if self.hasShield():
            self.shield.kill()
            self.shield = None
            return False
        super().kill()
        anchor = self.img.getAnchor()
        self.img.undraw()
        self.score_text.undraw()
        self.img = Image(anchor, DEATH_PATH)
        self.img.draw(self.win)
        return True

    def clear(self):
        self.img.undraw()
        if self.hasShield():
            self.shield.kill()

