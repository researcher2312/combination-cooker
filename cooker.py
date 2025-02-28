from graphics import Slot


class Cooker:
    def __init__(self):
        self.left_field = Slot(40, 80, 18)
        self.right_field = Slot(80, 80, 18)
        self.result_field = Slot(120, 80, 18)

    def display(self):
        self.left_field.display()
        self.right_field.display()
        self.result_field.display()

    def find_close_item(self, items):
        for item in items:
            for slot in [self.left_field, self.right_field]:
                dx = item.x - slot.x
                dy = item.y - slot.y
                if dx > -8 and dx < 24 and dy > -8 and dy < 24:
                    slot.insert_item(item)

    def check_item_removed(self):
        for slot in [self.left_field, self.right_field]:
            if slot.held_item is not None:
                dx = slot.held_item.x - slot.x
                dy = slot.held_item.y - slot.y
                if dx < -8 or dx > 24 or dy < -8 or dy > 24:
                    slot.held_item = None
