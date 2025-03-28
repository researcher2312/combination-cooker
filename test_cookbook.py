import pytest
from game.cookbook import Cookbook, Ingredient, IngredientType, Action


@pytest.fixture
def cookbook():
    return Cookbook()


def test_recipes(cookbook):
    apple = Ingredient("apple", IngredientType.fruit)
    sliced_apple = Ingredient(
        "sliced apple", IngredientType.fruit | IngredientType.sliced
    )
    pear = Ingredient("pear", IngredientType.fruit)
    water = Ingredient("water")
    flour = Ingredient("flour")
    milk = Ingredient("milk")

    assert cookbook.recipe_result(Action.cut, [apple]) == "sliced apple"
    assert cookbook.recipe_result(Action.cut, [pear]) == "sliced pear"
    assert cookbook.recipe_result(Action.boil, [apple, water]) == "boiled apple"
    assert cookbook.recipe_result(Action.add, [water, flour]) == "dough"
    assert cookbook.recipe_result(Action.add, [flour, water]) == "dough"
    assert cookbook.recipe_result(Action.blend, [milk, apple]) == "apple shake"
    assert not cookbook.recipe_result(Action.add, [flour, apple])


def test_ingredients():
    apple = Ingredient("apple", IngredientType.fruit)
    assert apple == Ingredient.from_string("apple")


def test_type_reader():
    assert (
        Ingredient.read_types("sliced+fruit")
        == IngredientType.sliced | IngredientType.fruit
    )
    assert Ingredient.read_types("boiled") == IngredientType.boiled
