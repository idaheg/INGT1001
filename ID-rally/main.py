#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#importerer time-funksjonen fra time-biblioteket
from time import time

ev3 = EV3Brick()

leftMotor = Motor(port=Port.A) 
rightMotor = Motor(port=Port.B) 
armMotor = Motor(port=Port.C, positive_direction=Direction.CLOCKWISE, gears=None)
robot = DriveBase(leftMotor, rightMotor, wheel_diameter=49.6, axle_track=127)
start_knapp = TouchSensor(port=Port.S4)
bord_sensor = ColorSensor(port=Port.S2)
panne_sensor = UltrasonicSensor(port=Port.S1)

def tableregistation():
    ev3.speaker.say("Tableedge registered. Try again")
    robot.drive(-100, 0)
    wait(1000)

# Write your program here.
ev3.speaker.beep()

# Trykk K1 for å starte
loop = True
while loop == True:
    if(start_knapp.pressed()):
        loop = False

# Roboten kjører frem til S1 måler riktig avstand til pannen til pasienten
start = True
rygge = True
start_time = time()
while start:
    robot.drive(100, 0)
    if (bord_sensor.reflection() < 1):
        robot.stop()
        start = False
        tableregistation()


    if (panne_sensor.distance() < 200): # Roboten stopper når avstandsmåleren registrerer pannen.
        end_time = time()
        
        robot.stop()
        ev3.speaker.say("Open your mouth, please.")
        wait(3000) # Roboten gir pasienten tid til å åpne munnen og kjøre sakte fremover
        robot.drive(60, 0)
        wait(1000)
        robot.turn(-20) 
        wait(500)
        armMotor.run_angle(100, 720) #Q-tipsen går opp en ned to gangen på den ene siden av munnen
        wait(1000)
        robot.turn(40)
        armMotor.run_angle(100, 720) #Q-tips sweiper igjen på andre siden
        wait(1000)
        robot.turn(-20) # tilbake til sentrum
        wait(500)
        robot.drive(-60, 0) # rygger sakte ut av munnen
        wait(1500)
        robot.stop()
        # "rygge tilbake til utgangspunktet" 
        time_return = time()
        while rygge:
            robot.drive(-100, 0)
            current_time = time()
            
            # Roboten rygger helt til den har brukt like lang tid tilbake som den brukte på å kjøre frem til pasienten
            if ((current_time - time_return) >= (end_time - start_time)):
                ev3.speaker.beep()
                robot.stop()
                start = False
                rygge = False
                ev3.speaker.say("Here is the test-pin")