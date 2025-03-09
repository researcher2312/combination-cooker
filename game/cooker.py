from enum import Enum
from images import get_image
from cookbook import Cookbook
from graphics import Image, Slot, Textbox, Rect

cookbook = Cookbook()
actions = ["cut", "boil", "fry", "bake", "add", "blend"]


class IngredientType(Enum):
    fruit = 1
    spread = 2
    drink = 3
    vegetable = 4


class CookingStation:
    def __init__(self, x, y, n_fields=2):
        self.x = x
        self.y = y
        self.fields = [Slot(x + i * 30, y, 18) for i in range(n_fields)]
        self.result_field = Slot(120, 80, 18)
        self.text = Textbox(x + 32, y + 20, "")
        self.left = get_image("left").set_coordinates(x + 16, y + 30)
        self.right = get_image("right").set_coordinates(x + 48, y + 30)
        self.set_action("boil")

    def display(self):
        for field in self.fields:
            field.display()
        self.text.display()
        self.left.display()
        self.right.display()
        self.action_image.display()

    def update(self):
        if self.right.clicked_now():
            self.next_action()
        if self.left.clicked_now():
            self.previous_action()

    def set_action(self, action: str):
        self.action_image = get_image(action).set_coordinates(self.x + 32, self.y + 30)
        self.action = action
        self.text.text = action

    def next_action(self):
        action_index = actions.index(self.action)
        if action_index != len(actions) - 1:
            self.set_action(actions[action_index + 1])
        else:
            self.set_action(actions[0])

    def previous_action(self):
        action_index = actions.index(self.action)
        if action_index == 0:
            self.set_action(actions[-1])
        else:
            self.set_action(actions[action_index - 1])

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
