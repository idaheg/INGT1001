#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random
import time from time


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
leftMotor = Motor(port=Port.A)
rightMotor = Motor(port=Port.D)
robot = DriveBase(leftMotor, rightMotor, wheel_diameter=49.6, axle_track=115)
color_s = ColorSensor(port=Port.S2)
ultra_s = UltrasonicSensor(port=Port.S3)
touch_avpa = TouchSensor(port=Port.S4)
white_color = 0
black_color = 0
random_int = random.int(1, 4)
last_time = time.time()
sound = SoundFile()


# Write your program here.

def color_calibration():
    while not any(ev3.buttons.pressed()):
        continue
    wait (1000)
    white_color = color_s.reflection()
    ev3.speaker.beep()
    ev3.screen.print("white color: ", white_color)
    while not any(ev3.buttons.pressed()):
        continue
    wait (1000)
    black_color = color_s.reflection()
    ev3.speaker.beep()
    ev3.screen.print("black color: ", black_color)

def underholdning(tall):
    if (tall = 1):
        # underholdning nr 1
        wait(1000)
        ev3.speaker.Play(100, "Sounds/Cat Purr")
    elif (tall = 2):
        # underholdning nr 2
        ev3.screen.dizzy
        for i in range(4):
            robot.straight(50)
            robot.turn(90)
            ev3.speaker.beep()
    elif (tall = 3):
        # underholdning nr 3
        ev3.speaker.say("Skal jeg fortelle en vits? Katta med slips!")
        ev3.speaker.Play(100, "Sounds/Laughing 1") 
    else:


color_calibration()
BLACK = 3
WHITE = 62
treshold = (BLACK + WHITE)/2
DRIVE_SPEED = 100
    
while True:
    current_time = time.time()
    if color_s.reflection() < treshold:
        rightMotor.run(100)
        leftMotor.stop()
    else:
        leftMotor.run(100)
        rightMotor.stop()
    if (current_time - last_time >= 10):
        underholdning(random_int)
    if (ultra_s.distance() < 150):
        robot.stop()
        ev3.speaker.playSound(FANFARE)

