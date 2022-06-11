import buildhat, buildhat_helper # 1 = Rot(Rechts); 2 = Grün (Links)
import RPi.GPIO as GPIO
import os
import serial
device:str  = ""

if os.name == 'nt':  # sys.platform == 'win32':
    from serial.tools.list_ports_windows import comports
elif os.name == 'posix':
    from serial.tools.list_ports_posix import comports
else:
    raise ImportError("Sorry: no implementation for your platform ('{}') available".format(os.name))

iterator = sorted(comports(False))
for n, (port, desc, hwid) in enumerate(iterator, 1):
    if desc.replace(f" ({port})", "") == "OpenMV Cam USB COM Port":
        device: str = port
    # OpenMV Cam USB COM Port

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN) # button


motor_m = buildhat_helper.Driving_Motor('A')
motor_s = buildhat_helper.Steering_Motor('B', 90, -90)

distance_sensor_f = buildhat.DistanceSensor('C')
distance_sensor_s = buildhat.DistanceSensor('D')

motor_m.set_default_speed(42)
motor_s.set_default_speed(10)
motor_s.run_to_position(0)

while GPIO.input(24) == 0:
    pass

distance_sensor_f.eyes(0, 0, 100, 100)
distance_sensor_s.eyes(100, 100, 0, 0)

def left() -> None:
    motor_s.run_to_position(90)
    motor_m.run_for_rotations(4, 42)
    motor_s.run_to_position(0)

def right() -> None:
    motor_s.run_to_position(-90)
    motor_m.run_for_rotations(4, 42)
    motor_s.run_to_position(0)

i = 0
if len(device) <= 0: raise RuntimeError('Couldn\'t find the openmv cam')
conn = serial.Serial(device)
print('Started connection with OpenMV Cam')
try:
    while i <= 12:
        motor_m.start(30)
        while distance_sensor_f.get_distance() > 600:
            data = conn.read_until('END\n'.encode('UTF-8')).decode('UTF-8').split('\n')
            try:
                data.pop('END')
            finally:
                pass
            try:
                data.pop('START')
            finally: 
                pass
            data.sort(key=lambda item: item['size'], reverse=True)
            if data[0] == 'BEGIN' or data[0] == 'END':
                pass
            if data[0]['type'] == '1': # Red
                if data[0]['rect'][1] < 160: # Left
                    if data[0]['rect'][1] + data[0]['rect'][3] < 50:
                        motor_s.run_to_position(0, 42)
                    else:
                        motor_s.run_to_position(30, 42)
                else: # Right
                    motor_s.run_to_position(60, 42)
            elif data[0]['type'] == '2': # Green
                if data[0]['rect'][1] < 160: #Left
                    motor_s.run_to_position(-60, 42)
                else:
                    if data[0]['rect'][1] + data[0]['rect'][3] < 270:
                        motor_s.run_to_position(0, 42)
                    else:
                        motor_s.run_to_position(30, 42)
        motor_m.stop()
        if distance_sensor_s.get_distance() == -1:
            right()
        else:
            left()
        i += 1
        print(i)
finally:
    print("Closing connection")
    if not conn.closed: conn.close()

GPIO.cleanup()