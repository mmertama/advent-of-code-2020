import re

example = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''


def find_safe_food(data):
    foods = []
    ingredients = set()
    allergens = set()
    for line in data:
        m = re.match(r'\s*(.*)\s+\(\s*contains\s+(.*)\s*\)', line)
        assert m
        ingredients_list = [x.strip() for x in m[1].split(' ')]
        allergens_list = [x.strip() for x in m[2].split(',')]
        foods.append({'inc': set(ingredients_list), 'all': set(allergens_list)})
        for i in ingredients_list:
            ingredients.add(i)
        for a in allergens_list:
            allergens.add(a)

    possibilities = {}
    for a in allergens:
        f = set()
        for food in foods:
            if a in food['all']:
                f = f.union(food['inc'])
        possibilities[a] = f

    for p in possibilities.items():
        print(p)

    for inc in ingredients:
        found = False
        for p in possibilities.values():
            if inc in p:
                found = True
        if not found:
            print(inc)

