from graphics import *
from entity import *

RADIUS = 96/ 2
HEIGHT = 27

class Shield(Entity):
    def __init__(self, x, y, win):
        super().__init__(x - RADIUS, y - HEIGHT, RADIUS * 2, HEIGHT, win)
        self.poly = Polygon(Point(x - RADIUS, y), Point(x - (RADIUS / 2), y - HEIGHT), Point(x + (RADIUS / 2), y - HEIGHT), Point(x + RADIUS, y), \
                            Point(x + RADIUS - 4, y + 4), Point(x + (RADIUS / 2) - 4, y - HEIGHT + 4), Point(x - (RADIUS / 2) + 4, y - HEIGHT + 4), Point(x - RADIUS + 4, y + 4))
        self.poly.setFill("red")
        self.poly.setOutline("")
        self.poly.draw(self.win)

    def move(self, x, y):
        super().move(x, y)
        self.poly.move(x, y)

    def kill(self):
        super().kill()
        self.poly.undraw()
