from graphics import *
from level import *
from serial_reader import *

PORT = '/dev/cu.wchusbserial533C0037561'
BAUD = 115200
DATA = 'ascii'

def spaceInvaders():
    win = GraphWin("Space Invaders", 1200, 700, autoflush=False)
    win.setBackground("black")

    ser = SerialReader(PORT, BAUD, DATA)

    levels_file = open("levels.txt", "r")

    player_won = False
    player = None
    key = ""
    for level_str in levels_file.read().strip().split('$'):
        level = Level(level_str, player, ser, win)
        player_won, player, key = level.run()
        if not player_won:
            break

    if player_won:
        end = Text(Point(win.getWidth() / 2, win.getHeight() / 2),  "Thanks for playing Space Invaders!")
        end.setSize(36)
        end.setTextColor("light green")
        end.draw(win)

        score = Text(Point(win.getWidth() / 2,  40 + win.getHeight() / 2), "Score: " + player.getScore())
        score.setSize(30)
        score.draw(win)
        score.setTextColor("white")

        win.getKey()

    if key == "q":
        levels_file.close()
        win.close()
    elif key == "Return":
        levels_file.close()
        win.close()
        spaceInvaders()
        ser.kill()

spaceInvaders()  