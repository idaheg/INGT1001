#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
leftMotor = Motor(port=Port.A)
rightMotor = Motor(port=Port.D)
robot = DriveBase(leftMotor, rightMotor, wheel_diameter=49.6, axle_track=115)
touch_avpa = TouchSensor(port=Port.S4)
touch_left = TouchSensor(port=Port.S1)
touch_right = TouchSensor(port=Port.S3)
#ultra_s = UltrasonicSensor(port=Port.S2)
start = 0

# Write your program here.
#ultra_s.distance(silent=False) == 90

while True:
    if (start == 0 and touch_avpa.pressed()):   
        ev3.speaker.say("Excercise 2 with Katjakai and Bentebent")
        while (start == 0):
            robot.drive(80, 0)
            if (touch_left.pressed() or touch_right.pressed()):
                robot.stop()
                robot.straight(-100)
                robot.turn(90)
            if (touch_avpa.pressed()):
                start = 1
    elif (start == 1 and touch_avpa.pressed()):
        robot.stop()
        ev3.speaker.say("Excercise done")
        start = 0