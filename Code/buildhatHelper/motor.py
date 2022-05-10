import buildhat

class Driving_Motor(buildhat.Motor):
    def set_motor_rotation(self, cm: float) -> None:
        self._cm_per_rotation = cm
        pass

    def run_for_cm(self, distance: float, speed: int=None, blocking: bool=True) -> None:
        rotations:float = distance / self.cm_per_rotation
        self.run_for_rotations(rotations, speed, blocking)
        pass

    @property
    def cm_per_rotation(self) -> float:
        return self._cm_per_rotation

class Steering_Motor(buildhat.Motor):
    __slots__ = ("upper_bound", "lower_bound")
    def __init__(self, port : str, upper_bound : int, lower_bound : int):
        super().__init__()

        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        pass

    def run_to_position(self, degrees, speed=None, blocking=True):
        degrees = min(max(degrees,self.lower_bound),self.upper_bound)

        super().run_to_position(degrees,speed,blocking)
        pass
    pass