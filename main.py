import sys
from controllers.DashBoard import DashBoard

def main():
    if len(sys.argv) == 1:
        dash = DashBoard()
        dash.start()
    elif len(sys.argv) > 1:
        if sys.argv[1] == 'auto':
            print('auto')


if __name__ == '__main__':
    main()
