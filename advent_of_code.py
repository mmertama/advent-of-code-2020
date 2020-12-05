import re
import functools

def read_local_lines(str):
    return str.splitlines()


def read_remote_lines(fn):
    lines = []
    with open(fn) as f:
        for l in f:
            lines.append(l.rstrip())
    return lines


def make_string(lst, *args):
    return ','.join([' ' + str(lst[x]) + ' (' + str(x) + ')' for x in args])


## day1


example1 = '''1721
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


## day 2

example2 = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''


def validate_passwords(data):
    valids = 0
    for d in data:
        m = re.match(r'(\d+)-(\d+)\s+(.):\s*(.+)', d)
        assert m
        min_appearance = int(m[1])
        max_appearance = int(m[2])
        code = m[3]
        pwd = m[4]
        count = pwd.count(code)
        if min_appearance <= count <= max_appearance:
            valids += 1
    print(str(valids), '/', len(data), "Valid passwords")


def validate_passwords_2(data):
    valids = 0
    for d in data:
        m = re.match(r'(\d+)-(\d+)\s+(.):\s*(.+)', d)
        assert m
        index_a = int(m[1]) - 1
        index_b = int(m[2]) - 1
        code = m[3]
        pwd = m[4]
        l = len(pwd)
        if index_a < l and index_b < l and ((pwd[index_a] == code) != (pwd[index_b] == code)):
            valids += 1
    print(str(valids), '/', len(data), "Valid passwords")


## day 3

example3='''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''


def navigate_thru_trees(m_x, m_y, map_pattern):
    x = 0
    y = 0
    height = len(map_pattern)
    pattern_width = len(map_pattern[0])
    trees = 0

    def is_tree(px, py):
        map_x = px % pattern_width
        map_y = py % height
        return map_pattern[map_y][map_x] == '#'

    while y < height:
        trees += is_tree(x, y)
        x += m_x
        y += m_y

    print("Tobogan encountered", trees, "trees")
    return trees


def navigate_thru_trees2(map_pattern):
    routes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)]
    m = 1
    for r in routes:
        m *= navigate_thru_trees(r[0], r[1], map_pattern)
    print("Route mul is", m)


## day 4

example4 = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''

example4_invalids='''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007'''

example4_valids = '''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''

def check_passports(data, keys):
    record_data = []
    current_record = {}

    for line in data:
        records = line.split()
        if len(records) == 0:
            record_data.append(current_record)
            current_record = {}
        else:
            for record in records:
                m = re.match(r'\s*(.+)\s*:\s*(.+)', record)
                assert m
                current_record[m[1]] = m[2]

    if len(current_record) > 0:
         record_data.append(current_record)

    valids = 0
    for record in record_data:
        is_valid = functools.reduce(lambda c, k: c
                                                 and k in record.keys()
                                                 and (isinstance(keys, (set, str))
                                                 or keys[k](record[k])), keys, True)
        if is_valid:
            valids += 1
    return valids


def check_passports_strict(data):
    def check_len(x):
        m = re.match(r'(\d+)(cm|in)', x)
        if m:
            if m[2] == 'cm':
                return 150 <= int(m[1]) <= 193
            if m[2] == 'in':
                return 59 <= int(m[1]) <= 76
        return False
    keys = {'byr': lambda x: 1920 <= int(x) <= 2002,
            'iyr': lambda x: 2010 <= int(x) <= 2020,
            'eyr': lambda x: 2020 <= int(x) <= 2030,
            'hgt': check_len,
            'hcl': lambda x: re.match(r'^#[0-9a-f]{6}$', x),
            'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
            'pid': lambda x: re.match(r'^[0-9]{9}$', x)}  # no cid :-D
    valids = check_passports(data, keys)
    print("Valid passports", valids)


def check_passports_loose(data):
    keys = {'byr',
            'iyr',
            'eyr',
            'hgt',
            'hcl',
            'ecl',
            'pid'}  # no cid :-D
    valids = check_passports(data, keys)
    print("Valid passports", valids)


#####

example5 = '''FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL'''


def find_seat(data):
    max_id = 0
    min_id = 100000
    occupied_seats = set()
    for line in data:
        row_data = line[:7]
        col_data = line[7:]
        row = 0
        for r in row_data:
            row <<= 1
            row |= 0 if r == 'F' else 1
        col = 0
        for c in col_data:
            col <<= 1
            col |= 0 if c == 'L' else 1
        seat_id = row * 8 + col
        if seat_id < min_id:
            min_id = seat_id
        if seat_id > max_id:
            max_id = seat_id
        occupied_seats.add(seat_id)
    print("max seat id:", max_id)

    for s in range(min_id, max_id + 1):
        if s not in occupied_seats:
            print(s, "missing")


if __name__ == "__main__":
    # find_two_factors(read_local_lines(example1))
    find_two_factors(read_remote_lines('data/input.txt'))
    # find_three_factors(read_local_lines(example1))
    find_three_factors(read_remote_lines('data/input.txt'))
    # validate_passwords(read_local_lines(example2))
    validate_passwords(read_remote_lines('data/input2.txt'))
    # validate_passwords_2(read_local_lines(example2))
    validate_passwords_2(read_remote_lines('data/input2.txt'))
    # navigate_thru_trees(3, 1, read_local_lines(example3))
    navigate_thru_trees(3, 1, read_remote_lines('data/input3.txt'))
    # navigate_thru_trees2(read_local_lines(example3))
    navigate_thru_trees2(read_remote_lines('data/input3.txt'))
    # check_passports_loose(read_local_lines(example4))
    check_passports_loose(read_remote_lines('data/input4.txt'))
    # check_passports_strict(read_local_lines(example4))
    # check_passports_strict(read_local_lines(example4_invalids))
    # check_passports_strict(read_local_lines(example4_valids))
    check_passports_strict(read_remote_lines('data/input4.txt'))
    # find_seat(read_local_lines(example5))
    find_seat(read_remote_lines('data/input5.txt'))