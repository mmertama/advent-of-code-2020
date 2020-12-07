## day 2
import re

example = '''1-3 a: abcde
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
