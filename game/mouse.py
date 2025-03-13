import pyxel as px
from graphics import Image
from drawer import InfiniteIngredient


class MouseDrag:
    def __init__(self, clickable_images: list[Image], displayable_images: list[Image]):
        self.clickable_images = clickable_images
        self.displayable_images = displayable_images
        self.dragged = None
        self.dx = 0
        self.dy = 0

    def find_overlapping(self) -> Image | InfiniteIngredient:
        for block in reversed(self.displayable_images + self.clickable_images):
            dx = px.mouse_x - block.x
            dy = px.mouse_y - block.y
            if dx > 0 and dx < 16 and dy > 0 and dy < 16:
                self.dx = dx
                self.dy = dy
                return block

    def start_dragging(self):
        # TODO: remove type checking and find a better way
        clicked_item = self.find_overlapping()
        if type(clicked_item) is Image:
            self.dragged = clicked_item
            self.move_to_back(self.dragged)
        elif type(clicked_item) is InfiniteIngredient:
            clicked_item.clone_ingredient()

    def drag(self):
        self.dragged.x = px.mouse_x - self.dx
        self.dragged.y = px.mouse_y - self.dy

    def handle_click(self, button: int):
        if px.btn(button):
            if self.dragged is not None:
                self.drag()
            else:
                self.start_dragging()
        else:
            self.dragged = None

    def move_to_back(self, item: Image):
        self.clickable_images.remove(item)
        self.clickable_images.append(item)
