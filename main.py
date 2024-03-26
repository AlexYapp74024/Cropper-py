import sys
from PySide6 import (
    QtWidgets as qtw, 
    QtGui as qtg, 
    QtCore as qtc
)

from Main.Main import MainApp

if __name__ == "__main__":
    app = qtw.QApplication()
    window = MainApp()
    window.open_img("sample.png")
    window.show()
    sys.exit(app.exec())
