import pyxel as px
from graphics import Image


class MouseDrag:
    def __init__(self, movable_images: list[Image], clickable_images: list[Image]):
        self.movable_images = movable_images
        self.clickable_images = clickable_images
        self.dragged = None
        self.dx = 0
        self.dy = 0

    def find_overlapping(self) -> Image | None:
        for image in reversed(self.clickable_images + self.movable_images):
            dx = px.mouse_x - image.x
            dy = px.mouse_y - image.y
            if dx > 0 and dx < 16 and dy > 0 and dy < 16:
                self.dx = dx
                self.dy = dy
                return image

    def start_dragging(self) -> None:
        clicked_item = self.find_overlapping()
        if type(clicked_item) is Image:
            self.dragged = clicked_item
            self.move_to_back(self.dragged)

    def drag(self) -> None:
        assert self.dragged is not None
        self.dragged.x = px.mouse_x - self.dx
        self.dragged.y = px.mouse_y - self.dy

    def handle_click(self, button: int) -> None:
        if px.btn(button):
            if self.dragged is not None:
                self.drag()
            else:
                self.start_dragging()
        else:
            self.dragged = None

    def move_to_back(self, item: Image) -> None:
        self.movable_images.remove(item)
        self.movable_images.append(item)
