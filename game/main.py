import pyxel as px
from cookbook import Ingredient, ingredients
from cooker import CookingStation
from drawer import IngredientDrawer, RubbishBin
from graphics import Button, Image, align_text_right
from images import get_image_data
from mouse import MouseDrag


class App:
    def __init__(self):
        px.init(160, 120, title="Cooking Game", quit_key=px.KEY_Q)
        px.mouse(True)
        px.load("resources.pyxres")
        self.items: list[Image] = []
        self.cooker = CookingStation(40, 40, 3)
        self.button = Button(65, 100, 30, 10, self.check_cookers)
        self.drawer = IngredientDrawer(self.items)
        self.rubbish_bin = RubbishBin(10, 100, self.items)
        self.clicker = MouseDrag(self.items, self.drawer.displayed_items)
        px.playm(0)
        px.run(self.update, self.draw)

    def check_cookers(self):
        result = self.cooker.check_recipe()
        if result is not None:
            self.create_item(result)
            self.cooker.clear_values(self.items)

    def create_item(self, ingr: Ingredient):
        name = ingr.name
        ingredients[name] = ingr
        graphics_name = ingr.graphics_name
        self.items.append(Image.from_data(get_image_data(graphics_name), name, 40, 35))

    def update(self):
        self.button.update()
        self.drawer.update()
        self.rubbish_bin.update()
        self.clicker.handle_click(px.MOUSE_BUTTON_LEFT)
        self.cooker.update()
        self.cooker.check_item_removed()
        self.cooker.find_close_item(self.items)

    def draw(self):
        px.cls(px.COLOR_WHITE)
        self.cooker.display()
        self.button.display()
        self.drawer.display()
        self.rubbish_bin.display()
        overlapped_block = self.clicker.find_overlapping()
        if overlapped_block is not None:
            align_text_right(150, 110, overlapped_block.name)
        for item in self.items:
            item.display()


App()
