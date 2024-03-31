from Image import Image
import gc

QUEUE_SIZE = 3

class ImageManager():
    def __init__(self) -> None:
        self.current_idx = 0
        self.images : list[Image] = []
        self.aspect_ratio = 1920/1080
        
        self.queue = []

    def open(self, paths = list[str]) -> None:
        opened = [i.path for i in self.images] + self.queue
        self.queue += [p for p in paths if p not in opened]
        self._open(self.queue[:QUEUE_SIZE])
        del self.queue[:QUEUE_SIZE]

    def _open(self, paths = list[str]) -> None:
        self.images += [Image(p) for p in paths]

    @property
    def current(self) -> Image:
        if self.not_loaded(): 
            return None
        return self.images[self.current_idx]

    def discard(self):
        del self.images[self.current_idx]

        if self.current_idx == len(self.images) and len(self.images) != 0:
            self.current_idx -= 1

        if len(self.images) == 0 and len(self.queue) > 0:
            self.images = []
            self._open(self.queue[:QUEUE_SIZE])
            del self.queue[:QUEUE_SIZE]

    def not_loaded(self) -> bool: 
        return len(self.images) == 0
    
    def next(self) -> None:
        if self.current_idx < len(self.images) - 1: 
            self.current_idx += 1

    def prev(self) -> None:
        if self.current_idx > 0: 
            self.current_idx -= 1
    