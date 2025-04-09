import copy
import csv
import re
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


def read_types(text: str) -> IngredientType:
    result = IngredientType.none
    if not text:
        return result
    for type_name in text.split("+"):
        result |= IngredientType[type_name]
    return result


def read_dependencies(text: str) -> list[IngredientType]:
    return [IngredientType[m] for m in Template(text).get_identifiers()]

    # return [IngredientType[m] for m in re.findall(r"\{(.*?)\}", text)]


class Action(Enum):
    cut = 0
    bake = 1
    boil = 2
    fry = 3
    add = 4
    blend = 5


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
        depends_on=IngredientType.none,
        graphics="",
    ):
        self.ingredient_type = ingredient_type
        self.name = name
        self.depends_on = depends_on
        self.graphics = graphics

    @classmethod
    def from_result_string(cls, text: str):
        if "{" in text:
            return cls("", read_types(text[1:-1]))
        else:
            return cls(text, IngredientType["none"])

    @classmethod
    def from_parameters(cls, name: str, ingredient_types: str, graphics: str):
        depends = read_dependencies(name)[0] if "$" in name else IngredientType.none
        return cls(name, read_types(ingredient_types), depends, graphics)

    @property
    def graphics_name(self) -> str:
        return self.graphics if self.graphics else self.name

    def get_original_name(self) -> str:
        if IngredientType.sliced in self.ingredient_type:
            return self.name.replace("sliced ", "")
        elif IngredientType.boiled in self.ingredient_type:
            return self.name.replace("boiled ", "")
        else:
            return self.name

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
        for ingr in ingredients:
            if result.depends_on in ingr.ingredient_type:
                name_templ = Template(result.name)
                depend_name = result.depends_on.name or ""
                result.name = name_templ.substitute(
                    {depend_name: ingr.get_original_name()}
                )
        return result

    def __str__(self):
        return f"{self.result.name} ({self.result.ingredient_type}): {self.action} {self.ingredients}"

    def __repr__(self):
        return f"{self.result.name} ({self.result.ingredient_type}): {self.action} {self.ingredients}"


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
        # configurable = True if "{" in name else False
        recipes.append(Recipe(result, action, ingrs))

    # def combination_possible(self, action: str, ingredients: list[str]) -> bool:
    #     return any(
    #         r["action"] == action and sorted(r["ingredients"]) == sorted(ingredients)
    #         for r in recipes
    #     )


def recipe_result(action: Action, ingredients: list[Ingredient]) -> Ingredient | None:
    for r in recipes:
        if r.check_match(action, ingredients):
            return r.get_result(ingredients)


# print(list(filter(lambda x: x.result.name == "{fruit} jam", recipes)))
