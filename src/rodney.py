from PySide6 import QtCore, QtWidgets

class Rodney(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(400, 400)
        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowStaysOnTopHint |
            QtCore.Qt.WindowType.Tool
        )
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground) TODO: uncomment this later

        screen = self.screen().availableGeometry()
        self.move(
            screen.right() - self.width(),
            screen.bottom() - self.height()
        )