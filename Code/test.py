import buildhat_helper
import math

motor = buildhat_helper.Motor('A')

motor.set_motor_rotation(8.76 * math.pi)
motor.run_for_cm(-10, 10)