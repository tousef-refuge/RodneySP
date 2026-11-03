from PySide6 import QtCore, QtGui
from src import RodneyState

class AnimationControls(QtCore.QObject):
    finished = QtCore.Signal(str)

    def __init__(self):
        super().__init__()
        self._sprites = {}

    def __getitem__(self, name):
        return self._sprites[name]

    def __setitem__(self, name, sprite):
        self._sprites[name] = sprite

    def play(self, state: RodneyState):
        for name, sprite in self._sprites.items():
            sprite.current_animation = sprite[state]
            sprite.frame = 0

    def render(self, painter: QtGui.QPainter):
        for name, sprite in self._sprites.items():
            sprite.render(painter)

    def update(self, dt):
        for name, sprite in self._sprites.items():
            if sprite.current_animation is None:
                continue
            self._update(name, sprite, dt)

    def _update(self, name, sprite, dt):
        pass # TODO: actually implement the animation here (oh boy)