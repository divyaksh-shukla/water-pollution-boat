import RPi.GPIO as GPIO

# Right Motor
R_MOTOR_1 = 18
R_MOTOR_2 = 27
R_EN_A = 4
# Left Motor
L_MOTOR_1 = 5
L_MOTOR_2 = 6
L_EN_B = 13

RIGHT_TURN_MS = 4000 # 4s # To be calibrated
LEFT_TURN_MS = 4000 # 4s # To be calibrated

# Ultrasonic Sensor
US_ECHO = 17
US_TRIGGER = 4
US_THRESHOLD = 0.2 # to be increased to max(length_boat, width_boat) in meters
US_MAX_DISTANCE = 1 # to be increased to max(length_boat, width_boat)*1.5 in meters

# Boat Dimensions
BOAT_WIDTH = 0.1
BOAT_HEIGHT = 0.1
BOAT_LENGTH = 0.15

# Setup the GPIO pins

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
GPIO.output(L_MOTOR_1,GPIO.LOW)
GPIO.output(L_MOTOR_2,GPIO.LOW)