import buildhat
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT) # status LED Green
GPIO.setup(23, GPIO.OUT) # status LED Red
GPIO.setup(24, GPIO.IN) # button

GPIO.output(23, GPIO.HIGH)

motor_m = buildhat.Motor('A')
motor_s = buildhat.Motor('B')

motor_m.reverse()
motor_m.set_default_speed(30)
motor_s.set_default_speed(10)

GPIO.output(23, GPIO.LOW)
GPIO.output(22, GPIO.HIGH)

while GPIO.input(24) == 0:
    pass

GPIO.output(23, GPIO.HIGH)
GPIO.output(22, GPIO.LOW)

motor_m.run_for_seconds(10)

# Programm end
GPIO.output(23, GPIO.LOW) 
GPIO.output(22, GPIO.HIGH)
GPIO.cleanup()