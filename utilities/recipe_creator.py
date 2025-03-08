from json import dump, load

FILENAME = "../recipes.json"


def get_new_recipe() -> dict:
    recipe_name = input()
    action = input()
    ingredients = input()
    ingredients = ingredients.split(", ")
    return {"name": recipe_name, "action": action, "ingredients": ingredients}


if __name__ == "__main__":
    with open(FILENAME, "r") as file:
        recipes = load(file)
    new_recipes = get_new_recipe()
    recipes.append(new_recipes)
    with open(FILENAME, "w") as file:
        dump(recipes, file)
