from PySide6 import (
    QtWidgets as qtw, 
    QtGui as qtg, 
    QtCore as qtc,
)

class Image():
    def __init__(self, img_path) -> None:
        self.pixmap = qtg.QPixmap(img_path)
        self.scale : float = 1.0
        self.x : int = 0
        self.y : int = 0

    

    
        