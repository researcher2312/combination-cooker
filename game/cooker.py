from cookbook import Action, Ingredient, recipe_result, ingredients
from graphics import Image, Slot, Textbox, create_image

actions = [Action.cut, Action.boil, Action.fry, Action.bake, Action.add, Action.blend]


class CookingStation:
    def __init__(self, x: int, y: int, n_fields: int = 2) -> None:
        self.x = x
        self.y = y
        self.fields = [Slot(x + i * 30, y, 18) for i in range(n_fields)]
        self.result_field = Slot(120, 80, 18)
        self.text = Textbox(x + 32, y + 20, "")
        self.left = create_image("left", x + 16, y + 30)
        self.right = create_image("right", x + 48, y + 30)
        self.set_action(Action.cut)

    def display(self) -> None:
        for field in self.fields:
            field.display()
        self.text.display()
        self.left.display()
        self.right.display()
        self.action_image.display()

    def update(self) -> None:
        if self.right.clicked_now():
            self.next_action()
        if self.left.clicked_now():
            self.previous_action()

    def set_action(self, action: Action) -> None:
        self.action_image = create_image(action.name, self.x + 32, self.y + 30)
        self.action = action
        self.text.text = action.name

    def next_action(self) -> None:
        action_index = actions.index(self.action)
        if action_index != len(actions) - 1:
            self.set_action(actions[action_index + 1])
        else:
            self.set_action(actions[0])

    def previous_action(self) -> None:
        action_index = actions.index(self.action)
        if action_index == 0:
            self.set_action(actions[-1])
        else:
            self.set_action(actions[action_index - 1])

    def find_close_item(self, items: list[Image]) -> None:
        for item in items:
            for slot in self.fields:
                dx = item.x - slot.x
                dy = item.y - slot.y
                if dx > -8 and dx < 24 and dy > -8 and dy < 24:
                    if not item.clicked():
                        slot.insert_item(item)

    def check_item_removed(self) -> None:
        for slot in self.fields:
            if slot.held_item is not None:
                dx = slot.held_item.x - slot.x
                dy = slot.held_item.y - slot.y
                if dx < -8 or dx > 24 or dy < -8 or dy > 24:
                    slot.held_item = None

    def get_contained_ingredients(self) -> list[Ingredient]:
        return [
            ingredients[slot.held_item.name]
            for slot in self.fields
            if slot.held_item is not None
        ]

    def check_recipe(self) -> Ingredient | None:
        return recipe_result(self.action, self.get_contained_ingredients())

    def clear_values(self, items: list[Image]) -> None:
        for slot in self.fields:
            if slot.held_item is not None:
                items.remove(slot.held_item)
                slot.held_item = None
