import csv
from enum import Enum, Flag
from pathlib import Path

RECIPES_FILENAME = "recipes.csv"
recipes_file = Path(__file__).resolve().parent / RECIPES_FILENAME


class IngredientType(Flag):
    none = 0
    fruit = 1
    spread = 2
    drink = 3
    vegetable = 4
    sliced = 5
    boiled = 6


class Action(Enum):
    cut = 0
    bake = 1
    boil = 2
    fry = 3
    add = 4
    blend = 5


ingredient_types = {"fruit", "spread", "drink", "vegetable"}
ingredient_attributes = {
    "apple": IngredientType.fruit,
    "pear": IngredientType.fruit,
    "water": IngredientType.drink,
    "milk": IngredientType.drink,
}


class Ingredient:
    def __init__(
        self, name: str, ingredient_type: IngredientType = IngredientType.none
    ):
        self.ingredient_type = ingredient_type
        self.name = name

    @classmethod
    def from_string(cls, text: str):
        if text in ingredient_types:
            return cls("", IngredientType[text])
        elif text in ingredient_attributes:
            return cls(text, ingredient_attributes[text])
        else:
            return cls(text, IngredientType["none"])

    def read_types(text: str) -> IngredientType:
        result = IngredientType.none
        for type_name in text.split("+"):
            result |= IngredientType[type_name]
        return result

    def __eq__(self, other):
        if not self.name or not other.name:
            return self.ingredient_type == other.ingredient_type
        else:
            return self.name == other.name

    def __repr__(self):
        return f"{self.name}({self.ingredient_type.name})"


class Recipe:
    def __init__(
        self,
        name: str,
        action: Action,
        ingredients: list[Ingredient],
        configurable=False,
    ):
        self.name = name
        self.action = action
        self.ingredients = ingredients
        self.configurable = configurable

    @classmethod
    def from_list(cls, data: list[str]):
        name = data[0]
        action = Action[data[1]]
        ingredients = [Ingredient.from_string(name) for name in data[2:]]
        result = cls(name, action, ingredients)
        if "{" in name:
            result.configurable = True
        return result

    def check_match(self, action: Action, ingredients: list[Ingredient]):
        return (
            self.action == action
            and len(self.ingredients) == len(ingredients)
            and all([ingredient in ingredients for ingredient in self.ingredients])
        )

    def get_final_name(self, ingredients: list[Ingredient]) -> str:
        if self.configurable:
            names = {
                x.ingredient_type.name: x.name
                for x in ingredients
                if x.ingredient_type != IngredientType.none
            }
            return self.name.format_map(names)
        else:
            return self.name

    def __str__(self):
        return f"{self.name}: {self.action} {self.ingredients}"


class Cookbook:
    def __init__(self):
        self.recipes: list[Recipe] = []
        # self.ingredients = list[Ingredient] = []
        with open(recipes_file, "rt") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                name = row[0]
                action = Action[row[2]]
                ingredients = [Ingredient.from_string(name) for name in row[3:]]
                configurable = True if "{" in name else False
                self.recipes.append(Recipe(name, action, ingredients, configurable))

    # def combination_possible(self, action: str, ingredients: list[str]) -> bool:
    #     return any(
    #         r["action"] == action and sorted(r["ingredients"]) == sorted(ingredients)
    #         for r in recipes
    #     )

    def recipe_result(self, action: Action, ingredients: list[Ingredient]) -> str:
        for r in self.recipes:
            if r.check_match(action, ingredients):
                return r.get_final_name(ingredients)
