from PySide6 import QtCore, QtGui

class Sprite:
    def __init__(self, x, y, width, height, ox=0.5, oy=0.5):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.rotation = 0.0
        self.origin = QtCore.QPointF(ox, oy)

        self.frames = []
        self.idx = 0

    def add_frames(self, *paths):
        frames = [QtGui.QPixmap(path) for path in paths]
        self.frames.extend(frames)

    def render(self, painter: QtGui.QPainter):
        painter.save()
        painter.translate(self.x, self.y)

        pivot_x = self.width * self.origin.x()
        pivot_y = self.height * self.origin.y()
        painter.translate(pivot_x, pivot_y)
        painter.rotate(self.rotation)

        image = self.frames[self.idx]
        painter.drawPixmap(int(-pivot_x), int(-pivot_y), int(self.width), int(self.height), image)
        painter.restore()
