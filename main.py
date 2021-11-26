import sys
from controllers.DashBoard import DashBoard
from auto import Auto
from subsystems import base

def main():
    if len(sys.argv) == 1:
        dash = DashBoard()
        dash.start()
    elif len(sys.argv) > 1:
        if sys.argv[1] == 'auto':
            a = Auto()
            a.start()
        elif sys.argv[1] == 'clean':
            base.clearDriveSpeeds()
            exit()

if __name__ == '__main__':
    main()
