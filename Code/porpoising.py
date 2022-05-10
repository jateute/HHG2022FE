import buildhatHelper
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT) # status LED Green
GPIO.setup(23, GPIO.OUT) # status LED Red
GPIO.setup(24, GPIO.IN) # button


GPIO.output(22, GPIO.LOW)
GPIO.output(23, GPIO.HIGH)
motor_m = buildhatHelper.Driving_Motor('A')
motor_s = buildhatHelper.Steering_Motor('B')

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

while run <= 2:
    while corner <= 3:
        motor_m.run_for_rotations()
        motor_s.run_for_degrees(-50)
        motor_m.run_for_seconds(2)
        motor_s.run_for_degrees(50)
        corner += 1
        print(corner, 'corner')
    corner = 0
    run += 1
    print(run, 'run')

# Programm end
GPIO.cleanup()