import pyxel as px


class MouseDrag:
    def __init__(self, clickable_blocks):
        self.dragged = None
        self.blocks = clickable_blocks
        self.dx = 0
        self.dy = 0

    def start_dragging(self):
        for block in self.blocks:
            dx = px.mouse_x - block.x
            dy = px.mouse_y - block.y
            if dx > 0 and dx < 16 and dy > 0 and dy < 16:
                self.dragged = block
                self.dx = dx
                self.dy = dy

    def drag(self):
        self.dragged.x = px.mouse_x - self.dx
        self.dragged.y = px.mouse_y - self.dy

    def handle_click(self, button):
        if px.btn(button):
            if self.dragged is not None:
                self.drag()
            else:
                self.start_dragging()
        else:
            self.dragged = None
