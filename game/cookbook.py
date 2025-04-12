import copy
import csv
from enum import Enum, Flag, auto
from pathlib import Path
from string import Template

(NAME, TYPE, ACTION, GRAPHICS, INGR1, INGR2, INGR3) = range(7)
RECIPES_FILENAME = "recipes.csv"
recipes_file = Path(__file__).resolve().parent / RECIPES_FILENAME


class IngredientType(Flag):
    none = 0
    fruit = auto()
    spread = auto()
    drink = auto()
    vegetable = auto()
    sliced = auto()
    boiled = auto()
    flat = auto()


class Action(Enum):
    cut = 0
    bake = 1
    boil = 2
    fry = 3
    add = 4
    blend = 5


class Ingredient:
    def __init__(
        self,
        name: str,
        ingredient_type: IngredientType = IngredientType.none,
        has_dependencies=False,
        graphics="",
    ):
        self.type = ingredient_type
        self.name = name
        self.has_dependencies = has_dependencies
        self.graphics = graphics

    @classmethod
    def from_result_string(cls, text: str):
        if "{" in text:
            return cls("", read_types(text[1:-1]))
        else:
            return cls(text, IngredientType["none"])

    @classmethod
    def from_parameters(cls, name: str, ingredient_types: str, graphics: str):
        has_dependencies = "$" in name
        return cls(name, read_types(ingredient_types), has_dependencies, graphics)

    @property
    def graphics_name(self) -> str:
        return self.graphics if self.graphics else self.name

    def get_original_name(self) -> str:
        if IngredientType.sliced in self.type:
            return self.name.replace("sliced ", "")
        elif IngredientType.boiled in self.type:
            return self.name.replace("boiled ", "")
        else:
            return self.name

    def __eq__(self, other):
        if not self.name or not other.name:
            return self.type == other.type
        else:
            return self.name == other.name

    def __repr__(self):
        return f"{self.name}({self.type.name})"


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

    def get_name_from_template(self, ingredients: list[Ingredient]) -> str:
        name_templ = Template(self.result.name)
        field_names = name_templ.get_identifiers()
        field_map = {}
        for name in field_names:
            for ingr in ingredients:
                if IngredientType[name] in ingr.type:
                    field_map.update({name: ingr.get_original_name()})
        return name_templ.substitute(field_map)

    def get_result(self, ingredients: list[Ingredient]) -> Ingredient:
        result = copy.deepcopy(self.result)
        if result.has_dependencies:
            result.name = self.get_name_from_template(ingredients)
        return result

    def __str__(self):
        return (
            f"{self.result.name} ({self.result.type}): {self.action} {self.ingredients}"
        )

    def __repr__(self):
        return (
            f"{self.result.name} ({self.result.type}): {self.action} {self.ingredients}"
        )


def read_types(text: str) -> IngredientType:
    result = IngredientType.none
    if not text:
        return result
    for type_name in text.split("+"):
        result |= IngredientType[type_name]
    return result


def read_dependencies(text: str) -> list[IngredientType]:
    return [IngredientType[m] for m in Template(text).get_identifiers()]


def recipe_result(action: Action, ingredients: list[Ingredient]) -> Ingredient | None:
    for r in recipes:
        if r.check_match(action, ingredients):
            return r.get_result(ingredients)


recipes: list[Recipe] = []
ingredients = {
    "apple": Ingredient("apple", IngredientType.fruit),
    "pear": Ingredient("pear", IngredientType.fruit),
    "chickpeas": Ingredient("chickpeas"),
    "water": Ingredient("water"),
    "oil": Ingredient("oil"),
    "milk": Ingredient("milk"),
    "flour": Ingredient("flour"),
    "sugar": Ingredient("sugar"),
    "yeast": Ingredient("yeast"),
}

with open(recipes_file, "rt") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        name = row[NAME]
        result = Ingredient.from_parameters(name, row[TYPE], row[GRAPHICS])
        action = Action[row[ACTION]]
        ingrs = [Ingredient.from_result_string(name) for name in row[INGR1:] if name]
        recipes.append(Recipe(result, action, ingrs))
