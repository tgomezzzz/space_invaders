# Space Invaders
Creative Embedded Systems Module 2

This game uses graphics.py. To install, run:
`pip3 install --user http://bit.ly/csc161graphics`

Space Invaders was a great way for me to use the hardware we learned about in this module. The game is almost always played with a joystick and a button, and I added the potentiometer to control the player's powerups. A C program constantly reads sensor data from the hardware, and sends it to the Space Invaders program via a serial port. The Space Invaders program contains a serial reader that reads the sensor data and uses it to control player movement, shooting, and ability usage. 
