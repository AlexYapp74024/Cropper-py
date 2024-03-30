from PySide6 import (
    QtWidgets as qtw, 
    QtGui as qtg, 
    QtCore as qtc,
)

from ImageManager import ImageManager
from Image import Image

class ImageCanvas(qtw.QGraphicsScene):
    def __init__(self, image_manager: ImageManager):
        super().__init__()

        self.images = image_manager
        self.mouse_down = False
        self.down_pos: qtc.QPoint = None
        self.update_image = None

    @property
    def image(self) -> Image:
        return self.images.current
    
    def mousePressEvent(self, event: qtw.QGraphicsSceneMouseEvent) -> None:
        if event.button() == qtc.Qt.MouseButton.LeftButton and self.image is not None:
            self.mouse_down = True
            self.down_pos = event.scenePos()
            self.img_pos  = qtc.QPointF(self.image.x, self.image.y)

    def mouseReleaseEvent(self, event: qtw.QGraphicsSceneMouseEvent) -> None:
        if event.button() == qtc.Qt.MouseButton.LeftButton:
            self.mouse_down = False

    def mouseMoveEvent(self, event: qtw.QGraphicsSceneMouseEvent) -> None:
        if not self.mouse_down: return
        if self.image is None: return

        displacement = self.img_pos - event.scenePos() + self.down_pos
        x1, y1 = displacement.toTuple()
        self.image.x = x1
        self.image.y = y1
        self.update_image()
        

    