import pyxel as px

blue = 5
white = 7
pink = 14

apple = (16, 0, blue)
knife = (0, 0, blue)
flour = (32, 0, blue)
milk = (0, 16, blue)
sugar = (16, 16, pink)
items = [apple, knife, flour, milk, sugar]


def display_image(x: int, y: int, image):
    px.blt(x, y, 0, image[0], image[1], 16, 16, image[2])


class Block:
    def __init__(self, image, x=0, y=0):
        self.x = x
        self.y = y
        self.image = image

    def display(self):
        display_image(self.x, self.y, self.image)


class App:
    def __init__(self):
        px.init(160, 120, title="Cooking Game")
        px.mouse(True)
        px.load("resources.pyxres")
        self.items = [Block(item) for item in items]
        px.playm(0)
        px.run(self.update, self.draw)

    def update(self):
        if px.btnp(px.KEY_Q):
            px.quit()
        if px.btnp(px.MOUSE_BUTTON_LEFT):
            for item in items:
                dx = item.x - px.mouse_x
                dy = item.y - px.mouse_y
                if dx < 16 and dy < 16:
                    item.x

    def draw(self):
        px.cls(white)
        px.text(55, 41, "Cooking game", px.frame_count % 16)
        for item in self.items:
            item.display()


App()
