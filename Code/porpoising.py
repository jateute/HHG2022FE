import buildhat
import buildhatHelper
print('Init...')

motor_m = buildhatHelper.Motor('A')
motor_s = buildhatHelper.Motor('B')

print('Init finished\nStarting')

#motor_m.reverse()
motor_m.set_default_speed(40)
motor_s.set_default_speed(10)
motor_s.run_to_position(0, 10)
#motor_cd.set_motor_rotation(8.76 * math.pi, 'cm')


corner = 0
run = 0

print('Start')

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

