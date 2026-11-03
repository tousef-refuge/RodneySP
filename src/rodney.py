from animation import AnimationControls
from PySide6 import QtCore, QtGui, QtMultimedia, QtWidgets
from src import *
import os
FPS = 60

class Rodney(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(WIDGET_SIZE, WIDGET_SIZE)
        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowStaysOnTopHint |
            QtCore.Qt.WindowType.Tool
        )
        if os.getenv("SOLID_BG") != "true":
            self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        screen = self.screen().availableGeometry()
        self.move(
            screen.right() - self.width() + WIDGET_PADDING,
            screen.bottom() - self.height() + WIDGET_PADDING
        )

        self.output = QtMultimedia.QAudioOutput(self)
        self.audio_controls = QtMultimedia.QMediaPlayer(self)
        self.audio_controls.setAudioOutput(self.output)
        self.output.setVolume(AUDIO_VOLUME)

        self.state = RodneyState.IDLE
        self.anim_controls = AnimationControls()

        self.clock = QtCore.QElapsedTimer()
        self.clock.start()

        self.fps_timer = QtCore.QTimer(self)
        self.fps_timer.timeout.connect(self._update_animation)
        self.fps_timer.start(1000 // FPS)

    def _play_sound(self, path):
        self.audio_controls.setSource(QtCore.QUrl.fromLocalFile(path))
        self.audio_controls.play()

    def _update_animation(self):
        dt = self.clock.restart()
        self.anim_controls.update(dt)
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(
            QtGui.QPainter.RenderHint.SmoothPixmapTransform
        )
        self.anim_controls.render(painter)
        painter.end()