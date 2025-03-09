import pyxel as px

from graphics import Image

DEFAULT_BG = px.COLOR_DARK_BLUE
special_background = {"water": px.COLOR_PINK, "sugar": px.COLOR_PINK}
image_alias = {"boiled apple": "apple", "boiled chickpeas": "chickpeas"}

image_names = [
    "bread", "apple", "flour", "sliced apple", "milk", "sugar", "water",
    "dough", "sweet dough", "apple pie", "caramel", "apple jam", "cookies",
    "flatbread", "apple chips", "apple compote", "caramelized apple",
    "pancake dough", "hot milk", "pudding", "apple pudding", "pancake",
    "apple pancake", "fritters", "cut", "fry", "boil", "bake", "add", "left",
    "right", "blend", "chickpeas", "powdered sugar", "yeast", "yeast dough",
    "yeast cake", "sweet yeast dough", "hummus", "oil", "apple shake",
]  # fmt: skip


def get_image(name: str) -> Image:
    if name in image_alias:
        aliased = get_image(image_alias[name])
        aliased.name = name
        return aliased
    position = image_names.index(name)
    row = position // 4
    column = position % 4
    bg = DEFAULT_BG
    if name in special_background:
        bg = special_background[name]
    return Image(column * 16, row * 16, bg, name)


def get_images(names: list[str]) -> list[Image]:
    return [get_image(name) for name in names]
