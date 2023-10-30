import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

# Right Motor
R_MOTOR_1 = 18
R_MOTOR_2 = 27
R_EN_A = 4
# Left Motor
L_MOTOR_1 = 5
L_MOTOR_2 = 6
L_EN_B = 13


GPIO.setmode(GPIO.BCM)
GPIO.setup(R_MOTOR_1,GPIO.OUT)
GPIO.setup(R_MOTOR_2,GPIO.OUT)
GPIO.setup(R_EN_A,GPIO.OUT)

GPIO.setup(L_MOTOR_1,GPIO.OUT)
GPIO.setup(L_MOTOR_2,GPIO.OUT)
GPIO.setup(L_EN_B,GPIO.OUT)

q=GPIO.PWM(R_EN_A,100)
p=GPIO.PWM(L_EN_B,100)
p.start(75)
q.start(75)

GPIO.output(R_MOTOR_1,GPIO.LOW)
GPIO.output(R_MOTOR_2,GPIO.LOW)
GPIO.output(L_MOTOR_2,GPIO.LOW)
GPIO.output(L_MOTOR_1,GPIO.LOW)

# Wrap main content in a try block so we can  catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent the user seeing lots of unnecessary error messages.
try:
# Create Infinite loop to read user input
   while(True):
      # Get user Input
      user_input = input()

      # To see users input
      # print(user_input)

      if user_input == 'w':
         GPIO.output(R_MOTOR_1,GPIO.HIGH)
         GPIO.output(R_MOTOR_2,GPIO.LOW)

         GPIO.output(L_MOTOR_2,GPIO.HIGH)
         GPIO.output(L_MOTOR_1,GPIO.LOW)

         print("Forward")

      elif user_input == 's':
         GPIO.output(R_MOTOR_1,GPIO.LOW)
         GPIO.output(R_MOTOR_2,GPIO.HIGH)

         GPIO.output(L_MOTOR_2,GPIO.LOW)
         GPIO.output(L_MOTOR_1,GPIO.HIGH)
         print('Back')

      elif user_input == 'd':
         GPIO.output(R_MOTOR_1,GPIO.LOW)
         GPIO.output(R_MOTOR_2,GPIO.HIGH)

         GPIO.output(L_MOTOR_2,GPIO.LOW)
         GPIO.output(L_MOTOR_1,GPIO.LOW)
         print('Right')

      elif user_input == 'a':
         GPIO.output(R_MOTOR_1,GPIO.HIGH)
         GPIO.output(R_MOTOR_2,GPIO.LOW)

         GPIO.output(L_MOTOR_2,GPIO.LOW)
         GPIO.output(L_MOTOR_1,GPIO.LOW)
         print('Left')

      # Press 'c' to exit the script
      elif user_input == 'c':
         GPIO.output(R_MOTOR_1,GPIO.LOW)
         GPIO.output(R_MOTOR_2,GPIO.LOW)

         GPIO.output(L_MOTOR_2,GPIO.LOW)
         GPIO.output(L_MOTOR_1,GPIO.LOW)
         print('Stop')

# If user press CTRL-C
except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()
  print("GPIO Clean up")

