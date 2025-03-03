from json import dump

actions = ["cut", "boil", "fry", "bake", "add"]
basic_ingredients = ["apple", "water", "flour", "sugar", "sugar", "milk"]
recipes = [
    {"name": "sliced apple", "action": "cut", "ingredients": ["apple"]},
    {"name": "boiled apple", "action": "boil", "ingredients": ["apple"]},
    {"name": "dough", "action": "add", "ingredients": ["water", "flour"]},
    {
        "name": "sweet dough",
        "action": "add",
        "ingredients": ["water", "flour", "sugar"],
    },
    {
        "name": "apple pie",
        "action": "bake",
        "ingredients": ["sweet dough", "sliced apple"],
    },
    {"name": "apple jam", "action": "fry", "ingredients": ["sliced apple", "sugar"]},
    {"name": "apple compote", "action": "boil", "ingredients": ["sliced apple"]},
    {"name": "cookies", "action": "bake", "ingredients": ["sweet dough"]},
    {"name": "flatbread", "action": "bake", "ingredients": ["dough"]},
    {"name": "apple chips", "action": "bake", "ingredients": ["sliced apple"]},
    {"name": "caramel", "action": "fry", "ingredients": ["sugar"]},
    {
        "name": "caramelized apple",
        "action": "add",
        "ingredients": ["sliced apple", "caramel"],
    },
    {
        "name": "pancake dough",
        "action": "add",
        "ingredients": ["milk", "flour", "sugar"],
    },
    {"name": "pancake", "action": "fry", "ingredients": ["pancake dough"]},
    {"name": "hot milk", "action": "boil", "ingredients": ["milk"]},
    {"name": "sweet milk", "action": "add", "ingredients": ["milk", "sugar"]},
    {"name": "pudding", "action": "boil", "ingredients": ["milk", "flour"]},
    {
        "name": "apple pudding",
        "action": "add",
        "ingredients": ["pudding", "sliced apple"],
    },
    {
        "name": "racuchy",
        "action": "fry",
        "ingredients": ["pancake dough", "sliced apple"],
    },
    {"name": "apple pancake", "action": "fry", "ingredients": ["apple jam", "pancake"]},
]


class Cookbook:
    def combination_possible(self, action: str, ingredients: list) -> bool:
        return any(
            r["action"] == action and sorted(r["ingredients"]) == sorted(ingredients)
            for r in recipes
        )

    def get_combination(self, action: str, ingredients: list) -> str:
        for r in recipes:
            if r["action"] == action and sorted(r["ingredients"]) == sorted(
                ingredients
            ):
                return r["name"]

    def test_combinations(self):
        assert self.get_combination("cut", ["apple"]) == "sliced apple"
        assert self.get_combination("boil", ["apple"]) == "boiled apple"
        assert self.get_combination("add", ["water", "flour"]) == "dough"
        assert self.get_combination("add", ["flour", "water"]) == "dough"
        assert not self.get_combination("add", ["flour", "apple"])
        print("Cookbook test succesful")


if __name__ == "__main__":
    cookbook = Cookbook()
    cookbook.test_combinations()
    with open("recipes.json", "w") as file:
        dump(recipes, file)
