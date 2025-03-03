import pyxel as px

from cookbook import basic_ingredients
from cooker import CookingStation
from graphics import Button, align_text_right
from images import get_images
from mouse import MouseDrag

cooking_stations = [
    CookingStation(10, 30, "cut"),
    CookingStation(80, 10, "boil"),
    CookingStation(90, 35, "fry"),
    CookingStation(10, 90, "bake"),
    CookingStation(80, 70, "add", 3),
]


class App:
    def __init__(self):
        px.init(160, 120, title="Cooking Game")
        px.mouse(True)
        px.load("resources.pyxres")
        self.items = get_images(basic_ingredients)
        self.clicker = MouseDrag(self.items)
        self.cookers = cooking_stations
        self.button = Button(50, 20, 30, 10, self.check_cookers)
        px.playm(0)
        px.run(self.update, self.draw)

    def check_cookers(self):
        for cooker in self.cookers:
            result = cooker.check_recipe()
            if result is not None:
                self.create_item(result)
                cooker.clear_values(self.items)

    def create_item(self, name: str):
        self.items.extend(get_images([name]))

    def update(self):
        if px.btnp(px.KEY_Q):
            px.quit()
        self.button.update()
        self.clicker.handle_click(px.MOUSE_BUTTON_LEFT)
        for cooker in self.cookers:
            cooker.check_item_removed()
            cooker.find_close_item(self.items)

    def draw(self):
        px.cls(px.COLOR_WHITE)
        for cooker in self.cookers:
            cooker.display()
        self.button.display()
        overlapped_block = self.clicker.find_overlapping()
        if overlapped_block is not None:
            align_text_right(150, 110, overlapped_block.name)
        for item in self.items:
            item.display()


App()
