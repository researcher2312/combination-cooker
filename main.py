import pyxel as px
from mouse import MouseDrag
from graphics import Block, Image, Slot
from cooker import Cooker

apple = Image(16, 0, px.COLOR_DARK_BLUE)
knife = Image(0, 0, px.COLOR_DARK_BLUE)
flour = Image(32, 0, px.COLOR_DARK_BLUE)
milk = Image(0, 16, px.COLOR_DARK_BLUE)
sugar = Image(16, 16, px.COLOR_PINK)
items = [apple, knife, flour, milk, sugar]
item_names = ["apple", "cut", "flour", "milk", "sugar"]


class App:
    def __init__(self):
        px.init(160, 120, title="Cooking Game")
        px.mouse(True)
        px.load("resources.pyxres")
        self.items = [Block(item, name) for item, name in zip(items, item_names)]
        self.clicker = MouseDrag(self.items)
        self.cooker = Cooker()
        px.playm(0)
        px.run(self.update, self.draw)

    def update(self):
        if px.btnp(px.KEY_Q):
            px.quit()
        self.clicker.handle_click(px.MOUSE_BUTTON_LEFT)
        self.cooker.bring_to_slot(self.items)

    def draw(self):
        px.cls(px.COLOR_WHITE)
        px.text(55, 41, "Cooking game", px.frame_count % 16)
        if self.clicker.dragged != None:
            px.text(130, 110, self.clicker.dragged.name, px.COLOR_BLACK)
        self.cooker.display()
        for item in self.items:
            item.display()


App()
