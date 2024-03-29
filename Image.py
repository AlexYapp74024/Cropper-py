from PySide6 import (
    QtWidgets as qtw, 
    QtGui as qtg, 
    QtCore as qtc,
)

class Image():
    def __init__(self, img_path:str, aspect_ratio:float = 1920/1080) -> None:
        self.path = img_path
        self._ori_pixmap = qtg.QPixmap(img_path)
        self.w, self.h = self._ori_pixmap.size().toTuple()
        
        self.x : int = 0
        self.y : int = 0
        self.scale : float = 1.0
        self._aspect_ratio = aspect_ratio

    def img_size(self) -> qtc.QSize:
        return self._ori_pixmap.size()
    
    def save(self, name:str = None) -> None:
        if name is None:
            name = self.path

        res = self._ori_pixmap.copy(
            self.x,
            self.y,
            self.w / self.scale,
            self.w / self.scale / self._aspect_ratio
        ).save(name,'png')

        print(res)

    def calc_movement_margin(self) -> tuple[int]:
        size = self._ori_pixmap.size()
        iw, ih = size.toTuple()
        sw, sh = (size / self.scale).toTuple()
        if iw > ih * self._aspect_ratio:
            h = ih - sh
            w = iw - sh * self._aspect_ratio
        else:
            w = iw - sw
            h = ih - sw / self._aspect_ratio
        
        return int(w) , int(h)

    def scaled_to_window_size(self, width) -> qtg.QPixmap:
        # img_W = width * self.scale
        pixmap = self._ori_pixmap.copy(
            self.x,
            self.y,
            self.w / self.scale,
            self.w / self.scale / self._aspect_ratio
        ).scaledToWidth(
            width,
            qtc.Qt.TransformationMode.SmoothTransformation
        )

        return pixmap
    

    
        