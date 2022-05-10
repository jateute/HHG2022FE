import buildhat

class Motor(buildhat.Motor):
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
