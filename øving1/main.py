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



# Write your program here.
ev3.speaker.beep()

ev3.screen.print("hello world!")
wait(1000)
#ev3.speaker.set_speech_options(language='no')
for i in range(4):
    robot.straight(200)
    robot.turn(90)
    ev3.speaker.beep()

ev3.screen.print("have a nice day!")
wait(1000)
ev3.speaker.say("have a nice day")


