import RPi.GPIO as GPIO
from time import sleep
from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=17, trigger=4, threshold_distance=0.2, max_distance=1)

GPIO.setwarnings(False)

# Right Motor
in1 = 18
in2 = 27
en_a = 4
# Left Motor
in3 = 5
in4 = 6
en_b = 13


GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en_a,GPIO.OUT)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en_b,GPIO.OUT)

q=GPIO.PWM(en_a,100)
p=GPIO.PWM(en_b,100)
p.start(75)
q.start(75)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)

# Wrap main content in a try block so we can  catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent the user seeing lots of unnecessary error messages.

try:
# Create Infinite loop to read user input
   while(True):
      # Get user Input

      # To see users input
      # print(user_input)

      ultrasonic.wait_for_out_of_range()
      GPIO.output(in1,GPIO.HIGH)
      GPIO.output(in2,GPIO.LOW)

      GPIO.output(in4,GPIO.HIGH)
      GPIO.output(in3,GPIO.LOW)

      print("Forward")

      # Press 'c' to exit the script
      ultrasonic.wait_for_in_range()
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.LOW)

      GPIO.output(in4,GPIO.LOW)
      GPIO.output(in3,GPIO.LOW)
      print('Stop')

# If user press CTRL-C
except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()
  print("GPIO Clean up")

