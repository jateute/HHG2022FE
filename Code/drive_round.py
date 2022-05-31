import buildhat, buildhat_helper
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT) # status LED Green
GPIO.setup(23, GPIO.OUT) # status LED Red
GPIO.setup(24, GPIO.IN) # button

GPIO.output(22, GPIO.LOW)
GPIO.output(23, GPIO.HIGH)

motor_m = buildhat_helper.Driving_Motor('A')
motor_s = buildhat_helper.Steering_Motor('B')

distance_sensor = buildhat.DistanceSensor('C')

print('Init finished\nStarting')

motor_m.set_default_speed(40)
motor_s.set_default_speed(10)
motor_s.run_to_position(0, 10)

corner = 0
run = 0

GPIO.output(23, GPIO.LOW)
GPIO.output(22, GPIO.HIGH)

while GPIO.input(24) == 0:
    pass

GPIO.output(23, GPIO.HIGH)
GPIO.output(22, GPIO.LOW)

motor_m.start(40)
time.sleep(100)
motor_m.stop