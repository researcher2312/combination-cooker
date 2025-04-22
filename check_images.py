from game.images import image_names
from game.cookbook import recipes, ingredients, read_dependencies


def get_all_possible_outcomes():
    pass


def check_simple_result(tested_graphics: str):
    if tested_graphics not in image_names:
        print(tested_graphics)


for recipe in recipes:
    tested_graphics = recipe.result.graphics_name
    if "$" in tested_graphics:
        dependent_types = read_dependencies(tested_graphics)
