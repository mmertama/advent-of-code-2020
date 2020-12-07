## day1


def make_string(lst, *args):
    return ','.join([' ' + str(lst[x]) + ' (' + str(x) + ')' for x in args])


example = '''1721
979
366
299
675
1456
'''


def find_index(lst, start, end, eq):
    if start > end:
        return None
    pos = int((end + start) / 2)
    d = eq(lst[pos])
    if d == 0:
        return pos
    if d < 0:
        return find_index(lst, pos + 1, end, eq)
    if d > 0:
        return find_index(lst, start, pos - 1, eq)


def find_two_factors(input_str):
    values = [int(x) for x in input_str]
    values.sort()
    max_index = len(values)
    for a in range(0, max_index):
        b = find_index(values, a + 1, max_index - 1, lambda x: (x + values[a]) - 2020)
        if b:
            print("Pair found", make_string(values, a, b), "ans: ", str(values[a] * values[b]))


def find_three_factors(input_str):
    values = [int(x) for x in input_str]
    values.sort()
    max_index = len(values)
    for a in range(0, max_index):
        for b in range(a + 1, max_index):
            c = find_index(values, b + 1, max_index - 1, lambda x: (x + values[a] + values[b]) - 2020)
            if c:
                print("Pair found", make_string(values, a, b, c), "ans: ", str(values[a] * values[b] * values[c]))
