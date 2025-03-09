import pyxel as px
from images import get_image
from graphics import Rect

TAB_PANEL_H = 10
MAX_TABS = 4


class InfiniteIngredient(Rect):
    def __init__(self, x, y, name, items) -> None:
        super().__init__(x, y)
        self.image = get_image(name).set_coordinates(x, y)
        self.name = name
        self.items_list = items

    def update(self):
        if self.clicked_now():
            image = get_image(self.name).set_coordinates(self.x, self.y)
            self.items_list.append(image)

    def display(self):
        self.image.display()


class IngredientDrawer:
    def __init__(self):
        self.selected = 0
        self.drawer_names = ["fruit", "veggies", "liquids", "dried"]
        self.keys = [px.KEY_1, px.KEY_2, px.KEY_3, px.KEY_4]

    def display(self):
        px.rect(0, 0, 160, 40, px.COLOR_PEACH)
        for i in range(1, MAX_TABS):
            px.line(i * 40, 0, i * 40, TAB_PANEL_H, px.COLOR_BROWN)
        self.print_bottom_line()
        self.print_drawer_names()

    def update(self):
        for key_n, key in enumerate(self.keys):
            if px.btnp(key):
                self.selected = key_n

    def print_bottom_line(self) -> None:
        left_line_end = self.selected * 40
        right_line_begin = (self.selected + 1) * 40
        if left_line_end > 0:
            px.line(0, TAB_PANEL_H, left_line_end, TAB_PANEL_H, px.COLOR_BROWN)
        if right_line_begin < 160:
            px.line(right_line_begin, TAB_PANEL_H, 160, TAB_PANEL_H, px.COLOR_BROWN)

    def print_drawer_names(self):
        for i, name in enumerate(self.drawer_names):
            px.text(i * 40 + 5, 3, name, px.COLOR_BLACK)
