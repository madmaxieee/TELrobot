from gpiozero import Servo


class Arm:
    def __init__(self) -> None:
        self.servos = [Servo()]
        pass