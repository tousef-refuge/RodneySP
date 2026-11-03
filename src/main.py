import sys
from dotenv import load_dotenv
from PySide6 import QtWidgets

from src import ROOT
from .rodney import Rodney

def main():
    load_dotenv(ROOT / ".env")
    app = QtWidgets.QApplication(sys.argv)
    rodney = Rodney()
    rodney.show()
    sys.exit(app.exec())