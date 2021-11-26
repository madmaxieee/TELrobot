from subsystems import base
from tel_image.findDoorCenter import findDoorCenter
class Stage:
    def __init__(self) -> None:
        self.isDone = False

    def start(self):
        print(f'{self.__class__.__name__} started')

    def loop(self):
        pass


class Stage1 (Stage):  # colored doors
    def start(self):
        super().start()

    def loop(self):
        pass

def test():
    stage1 = Stage1()
    stage1.start()

if __name__ == '__main__':
    test()
