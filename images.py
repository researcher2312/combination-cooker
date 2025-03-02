import pyxel as px

from graphics import Image

images = {
    "apple": (16, 0, px.COLOR_DARK_BLUE),
    "sugar": (16, 16, px.COLOR_PINK),
    "flour": (32, 0, px.COLOR_DARK_BLUE),
    "sliced apple": (48, 0, px.COLOR_DARK_BLUE),
    "water": (32, 16, px.COLOR_PINK),
    "dough": (48, 16, px.COLOR_DARK_BLUE),
    "sweet dough": (0, 32, px.COLOR_DARK_BLUE),
    "apple pie": (16, 32, px.COLOR_DARK_BLUE),
    "caramel": (32, 32, px.COLOR_DARK_BLUE),
    "apple jam": (48, 32, px.COLOR_DARK_BLUE),
    "cookies": (0, 48, px.COLOR_DARK_BLUE),
    "flatbread": (16, 48, px.COLOR_DARK_BLUE),
    "apple chips": (32, 48, px.COLOR_DARK_BLUE),
    "apple compote": (48, 48, px.COLOR_DARK_BLUE),
    "caramelized apple": (0, 64, px.COLOR_DARK_BLUE),
}


def get_images(names: list[str]) -> list[Image]:
    return [Image(*images[name], name) for name in names]
