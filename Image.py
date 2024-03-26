from PySide6 import (
    QtWidgets as qtw, 
    QtGui as qtg, 
    QtCore as qtc,
)
import cv2
import numpy as np
import qimage2ndarray
from math import ceil
from numba import jit
class Image():
    def __init__(self, img_path:str, aspect_ratio:float = 1920.0/1080) -> None:
        self._ori_pixmap = qtg.QPixmap(img_path)
        self._pixmap = qtg.QPixmap(img_path)
        self._np = qimage2ndarray.imread(img_path)
        self.h, self.w = self._np.shape[:2]
        
        self._updated = True
        self.x : int = 0
        self.y : int = 0
        self.scale : float = 1.0
        self.aspect_ratio = aspect_ratio
    
    def pixmap(self) -> qtg.QPixmap:
        return self._pixmap

    def cropped_pixmap(self) -> qtg.QPixmap:
        if self._updated: 
            self._pixmap = self._ori_pixmap.scaledToWidth(
                self.w, 
                qtc.Qt.TransformationMode.SmoothTransformation
            )
            self._pixmap.scroll(0, 0, 0, 0, self.w, self.h)
            self._updated = False
        
        return self._pixmap
    

    
        