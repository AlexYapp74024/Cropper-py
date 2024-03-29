from PySide6 import (
    QtWidgets as qtw, 
    QtGui as qtg, 
    QtCore as qtc,
)
import cv2
import numpy as np
import qimage2ndarray
from math import ceil
from numba import njit

class Image():
    def __init__(self, img_path:str, aspect_ratio:float = 1920.0/1080) -> None:
        self._ori_pixmap = qtg.QPixmap(img_path)
        # self._np = qimage2ndarray.imread(img_path)
        self.h, self.w = self._np.shape[:2]
        
        self.x : int = 0
        self.y : int = 0
        self.scale : float = 1.0
        self.aspect_ratio = aspect_ratio
        
        self._updated = True

    def img_size(self) -> qtc.QSize:
        return self._ori_pixmap.size()
    
    @staticmethod
    @njit
    def _calc_movement_margin(iw, ih, aspect_ratio) -> tuple[int]:
        if iw > ih * aspect_ratio:
            w = iw - ih * aspect_ratio
            w = int(w)
            h = 0
        else:
            w = 0
            h = ih - iw / aspect_ratio
            h = int(h)
        
        return w , h

    def calc_movement_margin(self) -> tuple[int]:
        iw, ih = self._ori_pixmap.size().toTuple()
        if iw > ih * self.aspect_ratio:
            w = iw - ih * self.aspect_ratio
            w = int(w)
            h = 0
        else:
            w = 0
            h = ih - iw / self.aspect_ratio
            h = int(h)
        
        return w , h

    def scaled_to_window_size(self, width) -> qtg.QPixmap:
        # img_W = width * self.scale
        _pixmap = self._ori_pixmap.copy(
            self.x,
            self.y,
            self.w / self.scale,
            self.h / self.scale
        ).scaledToWidth(
            width,
            qtc.Qt.TransformationMode.SmoothTransformation
        )

        return _pixmap
    

    
        