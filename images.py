import pyxel as px

from graphics import Image

DEFAULT_BG = px.COLOR_DARK_BLUE
special_background = {"water": px.COLOR_PINK, "sugar": px.COLOR_PINK}

image_names = [
    "bread", "apple", "flour", "sliced apple", "milk", "sugar", "water", "dough",
    "sweet dough", "apple pie", "caramel", "apple jam", "cookies", "flatbread",
    "apple chips", "apple compote", "caramelized apple", "pancake dough",
    "hot milk", "pudding", "apple pudding", "pancake", "apple pancake", "racuchy",
    "cut", "fry", "boil", "bake", "mix", "left", "right"
]  # fmt: skip


def get_image(name: str) -> Image:
    position = image_names.index(name)
    row = position // 4
    column = position % 4
    bg = DEFAULT_BG
    if name in special_background:
        bg = special_background[name]
    return Image(column * 16, row * 16, bg, name)


def get_images(names: list[str]) -> list[Image]:
    return [get_image(name) for name in names]
