import buildhat

class Driving_Motor():
    __slots__ = ("_cm_per_rotation","_motor")

    def __init__(self, port : str):
        self._motor = buildhat.Motor(port)
        self._motor
        pass

    def set_motor_rotation(self, cm: float) -> None:
        self._cm_per_rotation = cm
        pass

    def start(self, speed: int = None) -> None:
        self._motor.start(speed)
        pass

    def stop(self) -> None:
        self._motor.stop()
        pass

    def set_default_speed(self, speed: int) -> None:
        self._motor.set_default_speed(speed)

    def run_for_cm(self, distance: float, speed: int=None, blocking: bool=True) -> None:
        rotations:float = distance / self.cm_per_rotation
        self._motor.run_for_rotations(rotations, speed, blocking)
        pass

    def run_for_seconds(self, seconds: float, speed: int, blocking: bool=True) -> None:
        self._motor.run_for_seconds(seconds,speed,blocking)
        pass

    def run_for_rotations(self, rotations: float, speed: int=None, blocking : bool=True) -> None:
        self._motor.run_for_rotations(rotations,speed,blocking)
        pass

    @property
    def cm_per_rotation(self) -> float:
        return self._cm_per_rotation

class Steering_Motor():
    __slots__ = ("upper_bound", "lower_bound","_target_degrees","_speed","_motor")
    def __init__(self, port : str, upper_bound : int, lower_bound : int):
        self._motor = buildhat.Motor(port)

        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        pass

    def run_to_position(self, degrees, speed=None, blocking=True):
        #degrees = min(max(degrees,self.lower_bound),self.upper_bound)

        self._motor.run_to_position(degrees,speed,blocking)
        pass
    
    def set_target_position(self, degrees, speed=None):
        self._target_degrees = degrees
        self._speed = speed
        pass

    def update(self):
        self._motor.run_to_position(self._target_degrees,self._speed,False)
        pass

    def set_default_speed(self, speed):
        self._motor.set_default_speed(speed)
        pass

    @property
    def target_degrees(self) -> int:
        return self._target_degrees
        pass

    @property
    def target_speed(self) -> int:
        return self._speed
        pass
    pass