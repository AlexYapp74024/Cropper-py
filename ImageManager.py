from Image import Image

from PySide6 import (
    QtWidgets as qtw, 
    QtGui as qtg, 
    QtCore as qtc
)
import cv2
import numpy as np

class Worker(qtc.QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @qtc.Slot()  # QtCore.Slot
    def run(self):
        self.fn(*self.args, **self.kwargs)

class ImageManager():
    def __init__(self) -> None:
        self.current_idx = 0
        self.images : list[Image] = []
        self.aspect_ratio = 1920/1080

        self.threadpool = qtc.QThreadPool()

    def open(self, paths = list[str]) -> None:
        opened = [i.path for i in self.images] 
        self.images += [Image(p) for p in paths if p not in opened]

    @property
    def current(self) -> Image:
        if self.not_loaded(): 
            return None
        return self.images[self.current_idx]

    def save(self, path:str = None):
        pix = self.current.cropped()
        byte:bytes = pix.toImage().constBits().tobytes()
        w,h = pix.size().toTuple()
        arr = np.frombuffer(byte, np.uint8)
        arr = arr.reshape(h,w,4)
        cv2.imwrite(path, arr)
        del pix

    def discard(self):
        del self.images[self.current_idx]

        if self.current_idx == len(self.images) and len(self.images) != 0:
            self.current_idx -= 1

    def not_loaded(self) -> bool: 
        return len(self.images) == 0
    
    def next(self) -> None:
        if self.current_idx < len(self.images) - 1: 
            self.current_idx += 1

    def prev(self) -> None:
        if self.current_idx > 0: 
            self.current_idx -= 1