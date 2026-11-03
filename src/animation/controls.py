from PySide6 import QtCore, QtGui
from src import ASSETS_DIR, RodneyState
from .sprite import Sprite

class AnimationControls(QtCore.QObject):
    finished = QtCore.Signal(str)

    def __init__(self):
        super().__init__()
        self.state = RodneyState.IDLE
        self._sprites = {}

        body = Sprite(0, 0, 100, 100)
        body.add_frames(ASSETS_DIR / "sprites" / "body.png")
        self._sprites["body"] = body

        neck = Sprite(0, 0, 100, 100)
        neck.add_frames(ASSETS_DIR / "sprites" / "neck.png")
        self._sprites["neck"] = neck

        head = Sprite(0, 0, 100, 100)
        head.add_frames(
            ASSETS_DIR / "sprites" / f"head_idle.png",
            ASSETS_DIR / "sprites" / f"head_blink.png",
            ASSETS_DIR / "sprites" / f"head_talk.png"
        )
        self._sprites["head"] = head

    def __getitem__(self, name):
        return self._sprites[name]

    def __setitem__(self, name, sprite):
        self._sprites[name] = sprite

    def play(self, state: RodneyState):
        for name, sprite in self._sprites.items():
            sprite.idx = 0
        self.state = state

    def render(self, painter: QtGui.QPainter):
        for name, sprite in self._sprites.items():
            sprite.render(painter)

    def update(self, dt):
        for name, sprite in self._sprites.items():
            self._update(name, sprite, dt)

    def _update(self, name, sprite, dt):
        pass # TODO: actually implement the animation here (oh boy)