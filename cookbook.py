actions = ["cut", "boil", "fry", "bake", "mix"]

basic_ingredients = ["apple", "water", "flour", "sugar"]

recipes = [
    {name: "sliced apple", action: "cut", ingredients: ["apple"]},
    {name: "boiled apple", action: "boil", ingredients: ["apple"]},
    {name: "dough", action: "mix", ingredients: ["water", "flour"]},
    {name: "sweet dough", action: "mix", ingredients: ["water", "flour", "sugar"]},
    {name: "apple pie", action: "bake", ingredients: ["sweet dough", "sliced apple"]},
    {name: "apple jam", action: "fry", ingredients: ["sliced apple", "sugar"]},
    {name: "apple compote", action: "boil", ingredients: ["sliced apple"]},
    {name: "cookies", action: "bake", ingredients: ["sweet dough"]},
    {name: "flatbread", action: "bake", ingredients: ["dough"]},
    {name: "apple chips", action: "bake", ingredients: ["sliced apple"]},
    {name: "caramel", action: "fry", ingredients: ["sugar"]},
    {name: "caramelized apple", action: "mix", ingredients: ["sliced apple", "caramel"]},
]
