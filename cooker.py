from enum import Enum
from images import get_image
from cookbook import Cookbook
from graphics import Image, Slot, Textbox

cookbook = Cookbook()


class IngredientType(Enum):
    fruit = 1
    spread = 2
    drink = 3
    vegetable = 4


class Ingredient:
    def __init__(self, image, name):
        self.image = image
        self.name = name


class CookingStation:
    def __init__(self, x, y, n_fields=2):
        self.x = x
        self.y = y
        self.fields = [Slot(x + i * 30, y, 18) for i in range(n_fields)]
        self.result_field = Slot(120, 80, 18)
        self.action = "cut"
        self.text = Textbox(x + 17, y + 20, self.action)
        self.left = get_image("left").set_coordinates(x + 20, y + 30)
        self.right = get_image("right").set_coordinates(x + 50, y + 30)

    def display(self):
        for field in self.fields:
            field.display()
        self.text.display()
        self.left.display()
        self.right.display()

    def find_close_item(self, items: list[Image]):
        for item in items:
            for slot in self.fields:
                dx = item.x - slot.x
                dy = item.y - slot.y
                if dx > -8 and dx < 24 and dy > -8 and dy < 24:
                    if not item.clicked():
                        slot.insert_item(item)

    def check_item_removed(self):
        for slot in self.fields:
            if slot.held_item is not None:
                dx = slot.held_item.x - slot.x
                dy = slot.held_item.y - slot.y
                if dx < -8 or dx > 24 or dy < -8 or dy > 24:
                    slot.held_item = None

    def get_item_names(self) -> list[str]:
        return [
            slot.held_item.name for slot in self.fields if slot.held_item is not None
        ]

    def check_recipe(self):
        return cookbook.get_combination(self.action, self.get_item_names())

    def clear_values(self, items):
        for slot in self.fields:
            if slot.held_item is not None:
                items.remove(slot.held_item)
                slot.held_item = None
