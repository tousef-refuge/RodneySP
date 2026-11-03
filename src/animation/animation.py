from PySide6 import QtGui

class Animation:
    def __init__(self, paths: list[str]):
        self.frames = [QtGui.QPixmap(path) for path in paths]
