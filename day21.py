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
        f = None
        for food in foods:
            if a in food['all']:
                if f is None:
                    f = set(food['inc'])
                else:
                    f.intersection_update(food['inc'])
        possibilities[a] = f

    safe_food = set()

    for inc in ingredients:
        found = False
        for p in possibilities.values():
            if inc in p:
                found = True
        if not found:
            safe_food.add(inc)

    count = 0
    for f in foods:
        for s in safe_food:
            if s in f['inc']:
                count += 1
    print("Safe count", count)

    canonical_list = {}
    while True:
        if len(possibilities) == 0:
            break
        for k, v in possibilities.items():
            if len(v) == 1:
                canonical_list[v.pop()] = k

        possibilities = {k: v for k, v in possibilities.items() if len(v) > 0}

        for k in canonical_list.keys():
            for pk, pset in possibilities.items():
                if k in pset:
                    possibilities[pk].remove(k)

    dangerous_stuff = list(canonical_list.items())
    dangerous_stuff.sort(key=lambda t: t[1])
    print("Dangerous stuff:", ','.join([x[0] for x in dangerous_stuff]))


