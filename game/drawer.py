import pyxel as px
from graphics import Image, create_image

TAB_PANEL_H = 10
MAX_TABS = 4
drawer_names = ["fruit", "veggies", "liquids", "dried"]
drawer_products = [
    ["apple"],
    ["chickpeas"],
    ["water", "oil", "milk"],
    ["flour", "sugar", "yeast"],
]


class RubbishBin:
    def __init__(self, x: int, y: int, items: list[Image]) -> None:
        self.image_closed = create_image("rubbish", x, y)
        self.image_opened = create_image("open rubbish", x, y)
        self.items = items

    def display(self):
        if self.image_opened.hovered():
            self.image_opened.display()
        else:
            self.image_closed.display()

    def update(self):
        # TODO: switch to check only dragged item
        for item in self.items:
            if (
                abs(self.image_opened.x - item.x) < 16
                and abs(self.image_opened.y - item.y) < 16
                and not px.btn(px.MOUSE_BUTTON_LEFT)
            ):
                self.items.remove(item)
                break


class InfiniteIngredient:
    def __init__(self, x: int, y: int, name: str, items: list[Image]) -> None:
        self.x = x
        self.y = y
        self.image = create_image(name, x, y)
        self.name = name
        self.items_list = items

    def clone_ingredient(self) -> None:
        image = create_image(self.name, self.x, self.y)
        self.items_list.append(image)

    def display(self) -> None:
        self.image.display()


class IngredientDrawer:
    def __init__(self, items: list[Image]) -> None:
        self.global_items = items
        self.selected = 0
        self.keys = [px.KEY_1, px.KEY_2, px.KEY_3, px.KEY_4]
        self.displayed_items: list[InfiniteIngredient] = []
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
        if px.btnp(px.MOUSE_BUTTON_LEFT) and px.mouse_y < TAB_PANEL_H:
            for i in range(MAX_TABS):
                if px.mouse_x > i * 40 and px.mouse_x < (i + 1) * 40:
                    self.selected = i
                    self.setup_products()
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
        # self.remove_from_global()
        self.displayed_items.clear()
        for n, product_name in enumerate(drawer_products[self.selected]):
            self.displayed_items.append(
                InfiniteIngredient(n * 20 + 5, 13, product_name, self.global_items)
                # get_image(product_name).set_coordinates(n * 20 + 5, 13)
            )
        # self.global_items.extend(self.displayed_items)

    def remove_from_global(self) -> None:
        for item in self.displayed_items:
            self.global_items.remove(item)
