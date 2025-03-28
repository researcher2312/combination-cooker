from typing import Self, Callable

import pyxel as px
from images import ImageData, get_image_data


def create_image(name: str, x: int = 0, y: int = 0):
    return Image.from_data(get_image_data(name), x, y)


def get_text_size(text: str) -> tuple[int, int]:
    return (len(text) * 4 - 1, 5)


def align_text_right(x: int, y: int, text: str):
    text_x, text_y = get_text_size(text)
    px.text(x - text_x, 110, text, px.COLOR_BLACK)


class Rect:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y
        self.w = 16
        self.h = 16

    def display(self) -> None:
        self.image.display(self.x, self.y)

    def set_coordinates(self, x: int, y: int) -> Self:
        self.x, self.y = x, y
        return self

    def hovered(self) -> bool:
        return 0 < px.mouse_x - self.x < self.w and 0 < px.mouse_y - self.y < self.h

    def clicked(self) -> bool:
        return self.hovered() and px.btn(px.MOUSE_BUTTON_LEFT)

    def clicked_now(self) -> bool:
        return self.hovered() and px.btnp(px.MOUSE_BUTTON_LEFT)


class Textbox(Rect):
    def __init__(self, x: int, y: int, text: str):
        super().__init__(x, y)
        self.text = text

    def display(self):
        px.text(self.x, self.y, self.text, px.COLOR_BLACK)


class Image(Rect):
    def __init__(self, imx: int, imy: int, bg_color: int, name: str, x=0, y=0):
        super().__init__(x, y)
        self.sprite_x = imx
        self.sprite_y = imy
        self.bg_color = bg_color
        self.name = name

    @classmethod
    def from_data(cls, data: ImageData, x: int, y: int):
        return cls(data.im_x, data.im_y, data.bg_color, data.name, x, y)

    def display(self) -> None:
        px.blt(self.x, self.y, 0, self.sprite_x, self.sprite_y, 16, 16, self.bg_color)


class Slot(Rect):
    def __init__(self, x: int, y: int, len: int) -> None:
        super().__init__(x, y)
        self.len = len
        self.col = px.COLOR_BROWN
        self.held_item = None

    def display(self) -> None:
        px.rectb(self.x, self.y, self.len, self.len, self.col)

    def insert_item(self, item: Image) -> None:
        self.throw_out_item()
        self.held_item = item
        item.x = self.x + 1
        item.y = self.y + 1

    def throw_out_item(self) -> None:
        if self.held_item is not None:
            self.held_item.x += 17
            self.held_item.y -= 17
            self.held_item = None


class Button(Rect):
    def __init__(self, x: int, y: int, w: int, h: int, action: Callable):
        super().__init__(x, y)
        self.w = w
        self.h = h
        self.action = action
        self.text = "COOK"
        self.col = px.COLOR_BROWN
        tx, ty = get_text_size(self.text)
        self.text_x = x + (w - tx) / 2
        self.text_y = y + (h - ty) / 2

    def update(self) -> None:
        if self.clicked_now():
            self.action()

    def display(self) -> None:
        if self.clicked():
            self.col = px.COLOR_GRAY
        else:
            self.col = px.COLOR_BROWN
        self.display_internal()

    def display_internal(self) -> None:
        px.rect(self.x, self.y, self.w, self.h, self.col)
        px.text(self.text_x, self.text_y, self.text, px.COLOR_BLACK)
