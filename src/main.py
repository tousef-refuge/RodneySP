from dotenv import load_dotenv
from PySide6 import QtWidgets

from src import ROOT
from .rodney import Rodney

import os
import signal
import sys

def main():
    os.environ["QT_LOGGING_RULES"] = "*.info=false;"
    load_dotenv(ROOT / ".env")
    app = QtWidgets.QApplication(sys.argv)
    rodney = Rodney()
    rodney.show()

    # noinspection PyUnusedLocal
    def handle_interrupt(sig, frame):
        rodney.close()
    signal.signal(signal.SIGINT, handle_interrupt)

    sys.exit(app.exec())