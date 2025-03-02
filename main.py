import pyxel as px
from mouse import MouseDrag
from graphics import Button, align_text_right
from cooker import CookingStation
from images import images, get_images

cooking_stations = [
    CookingStation(10, 30, "cut"),
    CookingStation(80, 20, "boil"),
    CookingStation(50, 50, "fry"),
    CookingStation(10, 90, "bake"),
    CookingStation(80, 90, "mix")
]

starting_items = ["apple", "flour", "sugar", "water"]

class App:
    def __init__(self):
        px.init(160, 120, title="Cooking Game")
        px.mouse(True)
        px.load("resources.pyxres")
        self.items = get_images(starting_items)
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
        px.text(55, 41, "Cooking game", px.frame_count % 16)
        for cooker in self.cookers:
            cooker.display()
        self.button.display()
        overlapped_block = self.clicker.find_overlapping()
        if overlapped_block is not None:
            align_text_right(150, 110, overlapped_block.name)
        for item in self.items:
            item.display()


App()
