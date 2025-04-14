import pyxel as px
from graphics import Image, create_image

TAB_PANEL_H = 10
MAX_TABS = 4
drawer_names = ["fruit", "veggies", "liquids", "dried"]
drawer_products = [
    ["apple", "pear"],
    ["chickpeas"],
    ["water", "oil", "milk"],
    ["flour", "sugar", "yeast"],
]


class RubbishBin:
    def __init__(self, x: int, y: int, items: list[Image]) -> None:
        self.image_closed = create_image("rubbish", x, y)
        self.image_opened = create_image("open rubbish", x, y)
        self.items = items

    def display(self) -> None:
        if self.image_opened.hovered():
            self.image_opened.display()
        else:
            self.image_closed.display()

    def update(self) -> None:
        # TODO: switch to check only dragged item
        for item in self.items:
            if (
                abs(self.image_opened.x - item.x) < 16
                and abs(self.image_opened.y - item.y) < 16
                and not px.btn(px.MOUSE_BUTTON_LEFT)
            ):
                self.items.remove(item)
                break


class IngredientDrawer:
    def __init__(self, items: list[Image]) -> None:
        self.global_items: list[Image] = items
        self.selected = 0
        self.keys = [px.KEY_1, px.KEY_2, px.KEY_3, px.KEY_4]
        self.displayed_items: list[Image] = []
        self.setup_products()

    def display(self) -> None:
        px.rect(0, 0, 160, 30, px.COLOR_PEACH)
        for i in range(1, MAX_TABS):
            px.line(i * 40, 0, i * 40, TAB_PANEL_H, px.COLOR_BROWN)
        self.print_bottom_line()
        self.print_drawer_names()
        for item in self.displayed_items:
            item.display()

    def update(self) -> None:
        self.check_mouse_press_on_tabs()
        self.check_keyboard_press_on_tabs()
        self.check_mouse_press_on_ingredients()

    def check_mouse_press_on_ingredients(self) -> None:
        for item in self.displayed_items:
            if item.clicked_now():
                image = create_image(item.name, item.x, item.y)
                self.global_items.append(image)

    def check_mouse_press_on_tabs(self) -> None:
        if px.btnp(px.MOUSE_BUTTON_LEFT) and px.mouse_y < TAB_PANEL_H:
            for i in range(MAX_TABS):
                if px.mouse_x > i * 40 and px.mouse_x < (i + 1) * 40:
                    self.selected = i
                    self.setup_products()

    def check_keyboard_press_on_tabs(self) -> None:
        for key_n, key in enumerate(self.keys):
            if px.btnp(key):
                self.selected = key_n
                self.setup_products()

    def print_bottom_line(self) -> None:
        left_line_end = self.selected * 40
        right_line_begin = (self.selected + 1) * 40
        if left_line_end > 0:
            px.line(0, TAB_PANEL_H, left_line_end, TAB_PANEL_H, px.COLOR_BROWN)
        if right_line_begin < 160:
            px.line(right_line_begin, TAB_PANEL_H, 160, TAB_PANEL_H, px.COLOR_BROWN)

    def print_drawer_names(self) -> None:
        for i, name in enumerate(drawer_names):
            px.text(i * 40 + 5, 3, name, px.COLOR_BLACK)

    def setup_products(self) -> None:
        self.displayed_items.clear()
        for n, product_name in enumerate(drawer_products[self.selected]):
            self.displayed_items.append(create_image(product_name, n * 20 + 5, 13))
