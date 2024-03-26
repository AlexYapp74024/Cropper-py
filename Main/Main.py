import sys
from PySide6 import (
    QtWidgets as qtw, 
    QtGui as qtg, 
    QtCore as qtc,
)
from Main.UI.Main_ui import Ui_MainWindow
from Image import Image
from numba import jit, njit

class MainApp(qtw.QMainWindow, Ui_MainWindow):
    image:Image = None

    def __init__(self) -> None:
        self.target_res = (1920, 1080)

        super().__init__()
        self.setupUi(self)
        self.scene = qtw.QGraphicsScene()
        self.aspect_ratio = 1920.0/1080
        self.gv_image.setScene(self.scene)

    @staticmethod
    @njit
    def _calc_rect(fw:int, fh:int, aspect_ratio:float) -> tuple[int,int]:
        fw -= 2
        fh -= 2
        if fw > fh * aspect_ratio:
            w = fh*aspect_ratio
            h = fh
            x = (fw - w)/2
            y = 0
        else:
            w = fw
            h = fw/aspect_ratio
            x = 0
            y = (fh - h)/2

        return int(x), int(y), int(w), int(h)

    def resizeEvent(self, event: qtg.QResizeEvent) -> None:
        fw, fh = self.groupBox_gv.size().toTuple()
        x,y,w,h = self._calc_rect(fw, fh, self.aspect_ratio)
        self.gv_image.resize(w,h)
        self.gv_image.move(x,y) 
        self.update_image()

    def update_image(self) -> None:
        pix = self.image.cropped_pixmap()
        self.scene.addPixmap(pix)
    
    def open_img(self, img_path: str) -> None:
        self.image = Image(img_path)

