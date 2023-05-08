# Main window, open executable file, GUI = view.py Methods = controller.py
from controller import *


def main():
    application = QApplication([])
    window = Controller()
    window.show()
    application.exec_()


if __name__ == '__main__':
    main()