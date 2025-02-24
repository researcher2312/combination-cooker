import pyxel as px
from mouse import MouseDrag
from graphics import Block

apple = (16, 0, px.COLOR_DARK_BLUE)
knife = (0, 0, px.COLOR_DARK_BLUE)
flour = (32, 0, px.COLOR_DARK_BLUE)
milk = (0, 16, px.COLOR_DARK_BLUE)
sugar = (16, 16, px.COLOR_PINK)
items = [apple, knife, flour, milk, sugar]


class App:
    def __init__(self):
        px.init(160, 120, title="Cooking Game")
        px.mouse(True)
        px.load("resources.pyxres")
        self.items = [Block(item) for item in items]
        self.clicker = MouseDrag(self.items)
        px.playm(0)
        px.run(self.update, self.draw)

    def update(self):
        if px.btnp(px.KEY_Q):
            px.quit()
        self.clicker.handle_click(px.MOUSE_BUTTON_LEFT)

    def draw(self):
        px.cls(px.COLOR_WHITE)
        px.text(55, 41, "Cooking game", px.frame_count % 16)
        for item in self.items:
            item.display()


App()
