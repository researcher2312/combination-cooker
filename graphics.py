import pyxel as px


def get_text_size(text: str) -> int:
    return (len(text) * 4 - 1, 5)

def align_text_right(x: str, y: str, text: str):
    text_x, text_y = get_text_size(text)
    px.text(x-text_x, 110, text, px.COLOR_BLACK)

class Rect:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        self.image.display(self.x, self.y)

    def set_coordinates(self, x, y):
        self.x, self.y = x, y

    def hovered(self):
        return 0 < px.mouse_x - self.x < self.w and 0 < px.mouse_y - self.y < self.h

class Textbox(Rect):
    def __init__(self, x, y, text):
        super().__init__(x, y)
        self.text = text

    def display(self):
        px.text(self.x, self.y, self.text, px.COLOR_BLACK)

class Image(Rect):
    def __init__(self, imx, imy, bg_color, name, x=0, y=0):
        super().__init__(x, y)
        self.sprite_x = imx
        self.sprite_y = imy
        self.bg_color = bg_color
        self.name = name

    def display(self):
        px.blt(self.x, self.y, 0, self.sprite_x, self.sprite_y, 16, 16, self.bg_color)


class Slot(Rect):
    def __init__(self, x, y, len):
        super().__init__(x, y)
        self.len = len
        self.col = px.COLOR_BROWN
        self.held_item = None

    def display(self):
        px.rectb(self.x, self.y, self.len, self.len, self.col)

    def insert_item(self, item):
        self.throw_out_item()
        self.held_item = item
        item.x = self.x + 1
        item.y = self.y + 1

    def throw_out_item(self):
        if self.held_item is not None:
            self.held_item.x += 17
            self.held_item.y -= 17
            self.held_item = None


class Button(Rect):
    def __init__(self, x, y, w, h, action=None):
        super().__init__(x, y)
        self.w = w
        self.h = h
        self.action = action
        self.clicked = False
        self.text = "COOK"
        self.col = px.COLOR_BROWN
        tx, ty = get_text_size(self.text)
        self.text_x = x + (w - tx) / 2
        self.text_y = y + (h - ty) / 2

    def update(self):
        if self.hovered() and px.btn(px.MOUSE_BUTTON_LEFT):
            if not self.clicked and self.action is not None:
                self.action()
            self.clicked = True
        else:
            self.clicked = False

    def display(self):
        if self.clicked:
            self.col = px.COLOR_GRAY
        else:
            self.col = px.COLOR_BROWN
        self.display_internal()

    def display_internal(self):
        px.rect(self.x, self.y, self.w, self.h, self.col)
        px.text(self.text_x, self.text_y, self.text, px.COLOR_BLACK)
