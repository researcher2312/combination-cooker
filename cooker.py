import pyxel as px
from graphics import Slot


class Cooker:
    def __init__(self):
        self.left_field = Slot(18, 40, 80)
        self.right_fieled = Slot(18, 80, 80)
        self.result_field = Slot(18, 120, 80)

    def display(self):
        self.left_field.display()
        self.right_fieled.display()
        self.result_field.display()

    def bring_to_slot(self, items):
        for item in items:
            for slot in [self.left_field, self.right_fieled]:
                dx = item.x - slot.x
                dy = item.y - slot.y
                if dx > -8 and dx < 24 and dy > -8 and dy < 24:
                    item.x = slot.x + 1
                    item.y = slot.y + 1
