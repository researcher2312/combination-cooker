from game.cookbook import (
    Ingredient,
    IngredientType,
    Action,
    read_types,
    recipe_result,
    read_dependencies,
)

apple = Ingredient("apple", IngredientType.fruit)
pear = Ingredient("pear", IngredientType.fruit)
water = Ingredient("water")
flour = Ingredient("flour")
milk = Ingredient("milk")
dough = Ingredient("dough")
sugar = Ingredient("sugar")

sliced_apple = Ingredient("sliced apple", IngredientType.fruit | IngredientType.sliced)
boiled_apple = Ingredient("boiled apple", IngredientType.fruit | IngredientType.boiled)
sliced_pear = Ingredient("sliced pear", IngredientType.fruit | IngredientType.sliced)
apple_shake = Ingredient("apple shake", IngredientType.drink)
apple_jam = Ingredient("apple jam", IngredientType.spread)
bread_slice = Ingredient("bread_slice", IngredientType.flat)
bread_slice_with_apple_jam = Ingredient("bread_slice with apple jam")


def test_basic_recipes():
    assert recipe_result(Action.cut, [apple]) == sliced_apple
    assert recipe_result(Action.cut, [pear]) == sliced_pear
    assert recipe_result(Action.boil, [apple, water]) == boiled_apple
    assert recipe_result(Action.add, [water, flour]) == dough
    assert recipe_result(Action.add, [flour, water]) == dough
    assert recipe_result(Action.blend, [milk, apple]) == apple_shake
    assert not recipe_result(Action.add, [flour, apple])


def test_compound_recipes():
    assert recipe_result(Action.boil, [sliced_apple, sugar]) == apple_jam


def test_double_compound_recipes():
    assert (
        recipe_result(Action.add, [apple_jam, bread_slice])
        == bread_slice_with_apple_jam
    )


def test_compound_recipes_graphics_name():
    assert recipe_result(Action.add, [apple_jam, bread_slice]).graphics == "jam bread"


def test_basic_ingredient_creation():
    assert apple == Ingredient.from_result_string("apple")
    assert dough == Ingredient.from_result_string("dough")


def test_parametric_ingredient_creation():
    assert sliced_apple == Ingredient.from_parameters(
        "sliced apple", "sliced+fruit", ""
    )


def test_string_ingredient_creation():
    assert sliced_apple.type == Ingredient.from_result_string("{sliced+fruit}").type


def test_type_reader():
    assert read_types("sliced+fruit") == IngredientType.fruit | IngredientType.sliced
    assert read_types("boiled") == IngredientType.boiled
    assert read_types("") == IngredientType.none


def test_dependency_reader():
    assert read_dependencies("$fruit jam") == [IngredientType.fruit]
    assert read_dependencies("$flat x $spread") == [
        IngredientType.flat,
        IngredientType.spread,
    ]


def test_original_names():
    assert sliced_apple.get_original_name() == "apple"
    assert boiled_apple.get_original_name() == "apple"
    assert apple_jam.get_original_name() == "apple jam"
