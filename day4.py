## day 4

import re
import functools

example = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''

example_invalids='''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007'''

example_valids = '''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
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
