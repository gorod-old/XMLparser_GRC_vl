import sys

from PyQt5.QtWidgets import QApplication

from MessagePack import print_exception_msg
from app import MainWindow


def try_func(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print_exception_msg(msg=str(e))

    return wrapper


def start_app():
    marker = 'Выбор пути из проводника'
    app = QApplication(sys.argv)
    app_window = MainWindow(marker=marker)
    app_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    start_app()
