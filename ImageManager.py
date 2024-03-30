from Image import Image

class ImageManager():
    def __init__(self) -> None:
        self.current_idx = 0
        self.images : list[Image] = []

    def open(self, paths = list[str]) -> None:
        opened = [i.path for i in self.images]

        self.images += [Image(p) for p in paths if p not in opened]

    @property
    def current(self) -> Image:
        if self.not_loaded(): 
            return None
        return self.images[self.current_idx]

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
    