import pytest
from game.cookbook import Cookbook, Ingredient, IngredientType, Action, read_types

apple = Ingredient("apple", IngredientType.fruit)
pear = Ingredient("pear", IngredientType.fruit)
water = Ingredient("water")
flour = Ingredient("flour")
milk = Ingredient("milk")
dough = Ingredient("dough")
sliced_apple = Ingredient("sliced apple", IngredientType.fruit | IngredientType.sliced)
boiled_apple = Ingredient("boiled apple", IngredientType.fruit | IngredientType.boiled)
sliced_pear = Ingredient("sliced pear", IngredientType.fruit | IngredientType.sliced)
apple_shake = Ingredient("apple shake", IngredientType.drink)


@pytest.fixture
def cookbook():
    return Cookbook()


def test_recipes(cookbook):
    assert cookbook.recipe_result(Action.cut, [apple]) == sliced_apple
    assert cookbook.recipe_result(Action.cut, [pear]) == sliced_pear
    assert cookbook.recipe_result(Action.boil, [apple, water]) == boiled_apple
    assert cookbook.recipe_result(Action.add, [water, flour]) == dough
    assert cookbook.recipe_result(Action.add, [flour, water]) == dough
    assert cookbook.recipe_result(Action.blend, [milk, apple]) == apple_shake
    assert not cookbook.recipe_result(Action.add, [flour, apple])


def test_basic_ingredients():
    assert apple == Ingredient.from_string("apple")


def test_compound_ingredients():
    assert sliced_apple == Ingredient.from_parameters("sliced apple", "sliced+fruit")


def test_type_reader():
    assert read_types("sliced+fruit") == IngredientType.sliced | IngredientType.fruit
    assert read_types("boiled") == IngredientType.boiled
    assert read_types("") == IngredientType.none
