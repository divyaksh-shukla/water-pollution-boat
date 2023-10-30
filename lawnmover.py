from config import *
import datetime
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import DistanceSensor
import time
import sys

GPIO.setmode(GPIO.BCM)

# Initialize global variables
ultrasonic = DistanceSensor(echo=US_ECHO, trigger=US_TRIGGER, threshold_distance=US_THRESHOLD, max_distance=US_MAX_DISTANCE)

###############################################################################
# Boat Movement
###############################################################################
def move_forward():
    GPIO.output(R_MOTOR_1,GPIO.LOW)
    GPIO.output(R_MOTOR_2,GPIO.HIGH)

    GPIO.output(L_MOTOR_1,GPIO.LOW)
    GPIO.output(L_MOTOR_2,GPIO.HIGH)

def turn_right():
    print('Turning right')
    starttime = datetime.datetime.now()
    while(datetime.datetime.now() - starttime < datetime.timedelta(milliseconds=RIGHT_TURN_MS)):
        GPIO.output(R_MOTOR_1,GPIO.HIGH)
        GPIO.output(R_MOTOR_2,GPIO.LOW)

        GPIO.output(L_MOTOR_1,GPIO.LOW)
        GPIO.output(L_MOTOR_2,GPIO.HIGH)
    
def turn_left():
    print('Turning left')
    starttime = datetime.datetime.now()
    while(datetime.datetime.now() - starttime < datetime.timedelta(milliseconds=LEFT_TURN_MS)):
        GPIO.output(R_MOTOR_1,GPIO.LOW)
        GPIO.output(R_MOTOR_2,GPIO.HIGH)

        GPIO.output(L_MOTOR_1,GPIO.HIGH)
        GPIO.output(L_MOTOR_2,GPIO.LOW)
    
def move_back():
    GPIO.output(R_MOTOR_1,GPIO.HIGH)
    GPIO.output(R_MOTOR_2,GPIO.LOW)

    GPIO.output(L_MOTOR_1,GPIO.HIGH)
    GPIO.output(L_MOTOR_2,GPIO.LOW)

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
    return ultrasonic.distance < US_THRESHOLD

def move_till_obstacle():
    print('moving forward')
    while (not(obstacle_detected())):
        sys.stdout.write("\r"+"Distance: "+str(ultrasonic.distance))
        sys.stdout.flush()
        move_forward()
    print('\nobstacle detected')
    return

def distance_covered():
    pass

def move_for_width(width):
    print('moving forward')
    starttime = datetime.datetime.now()
    while (datetime.datetime.now() - starttime < datetime.timedelta(milliseconds=BOAT_WIDTH_MS) and not(obstacle_detected())):
        sys.stdout.write("\r"+"Distance: "+str(ultrasonic.distance))
        sys.stdout.flush()
        move_forward()
    print('\nobstacle detected')
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
    time.sleep(2)

if __name__ == '__main__':
    try:
        # setup_boat()
        lawnmover(width_of_boat=BOAT_WIDTH)
    except Exception as e:
        #GPIO.cleanup()
        print('GPIO cleanup')
        raise e
    
