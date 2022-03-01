from graphics import *
from swarm import *
from mothership import *
from alien import *
from player import *

class Level:
    def __init__(self, level_str, player, win):
        self.win = win
        if player == None:
            self.player = Player(self.win)
        else:
            self.player = player
        self.swarm = Swarm(level_str, self.win)
        self.alien_bullets = []
        self.player_bullets = []
        self.shield_bullets = []
        self.finished = False
        self.player_won = False
        self.win_message = Text(Point(self.win.getWidth() / 2, self.win.getHeight() / 2),  "Level cleared!")
        self.score = Text(Point(self.win.getWidth() / 2, 70 + self.win.getHeight() / 2), "")
        self.end_message = Text(Point(self.win.getWidth() / 2, 40 + self.win.getHeight() / 2),  "Click to continue.")
        self.mothership = None

    def run(self):
        while not self.finished:
            self.swarm.move()
            self.doMothership()
            self.moveBullets()

            self.alien_bullets += self.swarm.shoot()

            key = self.win.checkKey()
            if key == "Left":
                self.player.moveLeft()
            elif key == "Right":
                self.player.moveRight()
            elif key == "space":
                bullet = self.player.shoot()
                if bullet != None:
                    self.player_bullets.append(bullet)

            self.finished, self.player_won = self.checkAllCollisions()

            update(30)

        if not self.player_won:    
            self.win_message.setText("Better luck next time!")
            self.score.setText("Score: " + self.player.getScore())
            self.end_message.setText("Click to exit.")

        self.win_message.setSize(36)
        self.win_message.setTextColor("light green")
        self.win_message.draw(self.win)
        self.score.setSize(25)
        self.score.setTextColor("white")
        self.score.draw(self.win)
        self.end_message.setSize(20)
        self.end_message.setTextColor("white")
        self.end_message.draw(self.win)
        self.win.getMouse()
        self.endLevel()
        return self.player_won, self.player

    def moveBullets(self):
        for bullet in self.alien_bullets:
            bullet.move()
        for bullet in self.player_bullets:
            bullet.move()
        for bullet in self.shield_bullets:
            bullet.move()

    def hasMothership(self):
        return not self.mothership == None

    def doMothership(self):
        if self.hasMothership():
            if self.mothership.isDead():
                self.mothership = None
                return
            self.mothership.move()
        else:
            if randint(0, 500) < 1:
                self.mothership = Mothership(randint(0, 1), self.win)

    def checkAllCollisions(self):
        if self.checkAlienBulletCollisions() or self.checkPlayerCollisions():
            return True, False
        elif self.checkPlayerBulletCollisions():
            return True, True
        return False, False

    def checkAlienBulletCollisions(self):
        for bullet in self.alien_bullets:
            if bullet.isDead():
                continue
            if bullet.isColliding(self.player):
                killed = self.player.kill()
                bullet.kill()
                if killed:
                    return True

    def checkPlayerCollisions(self):
        found_collision, _ = self.swarm.checkCollisionWith(self.player)
        if found_collision:
            self.player.kill()
            return True

        for bullet in self.shield_bullets:
            if not bullet.isDead() and bullet.isColliding(self.player):
                bullet.kill()
                self.player.setShield()
                self.player.addScore(50)

    def checkPlayerBulletCollisions(self):
        for bullet in self.player_bullets:
            if bullet.isDead():
                continue

            if self.hasMothership():
                if bullet.isColliding(self.mothership):
                    self.mothership.kill()
                    bullet.kill()
                    self.shield_bullets.append(self.mothership.spawnShieldBullet(self.player.bottom()))
                    self.player.addScore(200)

            for alien_bullet in self.alien_bullets:
                if alien_bullet.isDead():
                    continue
                if bullet.isColliding(alien_bullet):
                    bullet.kill()
                    alien_bullet.kill()
                    self.player.addScore(50)

            for shield_bullet in self.shield_bullets:
                if shield_bullet.isDead():
                    continue
                if shield_bullet.isColliding(bullet):
                    bullet.kill()
                    shield_bullet.kill()
                    self.player.setShield()

            found_collision, collisions = self.swarm.checkCollisionWith(bullet)
            if found_collision:
                for collision in collisions:
                    self.player.addScore(100)
                    collision.kill()
                    bullet.kill()
                    death_attack = collision.deathAttack()
                    if not death_attack == None:
                        self.alien_bullets.append(death_attack)
                self.swarm.intensify(len(collisions))
        return self.swarm.isDead()

    def endLevel(self):
        self.swarm.clear()
        if not self.player_won:
            self.player.clear()
        self.win_message.undraw()
        self.end_message.undraw()
        self.score.undraw()
        if self.hasMothership():
            self.mothership.kill()
        for bullet in self.alien_bullets:
            bullet.kill()
        for bullet in self.player_bullets:
            bullet.kill()
        for bullet in self.shield_bullets:
            bullet.kill()
        del self.alien_bullets
        del self.player_bullets
        del self.shield_bullets
