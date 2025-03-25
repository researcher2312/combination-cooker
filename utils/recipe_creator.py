import csv
from pathlib import Path

recipes_file = Path("./recipes.csv").resolve()


def get_new_recipe() -> dict:
    recipe_name = input("name: ")
    action = input("action: ")
    ingredients = input("ingredients: ")
    ingredients = ingredients.split(", ")
    return {"name": recipe_name, "action": action, "ingredients": ingredients}


# with open(recipes_file, "rt") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         recipe = {"name": row[0], "action": row[1], "ingredients": row[2:]}
#         recipes.append(recipe)

# if __name__ == "__main__":
#     while True:
#         with open(FILENAME, "r") as file:
#             recipes = load(file)
#         new_recipes = get_new_recipe()
#         recipes.append(new_recipes)
#         with open(FILENAME, "w") as file:
#             dump(recipes, file)
