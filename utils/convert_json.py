from json import dump, load
from pathlib import Path
from csv import writer

FILENAME = Path("../game/recipes.json").resolve()

with open(FILENAME, "r") as file:
    recipes = load(file)

with open("recipes.csv", "w") as csvfile:
    writer = writer(csvfile)

    writer.writerow(
        ("recipe name", "action", "ingredient1", "ingredient2", "ingredient3")
    )
    for recipe in recipes:
        writer.writerow((recipe["name"], recipe["action"], *recipe["ingredients"]))
