import sys
from .rodney import Rodney
from PySide6 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    rodney = Rodney()
    rodney.show()
    sys.exit(app.exec())