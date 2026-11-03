from animation import AnimationControls
from PySide6 import QtCore, QtGui, QtWidgets
from src import RodneyState, WIDGET_SIZE
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
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground) TODO: uncomment this later

        screen = self.screen().availableGeometry()
        self.move(
            screen.right() - self.width(),
            screen.bottom() - self.height()
        )

        self.state = RodneyState.IDLE
        self.animcontrols = AnimationControls()

        self.clock = QtCore.QElapsedTimer()
        self.clock.start()

        self.fps_timer = QtCore.QTimer(self)
        self.fps_timer.timeout.connect(self._update_animation)
        self.fps_timer.start(1000 // FPS)

    def _update_animation(self):
        dt = self.clock.restart()
        self.animcontrols.update(dt)
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(
            QtGui.QPainter.RenderHint.SmoothPixmapTransform
        )
        self.animcontrols.render(painter)
        painter.end()