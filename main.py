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

    def set_coordinates(self, coords):
        self.x, self.y = coords


class MouseDrag:
    def __init__(self, clickable_blocks):
        self.clicked = False
        self.dragged = None
        self.blocks = clickable_blocks
        self.dx = 0
        self.dy = 0

    def start_dragging(self):
        for block in self.blocks:
            dx = px.mouse_x - block.x
            dy = px.mouse_y - block.y
            if dx > 0 and dx < 16 and dy > 0 and dy < 16:
                self.clicked = True
                self.dragged = block
                self.dx = dx
                self.dy = dy

    def drag(self):
        self.dragged.x = px.mouse_x - self.dx
        self.dragged.y = px.mouse_y - self.dy

    def handle_click(self, button_pressed):
        if button_pressed:
            if self.clicked:
                self.drag()
            else:
                self.start_dragging()
        else:
            self.clicked = False


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
        self.clicker.handle_click(px.btn(px.MOUSE_BUTTON_LEFT))

    def draw(self):
        px.cls(white)
        px.text(55, 41, "Cooking game", px.frame_count % 16)
        for item in self.items:
            item.display()


App()
