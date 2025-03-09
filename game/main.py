import pyxel as px
from cooker import CookingStation
from drawer import IngredientDrawer
from graphics import Button, align_text_right
from images import get_images
from mouse import MouseDrag


class App:
    def __init__(self):
        px.init(160, 120, title="Cooking Game")
        px.mouse(True)
        px.load("resources.pyxres")
        self.items = []
        self.clicker = MouseDrag(self.items)
        self.cooker = CookingStation(40, 40, 3)
        self.button = Button(65, 100, 30, 10, self.check_cookers)
        self.drawer = IngredientDrawer()
        px.playm(0)
        px.run(self.update, self.draw)

    def check_cookers(self):
        result = self.cooker.check_recipe()
        if result is not None:
            self.create_item(result)
            self.cooker.clear_values(self.items)

    def create_item(self, name: str):
        self.items.extend(get_images([name]))

    def update(self):
        if px.btnp(px.KEY_Q):
            px.quit()
        self.button.update()
        self.drawer.update()
        self.clicker.handle_click(px.MOUSE_BUTTON_LEFT)
        self.cooker.update()
        self.cooker.check_item_removed()
        self.cooker.find_close_item(self.items)

    def draw(self):
        px.cls(px.COLOR_WHITE)
        self.cooker.display()
        self.button.display()
        self.drawer.display()
        overlapped_block = self.clicker.find_overlapping()
        if overlapped_block is not None:
            align_text_right(150, 110, overlapped_block.name)
        for item in self.items:
            item.display()


App()
