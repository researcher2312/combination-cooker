import csv
from enum import Enum
from pathlib import Path

RECIPES_FILENAME = "recipes.csv"
recipes = []

recipes_file = Path(__file__).resolve().parent / RECIPES_FILENAME
with open(recipes_file, "rt") as file:
    reader = csv.reader(file)
    for row in reader:
        recipe = {"name": row[0], "action": row[1], "ingredients": row[2:]}
        recipes.append(recipe)


class IngredientType(Enum):
    fruit = 1
    spread = 2
    drink = 3
    vegetable = 4


class Action(Enum):
    cut = 0
    bake = 1
    boil = 2
    fry = 3
    blend = 4


class Ingredient:
    def __init__(self, name: str, type):
        self.name = name


class Recipe:
    def __init__(self, action: Action, ingredients: list[str]):
        self.action = action
        self.ingredients = ingredients


class Cookbook:
    def combination_possible(self, action: str, ingredients: list[str]) -> bool:
        return any(
            r["action"] == action and sorted(r["ingredients"]) == sorted(ingredients)
            for r in recipes
        )

    def get_combination(self, action: str, ingredients: list[str]) -> str:
        for r in recipes:
            if r["action"] == action and sorted(r["ingredients"]) == sorted(
                ingredients
            ):
                return r["name"]

    def test_combinations(self) -> None:
        assert self.get_combination("cut", ["apple"]) == "sliced apple"
        assert self.get_combination("boil", ["apple", "water"]) == "boiled apple"
        assert self.get_combination("add", ["water", "flour"]) == "dough"
        assert self.get_combination("add", ["flour", "water"]) == "dough"
        assert not self.get_combination("add", ["flour", "apple"])
        print("Cookbook test succesful")


if __name__ == "__main__":
    cookbook = Cookbook()
    cookbook.test_combinations()
