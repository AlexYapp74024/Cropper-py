import sys
from PySide6 import (
    QtWidgets as qtw, 
    QtGui as qtg, 
    QtCore as qtc,
)
from Main.UI.Main_ui import Ui_MainWindow

class MainApp(qtw.QMainWindow, Ui_MainWindow):
    pixmap: qtg.QPixmap = None

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.scene = qtw.QGraphicsScene()
        self.gv_image.setScene(self.scene)

    def resizeEvent(self, event: qtg.QResizeEvent) -> None:
        if self.pixmap: self.set_pixmap(self.pixmap)
        print(self.gv_image.size())

    def set_pixmap(self, pixmap: qtg.QPixmap) -> None:
        self.scene.addPixmap(pixmap)
    
    def open_img(self, img_path: str) -> None:
        pixmap = qtg.QPixmap(img_path)
        self.set_pixmap(pixmap)