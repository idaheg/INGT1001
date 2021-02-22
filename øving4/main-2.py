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

ev3 = EV3Brick()
leftMotor = Motor(port=Port.A)
rightMotor = Motor(port=Port.D)
robot = DriveBase(leftMotor, rightMotor, wheel_diameter=49.6, axle_track=115)
knapp_venstre = TouchSensor(port=Port.S4)
knapp_hoyre = TouchSensor(port=Port.S3)
color_sensor_right = ColorSensor(port=Port.S1)
color_sensor_left = ColorSensor(port=Port.S2)

ev3.speaker.beep()
bane = 0
teller = 0
valg = True
while valg == True:
    # valg indre bane
    if (knapp_venstre.pressed()):
        bane = 1
        valg = False
        ev3.screen.print("indre bane")

    #valg ytre bane
    elif (knapp_hoyre.pressed()):
        valg = False
        ev3.screen.print("ytre bane")

ev3.speaker.beep()

loop = True
while loop:
    #indre bane
    if (bane == 1):
        ev3.screen.print("1")
        if (color_sensor_right.reflection() < 20):
            #sort linje
            leftMotor.run(500)
            rightMotor.run(200)
        else:
            #hvit sone
            rightMotor.run(500)
            leftMotor.run(200)

        if (color_sensor_left.reflection() < 20 and color_sensor_right.reflection() < 20):
            if (teller == 0):
                robot.stop()
                robot.turn(150)
                wait(5000)
                robot.turn(-150)
                robot.straight(100)
                robot.stop()
                teller = 1
            else:
                robot.straight(100)
                robot.stop()

            

    else:
        if (color_sensor_right.reflection() < 20):
            #sort linje
            leftMotor.run(500)
            rightMotor.run(200)
        else:
            #hvit sone
            rightMotor.run(500)
            leftMotor.run(200)
        if (color_sensor_left.reflection() < 20 and color_sensor_right.reflection() < 20):
            if (teller == 1):
                robot.stop()
                robot.turn(150)
                wait(5000)
                robot.turn(-150)
                robot.straight(100)
                robot.stop()
            else:
                robot.straight(100)
                robot.stop()
                teller = 1


    wait(4)
