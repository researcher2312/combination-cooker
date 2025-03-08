from json import dump, load
from pathlib import Path

FILENAME = Path("../game/recipes.json").resolve()


def get_new_recipe() -> dict:
    recipe_name = input("name: ")
    action = input("action: ")
    ingredients = input("ingredients: ")
    ingredients = ingredients.split(", ")
    return {"name": recipe_name, "action": action, "ingredients": ingredients}


if __name__ == "__main__":
    while True:
        with open(FILENAME, "r") as file:
            recipes = load(file)
        new_recipes = get_new_recipe()
        recipes.append(new_recipes)
        with open(FILENAME, "w") as file:
            dump(recipes, file)
