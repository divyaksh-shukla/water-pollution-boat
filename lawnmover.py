from config import *
import datetime
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import DistanceSensor
import time

# Initialize global variables
ultrasonic = None

###############################################################################
# Boat Movement
###############################################################################
def move_forward():
    GPIO.output(R_MOTOR_1,GPIO.HIGH)
    GPIO.output(R_MOTOR_2,GPIO.LOW)

    GPIO.output(L_MOTOR_2,GPIO.HIGH)
    GPIO.output(L_MOTOR_1,GPIO.LOW)

def turn_right():
    starttime = datetime.datetime.now()
    while(datetime.datetime.now() - starttime < datetime.timedelta(milliseconds=RIGHT_TURN_MS)):
        GPIO.output(R_MOTOR_1,GPIO.LOW)
        GPIO.output(R_MOTOR_2,GPIO.HIGH)

        GPIO.output(L_MOTOR_2,GPIO.LOW)
        GPIO.output(L_MOTOR_1,GPIO.LOW)
    
def turn_left():
    starttime = datetime.datetime.now()
    while(datetime.datetime.now() - starttime < datetime.timedelta(milliseconds=LEFT_TURN_MS)):
        GPIO.output(R_MOTOR_1,GPIO.HIGH)
        GPIO.output(R_MOTOR_2,GPIO.LOW)

        GPIO.output(L_MOTOR_2,GPIO.LOW)
        GPIO.output(L_MOTOR_1,GPIO.LOW)
    
def move_back():
    GPIO.output(R_MOTOR_1,GPIO.LOW)
    GPIO.output(R_MOTOR_2,GPIO.HIGH)

    GPIO.output(L_MOTOR_2,GPIO.LOW)
    GPIO.output(L_MOTOR_1,GPIO.HIGH)

def stop():
    GPIO.output(R_MOTOR_1,GPIO.LOW)
    GPIO.output(R_MOTOR_2,GPIO.LOW)

    GPIO.output(L_MOTOR_2,GPIO.LOW)
    GPIO.output(L_MOTOR_1,GPIO.LOW)
    time.sleep(2)

###############################################################################
# UltraSonic sensor triggers
###############################################################################

def obstacle_detected():
    return False if (ultrasonic.distance < US_THRESHOLD) else True

def move_till_obstacle():
    while (not(obstacle_detected())):
        move_forward()
    return

def distance_covered():
    pass

def move_for_width(width):
    while (distance_covered() < width or not(obstacle_detected())):
        move_forward()
    return

def lawnmover(width_of_boat: int):
    while(True):
        move_till_obstacle()
        stop()
        turn_right()
        stop()
        move_for_width(width=width_of_boat)
        stop()
        turn_right()
        stop()
        move_till_obstacle()
        stop()
        turn_left()
        stop()
        move_for_width(width=width_of_boat)
        stop()
        turn_left()
        stop()

def setup_boat():
    ultrasonic = DistanceSensor(
        echo=US_ECHO, trigger=US_TRIGGER, 
        threshold_distance=US_THRESHOLD, max_distance=US_MAX_DISTANCE)

if __name__ == '__main__':
    setup_boat()
    lawnmover(width_of_boat=BOAT_WIDTH)