import buildhat

print('Init...')

motor_m = buildhat.Motor('A')
motor_s = buildhat.Motor('B')

print('Init finished\nStarting...')

motor_m.reverse()
motor_m.set_default_speed(40)
motor_s.set_default_speed(10)

corner = 0
run = 0

print('Start')

while run <= 3:
    while corner <= 4:
       # motor_s.run_for_degrees(-10)
       # motor_m.run_for_rotations(0.3)
       # motor_s.run_for_degrees(10)
        motor_m.run_for_seconds(3.3)
        motor_s.run_for_degrees(40)
        motor_m.run_for_seconds(1.7)
        motor_s.run_for_degrees(-40)
        corner += 1
        print(corner, 'corner')
    corner = 0
    run += 1
    print(run, 'run')
