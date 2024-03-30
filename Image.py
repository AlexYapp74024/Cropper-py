from PySide6 import (
    QtWidgets as qtw, 
    QtGui as qtg, 
    QtCore as qtc,
)

class Image():
    def __init__(self, img_path:str, aspect_ratio:float = 1920/1080) -> None:
        self.path = img_path
        self._ori_pixmap = None

        self._x : float = 0.0
        self._y : float = 0.0
        self.angle : int = 0 # In Multiples of 90
        self._scale : float = 1.0
        
        self.x_max : int = 0
        self.y_max : int = 0

        self._aspect_ratio = aspect_ratio

    @property
    def ori_pixmap(self) -> qtg.QPixmap:
        if self._ori_pixmap is None:
            self._ori_pixmap = qtg.QPixmap(self.path)
            self._w, self._h = self.ori_pixmap.size().toTuple()
        return self._ori_pixmap
    
    @ori_pixmap.setter
    def ori_pixmap(self, value):
        self._ori_pixmap = value

    @property
    def aspect_ratio(self) -> float:
        if (self.angle % 2):
            return 1 / self._aspect_ratio
        else:
            return self._aspect_ratio
        
    @aspect_ratio.setter
    def aspect_ratio(self, value) -> float:
        self._aspect_ratio = value
        self.calc_bounds()

    @property
    def w(self):
        self.ori_pixmap
        return self._w
    
    @property
    def h(self):
        self.ori_pixmap
        return self._h

    @property
    def x(self): return self._x

    @property
    def y(self): return self._y

    @property
    def scale(self): return self._scale
    
    def bounds_check(self) -> None:
        if self._x < 0: self._x = 0
        if self._x > self.x_max: self._x = self.x_max
        if self._y < 0: self._y = 0
        if self._y > self.y_max: self._y = self.y_max

    @x.setter
    def x(self, value):
        self._x = value
        if self._x < 0: self._x = 0
        if self._x > self.x_max: self._x = self.x_max

    @y.setter
    def y(self, value):
        self._y = value
        if self._y < 0: self._y = 0
        if self._y > self.y_max: self._y = self.y_max

    @scale.setter
    def scale(self, value): 
        self._scale = value
        self.calc_bounds()

    def img_size(self) -> qtc.QSize:
        return self.ori_pixmap.size()

    def flip_horizontal(self) -> None:
        self.ori_pixmap = self.ori_pixmap.transformed(
            qtg.QTransform().scale(-1,1), 
            qtc.Qt.TransformationMode.SmoothTransformation
        )
        self._x = self.x_max - self._x
    
    def flip_vertical(self) -> None:
        self.ori_pixmap = self.ori_pixmap.transformed(
            qtg.QTransform().scale(1,-1), 
            qtc.Qt.TransformationMode.SmoothTransformation
        )
        self._y = self.y_max - self._y

    def rotate_90(self) -> None:
        self.ori_pixmap = self.ori_pixmap.transformed(
            qtg.QTransform().rotate(-90), 
            qtc.Qt.TransformationMode.SmoothTransformation
        )
        self.calc_bounds()

    def rotate_270(self) -> None:
        self.ori_pixmap = self.ori_pixmap.transformed(
            qtg.QTransform().rotate(-90), 
            qtc.Qt.TransformationMode.SmoothTransformation
        )
        self.calc_bounds()

    def save(self, name:str = None) -> bool:
        if name is None:
            name = self.path

        iw, ih = self.ori_pixmap.size().toTuple()
        if iw > ih * self.aspect_ratio:
            return self.ori_pixmap.copy(
                int(self._x),
                int(self._y),
                self.h / self._scale * self.aspect_ratio,
                self.h / self._scale
            ).save(name,'png')
        else:  
            return self.ori_pixmap.copy(
                int(self._x),
                int(self._y),
                self.w / self._scale,
                self.w / self._scale / self.aspect_ratio
            ).save(name,'png')

    def calc_bounds(self):
        size = self.ori_pixmap.size()
        iw, ih = size.toTuple()
        sw, sh = (size / self._scale).toTuple()
        ar = self.aspect_ratio

        if iw > ih * ar:
            h = ih - sh
            w = iw - sh * ar
        else:
            w = iw - sw
            h = ih - sw / ar

        self.x_max = int(w)
        self.y_max = int(h)
        self.bounds_check()

    def scaled_to_window_size(self, width, height) -> qtg.QPixmap:
        iw, ih = self.ori_pixmap.size().toTuple() 

        if iw > ih * self.aspect_ratio:
            return self.ori_pixmap.copy(
                int(self._x),
                int(self._y),
                self.h / self._scale * self.aspect_ratio,
                self.h / self._scale
            ).scaledToHeight(
                height,
                qtc.Qt.TransformationMode.SmoothTransformation
            )
        else:
            return self.ori_pixmap.copy(
                int(self._x),
                int(self._y),
                self.w / self._scale,
                self.w / self._scale / self.aspect_ratio
            ).scaledToWidth(
                width,
                qtc.Qt.TransformationMode.SmoothTransformation
            )
    

    
        