from PySide6 import QtCore, QtGui
from animation import Animation
from src import RodneyState

class Sprite:
    def __init__(self, x, y, width, height, ox=0.5, oy=0.5):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.rotation = 0.0
        self.origin = QtCore.QPointF(ox, oy)

        self._animations: dict[RodneyState, Animation] = {}
        self.current_animation = None
        self.frame = 0

    # they could never make me hate you operation overloading
    def __getitem__(self, state: RodneyState):
        return self._animations[state]

    def __setitem__(self, state: RodneyState, animation):
        self._animations[state] = animation

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
