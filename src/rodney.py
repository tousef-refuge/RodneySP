from animation import AnimationControls
from PySide6 import QtCore, QtGui, QtMultimedia, QtWidgets
from src import *

import os
import random
import sys

IDLE_DIR = ASSETS_DIR / "audio" / "idle"
IDLE_VOICELINES = os.listdir(IDLE_DIR)

def idle_time():
    return int(IDLE_BASE_TIME * random.uniform(1 - IDLE_VARIANCE, 1 + IDLE_VARIANCE))

class Rodney(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.is_closing = False

        # window setup
        self.setFixedSize(WIDGET_SIZE, WIDGET_SIZE)
        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowStaysOnTopHint |
            QtCore.Qt.WindowType.Tool
        )
        if os.getenv("SOLID_BG") != "true":
            self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        screen = self.screen().availableGeometry()
        nx = screen.right() - self.width() + WIDGET_PADDING
        ny = screen.bottom() - self.height() + WIDGET_PADDING
        self.region = QtCore.QRect(nx, ny, self.width(), self.height())
        self.move(nx, ny)
        # if self.region.contains(QtGui.QCursor.pos()):

        # audio
        self.output = QtMultimedia.QAudioOutput(self)
        self.audio_controls = QtMultimedia.QMediaPlayer(self)
        self.audio_controls.setAudioOutput(self.output)
        self.audio_controls.mediaStatusChanged.connect(self._on_sound_end)
        self.output.setVolume(AUDIO_VOLUME)

        if os.getenv("PLAY_STARTOGG") != "false":
            self._play_sound(ASSETS_DIR / "audio" / "start.ogg")

        # animation
        self.clock = QtCore.QElapsedTimer()
        self.clock.start()

        self.anim_controls = AnimationControls()
        self.fps_timer = QtCore.QTimer(self)
        self.fps_timer.timeout.connect(self._update_animation)
        self.fps_timer.start(1000 // FPS)

        # idle timer
        self.idle_timer = QtCore.QTimer(self)
        self.idle_timer.setSingleShot(True)
        self.idle_timer.timeout.connect(self._on_idle_finish)
        self.idle_timer.start(max(idle_time(), MIN_START_TIME))

        # cursor timer
        self.cursor_timer = QtCore.QTimer(self)
        self.cursor_timer.timeout.connect(self._on_cursor_finish)
        self.cursor_timer.start(50)

        self.is_down = False
        self.original_pos = None

    def _play_sound(self, path):
        self.audio_controls.setSource(QtCore.QUrl.fromLocalFile(path))
        self.audio_controls.play()

    def _update_animation(self):
        dt = self.clock.restart()
        self.anim_controls.update(dt / 1000)
        self.update()

    def showEvent(self, event):
        super().showEvent(event)
        self.original_pos = self.pos()

    def paintEvent(self, event):
        if self.is_closing:
            return

        painter = QtGui.QPainter(self)
        painter.setRenderHint(
            QtGui.QPainter.RenderHint.SmoothPixmapTransform
        )
        self.anim_controls.render(painter)
        painter.end()

    def closeEvent(self, event):
        if self.is_closing:
            event.accept()
            return

        event.ignore()
        self.is_closing = True
        if os.getenv("PLAY_ENDOGG") != "false":
            self.audio_controls.mediaStatusChanged.connect(self._exit)
            self._play_sound(ASSETS_DIR / "audio" / "end.ogg")
        else:
            sys.exit(0)

    def _exit(self, status):
        if status == QtMultimedia.QMediaPlayer.MediaStatus.EndOfMedia:
            self.close()
            sys.exit(0)

    def _on_idle_finish(self):
        if self.is_closing:
            return

        self.anim_controls.play(RodneyState.ENTER)
        self._play_sound(IDLE_DIR / random.choice(IDLE_VOICELINES))

    def _on_cursor_finish(self):
        hovering = self.region.contains(QtGui.QCursor.pos())
        if hovering and not self.is_down:
            self.is_down = True
            self.move(self.original_pos + QtCore.QPoint(0, WIDGET_DOWN))

        elif not hovering and self.is_down:
            self.is_down = False
            self.move(self.original_pos)

    def _on_sound_end(self, status):
        if self.is_closing:
            return

        if status == QtMultimedia.QMediaPlayer.MediaStatus.EndOfMedia:
            self.idle_timer.start(idle_time())
            self.anim_controls.play(RodneyState.EXIT)