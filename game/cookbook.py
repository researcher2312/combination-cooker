import copy
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
    flat = 7


def read_types(text: str) -> IngredientType:
    result = IngredientType.none
    if not text:
        return result
    for type_name in text.split("+"):
        result |= IngredientType[type_name]
    return result


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
        self,
        name: str,
        ingredient_type: IngredientType = IngredientType.none,
        depends=False,
    ):
        self.ingredient_type = ingredient_type
        self.name = name
        self.depends = depends

    @classmethod
    def from_string(cls, text: str):
        if text in ingredient_types:
            return cls("", IngredientType[text])
        elif text in ingredient_attributes:
            return cls(text, ingredient_attributes[text])
        else:
            return cls(text, IngredientType["none"])

    @classmethod
    def from_parameters(cls, name: str, ingredient_types: str):
        depends = False
        if "{" in name:
            depends = True
        return cls(name, read_types(ingredient_types), depends)

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
        result: Ingredient,
        action: Action,
        ingredients: list[Ingredient],
    ):
        self.result = result
        self.action = action
        self.ingredients = ingredients

    def check_match(self, action: Action, ingredients: list[Ingredient]) -> bool:
        return (
            self.action == action
            and len(self.ingredients) == len(ingredients)
            and all([ingredient in ingredients for ingredient in self.ingredients])
        )

    def get_result(self, ingredients: list[Ingredient]) -> Ingredient:
        result = copy.deepcopy(self.result)
        if result.depends:
            formatter = {ingr.ingredient_type.name: ingr.name for ingr in ingredients}
            result.name = result.name.format_map(formatter)
        return result

    def __str__(self):
        return f"{self.result.name} ({self.result.ingredient_type}): {self.action} {self.ingredients}"


class Cookbook:
    def __init__(self):
        self.recipes: list[Recipe] = []
        # self.ingredients = list[Ingredient] = []
        with open(recipes_file, "rt") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                name = row[0]
                result = Ingredient.from_parameters(name, row[1])
                action = Action[row[2]]
                ingredients = [Ingredient.from_string(name) for name in row[3:]]
                # configurable = True if "{" in name else False
                self.recipes.append(Recipe(result, action, ingredients))

    # def combination_possible(self, action: str, ingredients: list[str]) -> bool:
    #     return any(
    #         r["action"] == action and sorted(r["ingredients"]) == sorted(ingredients)
    #         for r in recipes
    #     )

    def recipe_result(
        self, action: Action, ingredients: list[Ingredient]
    ) -> Ingredient | None:
        for r in self.recipes:
            if r.check_match(action, ingredients):
                return r.get_result(ingredients)
