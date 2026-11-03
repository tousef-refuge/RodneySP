from PySide6 import QtCore

class AnimationControls(QtCore.QObject):
    def __init__(self):
        super().__init__()

        self.clock = QtCore.QElapsedTimer()
        self.clock.start()

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(20)

        self._sprites = {}

    def __getitem__(self, name):
        return self._sprites[name]

    def __setitem__(self, name, sprite):
        self._sprites[name] = sprite

    def update(self):
        dt = self.clock.restart() / 1000.0
        for name, sprite in self._sprites.items():
            if sprite.current_animation is None:
                continue
            self._update(name, sprite, dt)

    def _update(self, name, sprite, dt):
        pass # TODO: actually implement the animation here (oh boy)