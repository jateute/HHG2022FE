import buildhatHelper
import math

motor = buildhatHelper.Motor('A')

motor.set_motor_rotation(8.76 * math.pi)
motor.run_for_cm(-10, 10)