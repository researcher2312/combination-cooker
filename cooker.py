from graphics import Slot
from cookbook import Cookbook

cookbook = Cookbook()

class Ingredient:
    def __init__(self, image, name):
        self.image = image
        self.name = name


class CookingStation:
    def __init__(self, x, y, action, no_fields=2):
        self.fields = [Slot(x+i*30, y, 18) for i in range(no_fields)]
        self.result_field = Slot(120, 80, 18)
        self.action = action

    def display(self):
        for field in self.fields:
            field.display()

    def find_close_item(self, items):
        for item in items:
            for slot in self.fields:
                dx = item.x - slot.x
                dy = item.y - slot.y
                if dx > -8 and dx < 24 and dy > -8 and dy < 24:
                    slot.insert_item(item)

    def check_item_removed(self):
        for slot in self.fields:
            if slot.held_item is not None:
                dx = slot.held_item.x - slot.x
                dy = slot.held_item.y - slot.y
                if dx < -8 or dx > 24 or dy < -8 or dy > 24:
                    slot.held_item = None

    def get_items(self):
        return [
            slot.held_item.name
            for slot in self.fields
            if slot.held_item is not None
        ]

    def check_recipe(self):
        recipe = cookbook.get_combination(self.action, self.get_items())
        print(f"{self.action} - {recipe}")
