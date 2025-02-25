import pyxel as px


class Image:
    def __init__(self, x, y, bg_color):
        self.sprite_x = x
        self.sprite_y = y
        self.bg_color = bg_color

    def display(self, x: int, y: int):
        px.blt(x, y, 0, self.sprite_x, self.sprite_y, 16, 16, self.bg_color)


class Slot:
    def __init__(self, len, x, y):
        self.len = len
        self.x = x
        self.y = y
        self.col = px.COLOR_BROWN

    def display(self):
        px.rectb(self.x, self.y, self.len, self.len, self.col)


class Block:
    def __init__(self, image, x=0, y=0):
        self.x = x
        self.y = y
        self.image = image

    def display(self):
        self.image.display(self.x, self.y)

    def set_coordinates(self, coords):
        self.x, self.y = coords
