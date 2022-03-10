# Space Invaders
### Creative Embedded Systems Module 2
![Cover Image](https://github.com/tgomezzzz/space_invaders/blob/main/images/space_invaders2.png)

This game uses graphics.py. To install, run:
`pip3 install --user http://bit.ly/csc161graphics`  
  
To run the game, navigate to the src/ directory, and run: `python3 space_invaders.py`

Space Invaders was a great way for me to use the hardware we learned about in this module. The game is almost always played with a joystick and a button, and I added the potentiometer to control the player's powerups. A C program constantly reads sensor data from the hardware, and sends it to the Space Invaders program via a serial port. The Space Invaders program contains a serial reader that reads the sensor data and uses it to control player movement, shooting, and ability usage.

![More Gameplay](https://github.com/tgomezzzz/space_invaders/blob/main/images/space_invaders1.png)

Designing the controller was a process of trial and error. I chose a layout similar to gaming console controllers, with the joystick on the left, the button on the right, but I added the potentiometer in the middle. The hardware is held in place with a cardboard cover, while a hollowed block of styrofoam holds the wiring in place. The ESP32 rests at the bottom of the styrofoam block, and a port in the side allows it to connect to the machine running Space Invaders via a wire.

![Hardware Container](https://github.com/tgomezzzz/space_invaders/blob/main/images/container.jpg)
