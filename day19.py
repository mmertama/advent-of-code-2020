import re

example = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''

example2 = '''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42 | 42 8
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'''

TERMINATE = 0
SUB_RULE = 1
SUB_RULE_OR = 2

update = '''8: 42 | 42 8
11: 42 31 | 42 11 31'''


def sub_rules(rules, key, index, line, pos):
    passing = pos
    rule_list = rules[key][index]
    for i in range(0, len(rule_list)):
        passing = is_match(rules, rule_list[i], line, passing)
        if passing < 0:
            break
        if passing >= len(line) and i < len(rule_list) - 1:
            return -1 if key != rule_list[i] else passing
    return passing


def is_match(rules, key, line, pos):
    rule = rules[key]
    if rule[0] == TERMINATE:
        return (pos + 1) if line[pos] == rule[1] else -1
    if rule[0] == SUB_RULE:
        passing = sub_rules(rules, key, 1, line, pos)
        return passing
    if rule[0] == SUB_RULE_OR:
        passing = sub_rules(rules, key, 1, line, pos)
        if passing >= 0:
            return passing
        passing = sub_rules(rules, key, 2, line, pos)
        return passing
    assert False


def parse(rules, line):
    m = re.match(r'\s*(\d+)\s*:\s(("([a-z])")|([0-9]+(\s+[0-9]+)*))(\s*\|\s*([0-9]+(\s+[0-9]+)*))?', line)
    assert m
    key = m[1]
    if m[4] is not None:
        rules[key] = (TERMINATE, m[4])
    elif m[5] is not None:
        sub_rules = m[5].split(' ')
        if m[8] is not None:
            sub_rules_or = m[8].split(' ')
            rules[key] = (SUB_RULE_OR, sub_rules, sub_rules_or)
        else:
            rules[key] = (SUB_RULE, sub_rules)
    else:
        assert False


def find_matches(data, update_data=None):
    rules = {}
    matching = False
    matches = 0

    for line in data:
        if len(line) == 0:
            if matching:
                return
            if update_data:
                for ll in update_data:
                    parse(rules, ll)
            matching = True
            continue

        if matching:
            rule = '0'
            result = is_match(rules, rule, line, 0)
            #print(line, result, len(line))
            if result == len(line):
                matches += 1

        else:
            parse(rules, line)
    print("Matches", matches)

