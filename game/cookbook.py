import csv
from enum import Enum, Flag
from pathlib import Path

RECIPES_FILENAME = "recipes.csv"
recipes_file = Path(__file__).resolve().parent / RECIPES_FILENAME

ingredient_types = {"fruit", "spread", "drink", "vegetable"}


class IngredientType(Flag):
    none = 0
    fruit = 1
    spread = 2
    drink = 3
    vegetable = 4


class Action(Enum):
    cut = 0
    bake = 1
    boil = 2
    fry = 3
    add = 4
    blend = 5


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
        else:
            return cls(text, IngredientType["none"])

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
    ):
        self.name = name
        self.action = action
        self.ingredients = ingredients
        self.configurable = False

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
        with open(recipes_file, "rt") as file:
            reader = csv.reader(file)
            for row in reader:
                self.recipes.append(Recipe.from_list(row))

    # def combination_possible(self, action: str, ingredients: list[str]) -> bool:
    #     return any(
    #         r["action"] == action and sorted(r["ingredients"]) == sorted(ingredients)
    #         for r in recipes
    #     )

    def recipe_result(self, action: Action, ingredients: list[Ingredient]) -> str:
        for r in self.recipes:
            if r.check_match(action, ingredients):
                return r.get_final_name(ingredients)

    def test_combinations(self) -> None:
        apple = Ingredient("apple", IngredientType.fruit)
        pear = Ingredient("pear", IngredientType.fruit)
        water = Ingredient("water")
        flour = Ingredient("flour")
        assert self.recipe_result(Action.cut, [apple]) == "sliced apple"
        assert self.recipe_result(Action.cut, [pear]) == "sliced pear"
        assert self.recipe_result(Action.boil, [apple, water]) == "boiled apple"
        assert self.recipe_result(Action.add, [water, flour]) == "dough"
        assert self.recipe_result(Action.add, [flour, water]) == "dough"
        assert not self.recipe_result(Action.add, [flour, apple])
        print("Cookbook test succesful")


if __name__ == "__main__":
    cookbook = Cookbook()
    cookbook.test_combinations()
