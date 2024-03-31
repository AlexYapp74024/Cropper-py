from __future__ import annotations
from functools import wraps

from PySide6 import (
    QtWidgets as qtw, 
    QtGui as qtg, 
    QtCore as qtc,
)
from Main.UI.Main_ui import Ui_MainWindow
from Image import Image
from ImageManager import ImageManager
from ImageCanvas import ImageCanvas
from numba import njit
from settings import settings

import pprint
import os

class MainApp(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.target_res = (1920, 1080)
        self.images = ImageManager()

        self.setupUi(self)
        self.aspect_ratio = 1920.0/1080

        self.cb_dimension.addItem("600 x 800")
        self.reset_scene()

        self.cb_useDefaultSavePath.setText("Save Path:" + settings["default_save_path"])
        self.pb_delete_ori.setChecked(settings["delete_original_image"])

        # assign controls
        self.sb_x.valueChanged.connect(self.sb_x_change)
        self.sb_y.valueChanged.connect(self.sb_y_change)
        self.sb_s.valueChanged.connect(self.sb_s_change)

        self.actionSave.triggered.connect(self.save)
        self.pb_save.clicked.connect(self.save)
        
        self.actionOpen.triggered.connect(self.open)
        self.pb_open.clicked.connect(self.open)

        self.pb_next.clicked.connect(self.next)
        self.pb_prev.clicked.connect(self.prev)

        self.pb_discard.clicked.connect(self.discard)
        self.actionDiscard.triggered.connect(self.discard)

        self.pb_rotate_clockwise.clicked.connect(self.rotate_90)
        self.actionRotate_Clockwise.triggered.connect(self.rotate_90)
        
        self.pb_rotate_counterClockwise.clicked.connect(self.rotate_270)
        self.actionRotate_Conter_Clockwise.triggered.connect(self.rotate_270)

        self.pb_flip_horizontal.clicked.connect(self.flip_horizontal)
        self.actionFlip_Horizontal.triggered.connect(self.flip_horizontal)
        
        self.pb_flip_vertical.clicked.connect(self.flip_vertical)
        self.actionFlip_Vertical.triggered.connect(self.flip_vertical)

        self.cb_dimension.currentTextChanged.connect(self.dim_change)

        self.pb_change_path.clicked.connect(self.change_save_path)  
        self.pb_delete_ori.clicked.connect(self.toggle_delete_ori)

    def _use_image(update=True):
        def func(foo, ):
            @wraps(foo)
            def magic(self: MainApp,*args,**kwargs):
                if self.image is None: 
                    return
                foo(self, *args,**kwargs)
                
                if update: self.update_image()

            return magic
        return func

    @property
    def image(self) -> Image:
        return self.images.current

    def toggle_delete_ori(self, _):
        settings["delete_original_image"] = self.pb_delete_ori.isChecked()
        self.save_settings()

    def change_save_path(self, _):
        file_name = qtw.QFileDialog()
        file_name.setFileMode(qtw.QFileDialog.FileMode.Directory)
        name = file_name.getExistingDirectory(self, "Select Directory")
        
        if name != '' : 
            settings["default_save_path"] = name
            self.save_settings()

    def save_settings(self):
        with open("settings.py", 'w') as f:
            out = pprint.pformat(settings, indent=4)
            f.write(f"settings = {out}")

    def dim_change(self, value:str) -> None:
        w,h = value.split(' x ')
        self.aspect_ratio = int(w)/int(h)

        # force a resize, to update layouts
        self.resize(self.size()*1.0001)

        if self.image is not None: 
            self.update_image()

    @_use_image()
    def flip_horizontal(self) -> None:
        self.image.flip_horizontal()
    
    @_use_image()
    def flip_vertical(self) -> None:
        self.image.flip_vertical()

    @_use_image()
    def rotate_270(self):
        self.image.rotate_270()
        self.set_spinner_bounds()

    @_use_image()
    def rotate_90(self):
        self.image.rotate_90()
        self.set_spinner_bounds()

    @_use_image()
    def prev(self):
        self.images.prev()
        self.set_spinner_bounds()

    @_use_image()
    def next(self):
        self.images.next()
        self.set_spinner_bounds()

    def open(self):
        file_name = qtw.QFileDialog()
        file_name.setFileMode(qtw.QFileDialog.FileMode.ExistingFiles)
        filter = "Image Files (*.png;, *.jpg; *.jpeg; *.jpe; *.jfif; *.exif;, *.bmp; *.dib; *.rle;, *.tiff *.tif;, *.gif;, *.tga;,*.dds;);"
        names , _ = file_name.getOpenFileNames(
            self,"Open Images", 
            settings["default_open_path"], 
            filter)
        
        if names == []: return
        settings["default_open_path"] = os.path.dirname(names[0])
        
        self.images.open(names)
        self.save_settings()
        self.update_image()
        self.set_spinner_bounds()

    @_use_image()
    def discard(self):
        if self.pb_delete_ori.isChecked():
            os.remove(self.image.path)
        self.images.discard()

        if self.image is None:
            self.reset_scene()
        self.set_spinner_bounds()

    @_use_image()
    def save(self):
        path = f"{settings['default_save_path']}/{os.path.basename(self.image.path)}"
        self.image.save(path)
        self.discard()

    @_use_image()
    def sb_x_change(self, a):
        self.image.x = a

    @_use_image()
    def sb_y_change(self, a): 
        self.image.y = a

    @_use_image()
    def sb_s_change(self, a): 
        self.image.scale = a
        self.set_spinner_bounds()

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

    def reset_scene(self):
        self.scene = ImageCanvas(self.images)
        def update_callback():
            self.update_image()
            self.sb_x.setValue(self.image.x)
            self.sb_y.setValue(self.image.y)

        self.scene.update_image = update_callback
        self.gv_image.setScene(self.scene)
        self.pixmap = self.scene.addPixmap(qtg.QPixmap())

    @_use_image(update=False)
    def update_image(self) -> None:
        w , h = self.gv_image.size().toTuple()
        pix = self.image.scaled_to_window_size(w, h)
        self.pixmap.setPixmap(pix)
    
    @_use_image()
    def set_spinner_bounds(self):
        self.image.calc_bounds()
        self.sb_x.setMaximum(self.image.x_max)
        self.sb_y.setMaximum(self.image.y_max)

