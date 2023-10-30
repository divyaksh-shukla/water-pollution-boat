from config import *
from gpiozero import DistanceSensor
import sys
import time

GPIO.setmode(GPIO.BCM)

# Initialize global variables
ultrasonic = DistanceSensor(echo=US_ECHO, trigger=US_TRIGGER, threshold_distance=US_THRESHOLD, max_distance=US_MAX_DISTANCE)

try:
	while(True):
		sys.stdout.write("\r"+"Distance: "+str(ultrasonic.distance))
		time.sleep(0.2)
		sys.stdout.flush()
except Exception as e:
	#GPIO.cleanup()
	raise e
#finally:
	#GPIO.cleanup()
print()
