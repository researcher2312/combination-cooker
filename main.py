import pyxel as px
from mouse import MouseDrag
from graphics import Rect, Image, Button
from cooker import Cooker

apple = Image(16, 0, px.COLOR_DARK_BLUE, "apple")
knife = Image(0, 0, px.COLOR_DARK_BLUE, "knife")
flour = Image(32, 0, px.COLOR_DARK_BLUE, "flour")
milk = Image(0, 16, px.COLOR_DARK_BLUE, "milk")
sugar = Image(16, 16, px.COLOR_PINK, "sugar")
items = [apple, knife, flour, milk, sugar]


class App:
    def __init__(self):
        px.init(160, 120, title="Cooking Game")
        px.mouse(True)
        px.load("resources.pyxres")
        self.items = items
        self.clicker = MouseDrag(self.items)
        self.cooker = Cooker()
        self.button = Button(50, 20, 30, 10)
        px.playm(0)
        px.run(self.update, self.draw)

    def update(self):
        if px.btnp(px.KEY_Q):
            px.quit()
        self.button.update()
        self.clicker.handle_click(px.MOUSE_BUTTON_LEFT)
        self.cooker.check_item_removed()
        self.cooker.find_close_item(self.items)

    def draw(self):
        px.cls(px.COLOR_WHITE)
        px.text(55, 41, "Cooking game", px.frame_count % 16)
        self.cooker.display()
        self.button.display()
        overlapped_block = self.clicker.find_overlapping()
        if overlapped_block is not None:
            px.text(130, 110, overlapped_block.name, px.COLOR_BLACK)
        for item in self.items:
            item.display()


App()
