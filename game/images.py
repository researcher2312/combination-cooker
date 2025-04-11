import pyxel as px

DEFAULT_BG = px.COLOR_DARK_BLUE
special_background = {"water": px.COLOR_PINK, "sugar": px.COLOR_PINK}
image_alias = {"boiled apple": "apple", "boiled chickpeas": "chickpeas"}

image_names = [
    "bread", "apple", "flour", "sliced apple", "milk", "sugar", "water",
    "dough", "sweet dough", "apple pie", "caramel", "jam", "cookies",
    "flatbread", "apple chips", "compote", "caramelized apple",
    "pancake dough", "hot milk", "pudding", "apple pudding", "pancake",
    "apple pancake", "fritters", "cut", "fry", "boil", "bake", "add", "left",
    "right", "blend", "chickpeas", "powdered sugar", "yeast", "yeast dough",
    "yeast cake", "sweet yeast dough", "hummus", "oil", "fruit shake",
    "bread slice", "jam bread", "rubbish", "open rubbish", "pear", "sliced pear"
]  # fmt: skip


class ImageData:
    def __init__(self, im_x: int, im_y: int, bg_col: int):
        self.im_x = im_x
        self.im_y = im_y
        self.bg_color = bg_col


def get_image_data(name: str) -> ImageData:
    if name in image_alias:
        aliased = get_image_data(image_alias[name])
        return aliased
    position = image_names.index(name)
    row = position // 4
    column = position % 4
    bg = DEFAULT_BG
    if name in special_background:
        bg = special_background[name]
    return ImageData(column * 16, row * 16, bg)


def get_images_data(names: list[str]) -> list[ImageData]:
    return [get_image_data(name) for name in names]
