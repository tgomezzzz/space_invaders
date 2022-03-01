class Entity:
    def __init__(self, x, y, w, h, win):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.win = win

        self.is_dead = False

    def cX(self):
        return self.x + self.w / 2

    def cY(self):
        return self.y + self.h / 2

    def left(self):
        return self.x

    def right(self):
        return self.x + self.w

    def top(self):
        return self.y
    
    def bottom(self):
        return self.y + self.h

    def width(self):
        return self.w

    def height(self):
        return self.h

    def isColliding(self, entity):
        return self.right() > entity.left() and self.left() < entity.right() and self.top() < entity.bottom() and self.bottom() > entity.top()

    def move(self, d_x, d_y):
        self.x += d_x
        self.y += d_y

    def kill(self):
        self.is_dead = True

    def isDead(self):
        return self.is_dead

    