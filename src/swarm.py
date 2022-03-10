from alien import *
from random import randint

PADDING = 200
ALIEN_WIDTH = 67

LEFT_OFFSET = 48
RIGHT_OFFSET = -48
TOP_OFFSET = 100

class Swarm:
    def __init__(self, swarm_str, win):
        self.win = win
        self.swarm, self.size = self.buildSwarm(swarm_str)

        self.descend = False
        self.dir = 1
        self.speed = 0.5
        self.remaining_descent = 0
        self.bullet_chance = 1
        self.left = self.leftmost()
        self.right = self.rightmost()
        self.remaining = self.size

    def buildSwarm(self, swarm_str):
        size = 0
        j = 0
        rows = []
        for line in swarm_str.strip().split('\n'):
            aliens = line.strip().split(" ")
            count = len(aliens)
            space = (self.win.getWidth() - (2 * PADDING))
            x_spacing = space / count
            row_padding = (space - (x_spacing * (count - 1))) / 2
            row = []
            for i in range(count):
                size += 1
                x_pos = PADDING + row_padding + (i * x_spacing)
                y_pos = TOP_OFFSET + (j * 80)
                if aliens[i] == '0' or aliens[i] == 'b':
                    row.append(BlueAlien(x_pos, y_pos, self.win))
                elif aliens[i] == '1' or aliens[i] == 'g':
                    row.append(GreenAlien(x_pos, y_pos, self.win))
                elif aliens[i] == '2' or aliens[i] == 'o':
                    row.append(OrangeAlien(x_pos, y_pos, self.win))
            rows.append(row)
            j += 1
        return rows, size

    def setDescent(self):
        self.descend = True
        self.remaining_descent = 15

    def rightmost(self):
        ma = 0
        max_alien = None
        for row in self.swarm:
            for alien in row:
                if not alien.isDead() and alien.right() > ma:
                    ma = alien.right()
                    max_alien = alien
        return max_alien

    def leftmost(self):
        mi = self.win.getWidth()
        min_alien = None
        for row in self.swarm:
            for alien in row:
                if not alien.isDead() and alien.left() < mi:
                    mi = alien.right()
                    min_alien = alien
        return min_alien

    def move(self):
        if self.descend:
            for row in self.swarm:
                for alien in row:
                    alien.move(0, 1)
            self.remaining_descent -= 1
            if self.remaining_descent <= 0:
                self.descend = False
        else:
            if self.right.right() > self.win.getWidth() + RIGHT_OFFSET or self.left.left() < LEFT_OFFSET:
                self.dir *= -1
                self.setDescent()

            for row in self.swarm:
                for alien in row:
                    alien.move(self.dir * self.speed, 0)

    def shoot(self):
        new_bullets = []
        for row in self.swarm:
            for alien in row:
                if not alien.isDead():
                    if randint(0, 2000) < self.bullet_chance:
                        new_bullets += alien.shoot()
        return new_bullets

    def checkCollisionWith(self, entity):
        collisions = []
        for row in self.swarm:
            for alien in row:
                if alien.isDead():
                    continue
                if alien.isColliding(entity):
                    collisions.append(alien) 
        return len(collisions) > 0, collisions

    def intensify(self, strength):
        self.speed += 0.15 * strength
        self.remaining -= strength
        self.bullet_chance += 0.05 * (self.size - self.remaining)
        if self.remaining < self.size / 5:
            self.bullet_chance += 0.75
        if self.left.isDead():
            self.left = self.leftmost()
        if self.right.isDead():
            self.right = self.rightmost()

    def isDead(self):
        return self.remaining == 0

    def clear(self):
        for row in self.swarm:
            for alien in row:
                alien.kill()
        del self.swarm
