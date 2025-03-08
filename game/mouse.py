import pyxel as px


class MouseDrag:
    def __init__(self, clickable_blocks):
        self.blocks = clickable_blocks
        self.dragged = None
        self.dx = 0
        self.dy = 0

    def find_overlapping(self):
        for block in reversed(self.blocks):
            dx = px.mouse_x - block.x
            dy = px.mouse_y - block.y
            if dx > 0 and dx < 16 and dy > 0 and dy < 16:
                self.dx = dx
                self.dy = dy
                return block

    def start_dragging(self):
        self.dragged = self.find_overlapping()
        if self.dragged is not None:
            self.move_to_back(self.dragged)

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

    def move_to_back(self, item):
        self.blocks.remove(item)
        self.blocks.append(item)
