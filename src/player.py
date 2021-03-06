from graphics import *
from bullet import *
from entity import *
from shield import *

PLAYER_PATH = "../images/player.png"
DEATH_PATH = "../images/explosion.png"
GROUND = 50
POWERUP_KILLS = 4
POWERUP_COLORS = {"b": "cyan", "g": "light green", "o": "orange"}

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
        self.powerup = ["", 0]
        self.indicators = []
        self.ability = None

    def moveLeft(self, speed):
        if speed == None:
            speed = self.speed
        if self.left() - speed < 0:
            return
        self.moveShield(-speed)
        self.moveAbility(-speed)
        self.moveIndicators(-speed)
        self.score_text.move(-speed, 0)
        super().move(-speed, 0)
        self.img.move(-speed, 0)

    def moveRight(self, speed):
        if speed == None:
            speed = self.speed
        if self.right() + speed > self.win.getWidth():
            return
        self.moveShield(speed)
        self.moveAbility(speed)
        self.moveIndicators(speed)
        self.score_text.move(speed, 0)
        super().move(speed, 0)
        self.img.move(speed, 0)

    def moveShield(self, d_x):
        if self.hasShield():
            self.shield.move(d_x, 0)

    def moveAbility(self, d_x):
        if self.hasAbility():
            self.ability.moveWithPlayer(d_x)

    def moveIndicators(self, d_x):
        for i in self.indicators:
            i.move(d_x, 0)

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
        return Bullet(x, y, 4, 10, 0, -4, "white", self.win)

    def doPowerup(self, alien):
        if alien == self.powerup[0] or self.powerup[0] == "":
            self.powerup[0] = alien
            if self.powerup[1] < POWERUP_KILLS:
                self.powerup[1] += 1
                self.addIndicator(alien)
            if self.powerup[1] >= POWERUP_KILLS:
                self.setAbility(alien)
        elif not self.hasAbility():
            self.clearIndicators()
            self.powerup = [alien, 1]
            self.addIndicator(alien)

    def setAbility(self, alien):
        if self.hasAbility():
            return
        if alien == "b":
            self.ability = VerticalBurst(self.cX(), self.top(), self.win)
        elif alien == "g":
            self.ability = HorizontalBurst(self.cX(), self.top(), 0, -4, True, self.win)
        elif alien == "o":
            self.ability = BombBurst(self.cX(), self.top(), 10, 10, 0, -4, True, self.win)

    def useAbility(self):
        self.ability.draw()
        ret = self.ability
        self.ability = None
        self.powerup = ["", 0]
        self.clearIndicators()
        return ret

    def hasAbility(self):
        return not self.ability == None

    def addIndicator(self, alien):
        pos = len(self.indicators)
        gap = 3
        width = ((self.w + gap) / (POWERUP_KILLS)) - gap
        offset = gap + width
        x = self.left() + (offset * pos)
        indicator = Rectangle(Point(x, self.bottom() + 4), Point(x + width, self.bottom()))
        indicator.setOutline("")
        indicator.setFill(POWERUP_COLORS[alien])
        indicator.draw(self.win)
        self.indicators.append(indicator)

    def clearIndicators(self):
        for i in self.indicators:
            i.undraw()
        self.indicators = []

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
        self.clearIndicators()
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

