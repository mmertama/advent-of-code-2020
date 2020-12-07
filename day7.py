import re

example = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

example2 = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''


def search_luggage(rules, container, luggage, luggages=set()):
    if container in luggages:
        return luggages
    foundings = set()
    for rule in rules[container]:
        target = rule[1]
        if target == luggage:
            foundings.add(container)
            break
        else:
            sub_foundings = search_luggage(rules, target, luggage, luggages)
            if len(sub_foundings):
                foundings.update(sub_foundings)
                foundings.add(container)
                break
    return foundings


def search_luggage_content(rules, luggage, luggages={}):
    if luggage in luggages:
        return luggages
    count = 0
    for rule in rules[luggage]:
        times = rule[0]
        target = rule[1]
        if target not in luggages:
            children = search_luggage_content(rules, target, luggages)
            luggages.update(children)
        assert target in luggages
        times *= luggages[target] + 1    # children + this
        count += times
    luggages[luggage] = count
    return luggages


def get_rules(data):
    rules = {}
    for line in data:
        m = re.match(r'(.*)\s+bags?\s+contain\s+(no\s+other\s+bags)?(.*).$', line)
        assert m
        properties = m[1]
        assert properties not in rules
        rules[properties] = list()
        if not m[2]:
            content_list = m[3].split(',')
            for content in content_list:
                m_content = re.match(r'\s*(\d+)\s+(.*)\s+bags?', content)
                assert m_content
                rules[properties].append((int(m_content[1]), m_content[2]))
    return rules


def luggage_processor(data, luggage):
    rules = get_rules(data)
    luggages = set()
    for l in rules.keys():
        luggages.update(search_luggage(rules, l, luggage))
    print("number of bags:", len(luggages))


def luggage_processor_content(data, luggage):
    rules = get_rules(data)
    luggages = search_luggage_content(rules, luggage)
    print("number of bags in bag:", luggages[luggage])
