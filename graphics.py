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
        self.held_item = None

    def display(self):
        px.rectb(self.x, self.y, self.len, self.len, self.col)

    def insert_item(self, item):
        self.throw_out_item()
        self.held_item = item
        item.x = self.x + 1
        item.y = self.y + 1

    def throw_out_item(self):
        if self.held_item != None:
            self.held_item.x += 17
            self.held_item.y -= 17
            self.held_item = None


class Block:
    def __init__(self, image, name, x=0, y=0):
        self.x = x
        self.y = y
        self.image = image
        self.name = name

    def display(self):
        self.image.display(self.x, self.y)

    def set_coordinates(self, coords):
        self.x, self.y = coords


class Button:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = "COOK"
        self.col = px.COLOR_BROWN
        self.text_x = x + w/2
        self.text_y = y + h/2

    def display(self):
        px.rect(self.x, self.y, self.w, self.h, self.col)
        px.text(self.text_x, self.text_y, self.text, px.COLOR_BLACK)


    
