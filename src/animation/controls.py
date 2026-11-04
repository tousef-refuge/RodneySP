from PySide6 import QtCore, QtGui
from src import *
from .sprite import Sprite
import math
import random

# i thought id use this more gg
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

        neck = Sprite(NECK_X, NECK_Y, NECK_WIDTH, NECK_HEIGHT, NECK_OX, NECK_OY)
        neck.add_frames(ASSETS_DIR / "sprites" / "neck.png")
        self._sprites["neck"] = neck
        self.neck_angle = 0

        head = Sprite(HEAD_X, HEAD_Y, HEAD_WIDTH, HEAD_HEIGHT, HEAD_OX, HEAD_OY)
        head.add_frames(
            ASSETS_DIR / "sprites" / f"head_idle.png",
            ASSETS_DIR / "sprites" / f"head_blink.png",
            ASSETS_DIR / "sprites" / f"head_talk.png"
        )
        self._sprites["head"] = head
        self.neck_length = math.hypot(HEAD_X - HEAD_WIDTH * 0.5, HEAD_Y - HEAD_HEIGHT * 0.5)
        self.head_turn = 0

    def __getitem__(self, name):
        return self._sprites[name]

    def __setitem__(self, name, sprite):
        self._sprites[name] = sprite

    def play(self, state: RodneyState):
        self.state = state
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
            self._update(name, sprite)

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

        target = -HEAD_TILT_ANGLE if self.state == RodneyState.TALKING else 0
        self.head_turn = lerp(self.head_turn, target, 1.0 - math.exp(-HEAD_TILT_SPEED * dt))

    def _update(self, name, sprite):
        if name == "neck":
            sprite.rotation = NECK_BOB * math.sin(self.elapsed)
            self.neck_angle = sprite.rotation

        if name == "head":
            idx = 0 if self.state == RodneyState.IDLE else (2 if self.state == RodneyState.TALKING else 1)
            if self.is_blinking:
                idx = 1
            sprite.idx = idx

            pivot_x = NECK_X + NECK_WIDTH * NECK_OX
            pivot_y = NECK_Y + NECK_HEIGHT * NECK_OY

            dx = HEAD_X + HEAD_WIDTH * 0.5 - pivot_x
            dy = HEAD_Y + HEAD_HEIGHT * 0.5 - pivot_y

            angle = math.radians(self.neck_angle)
            cx = pivot_x + dx * math.cos(angle) - dy * math.sin(angle)
            cy = pivot_y + dx * math.sin(angle) + dy * math.cos(angle)

            sprite.x = cx - HEAD_WIDTH * 0.5
            sprite.y = cy - HEAD_HEIGHT * 0.5

            sprite.rotation = self.neck_angle + HEAD_ANGLE_OFFSET * math.cos(self.elapsed) + self.head_turn