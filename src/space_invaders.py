from graphics import *
from level import *

def spaceInvaders():
    win = GraphWin("Space Invaders", 1200, 700, autoflush=False)
    win.setBackground("black")

    levels_file = open("levels.txt", "r")

    player_won = False
    player = None
    for level_str in levels_file.read().strip().split('$'):
        level = Level(level_str, player, win)
        player_won, player = level.run()
        if not player_won:
            break

    if player_won:
        end = Text(Point(win.getWidth() / 2, win.getHeight() / 2),  "Thanks for playing Space Invaders!")
        end.setSize(36)
        end.setColor("light green")
        end.draw(win)

        score = Text(Point(win.getWidth() / 2,  40 + win.getHeight() / 2), "Score: " + player.getScore())
        score.setSize(30)
        score.draw(win)
        score.setColor("white")
        win.getMouse()
    
    levels_file.close()
    win.close()

spaceInvaders()  