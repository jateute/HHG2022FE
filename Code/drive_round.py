import buildhat, buildhat_helper # 1 = Rot(Rechts); 2 = Grün (Links)
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT) # status LED Green
GPIO.setup(23, GPIO.OUT) # status LED Red
GPIO.setup(24, GPIO.IN) # button

GPIO.output(22, GPIO.LOW)
GPIO.output(23, GPIO.HIGH)

motor_m = buildhat_helper.Driving_Motor('A')
motor_s = buildhat_helper.Steering_Motor('B', 90, -90)

distance_sensor_f = buildhat.DistanceSensor('C')
distance_sensor_s = buildhat.DistanceSensor('D')

motor_m.set_default_speed(40)
motor_s.set_default_speed(10)
motor_s.run_to_position(0)

GPIO.output(23, GPIO.LOW)
GPIO.output(22, GPIO.HIGH)

while GPIO.input(24) == 0:
    pass

distance_sensor_f.eyes(0, 0, 100, 100)
distance_sensor_s.eyes(100, 100, 0, 0)

GPIO.output(23, GPIO.HIGH)
GPIO.output(22, GPIO.LOW)
def left() -> None:
    motor_s.run_to_position(90)
    motor_m.run_for_rotations(4, 40)
    motor_s.run_to_position(0)

def right() -> None:
    motor_s.run_to_position(-90)
    motor_m.run_for_rotations(4, 40)
    motor_s.run_to_position(0)

i = 0
while i <= 12:
    motor_m.start(40)
    while distance_sensor_f.get_distance() > 600:
        pass
    motor_m.stop()
    if distance_sensor_s.get_distance() == -1:
        right()
    else:
        left()
    i += 1
    print(i)

GPIO.cleanup()