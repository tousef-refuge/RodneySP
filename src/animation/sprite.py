from PySide6 import QtCore, QtGui

class Sprite:
    def __init__(self, x, y, width, height, ox=0.5, oy=0.5):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.rotation = 0.0
        self.origin = QtCore.QPointF(ox, oy)

        self._animations = {}
        self.current_animation = None
        self.frame = 0

    # they could never make me hate you operation overloading
    def __getitem__(self, name):
        return self._animations[name]

    def __setitem__(self, name, animation):
        self._animations[name] = animation

    def render(self, painter: QtGui.QPainter):
        if not self.current_animation:
            return

        image = self.current_animation.frames[self.frame]
        painter.save()
        painter.translate(self.x, self.y)

        pivot_x = self.width * self.origin.x()
        pivot_y = self.height * self.origin.y()
        painter.translate(pivot_x, pivot_y)
        painter.rotate(self.rotation)

        painter.drawPixmap(int(-pivot_x), int(-pivot_y), int(self.width), int(self.height), image)
        painter.restore()
