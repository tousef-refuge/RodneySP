from PySide6 import QtCore, QtGui
from src import *
from .sprite import Sprite
import random

def lerp(a, b, t):
    return a + (b - a) * t

class AnimationControls(QtCore.QObject):
    finished = QtCore.Signal(str)

    def __init__(self):
        super().__init__()
        self.state = RodneyState.IDLE
        self._sprites = {}

        self.elapsed = 0.0
        self.is_blinking = False
        self.blink_time = BLINK_TIME

        body = Sprite(BODY_X, BODY_Y, BODY_WIDTH, BODY_HEIGHT)
        body.add_frames(ASSETS_DIR / "sprites" / "body.png")
        self._sprites["body"] = body

        neck = Sprite(NECK_X, NECK_Y, NECK_WIDTH, NECK_HEIGHT)
        neck.add_frames(ASSETS_DIR / "sprites" / "neck.png")
        self._sprites["neck"] = neck

        head = Sprite(HEAD_X, HEAD_Y, HEAD_WIDTH, HEAD_HEIGHT)
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
        self.state = state
        self.elapsed = 0.0
        if state == RodneyState.ENTER or state == RodneyState.EXIT:
            self.is_blinking = True
            self.blink_time = BLINK_TIME

    def render(self, painter: QtGui.QPainter):
        for name, sprite in self._sprites.items():
            sprite.render(painter)

    def update(self, dt):
        if not self.is_blinking and not random.randrange(RANDOM_BLINK_CHANCE):
            self.is_blinking = True
            self.blink_time = BLINK_TIME

        # this guy is gonna stare at your soul while yapping
        self.is_blinking &= self.state != RodneyState.TALKING

        self.elapsed += dt
        for name, sprite in self._sprites.items():
            self._update(name, sprite, dt)

        # blinking sorta
        if self.is_blinking:
            self.blink_time -= dt
            if self.blink_time <= 0:
                self.is_blinking = False
                self.blink_time = BLINK_TIME

                if self.state == RodneyState.ENTER:
                    self.play(RodneyState.TALKING)

                if self.state == RodneyState.EXIT:
                    self.play(RodneyState.IDLE)

    def _update(self, name, sprite, dt):
        # TODO: actually ACTUALLY implement the animation here (oh boy)
        if name == "head":
            idx = 0 if self.state == RodneyState.IDLE else (2 if self.state == RodneyState.TALKING else 1)
            if self.is_blinking:
                idx = 1
            sprite.idx = idx