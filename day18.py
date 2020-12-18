import re
example0 = '''1 + 2 * 3 + 4 * 5 + 6'''

example1 = '''1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'''


def expression(line):
    parenthesis = 0
    start = 0
    for i in range(0, len(line)):
        if line[i] == '(':
            if parenthesis == 0:
                start = i
            parenthesis += 1
        if line[i] == ')':
            parenthesis -= 1
            if parenthesis == 0:
                return start, i
    return start, len(line)


def parse_no_precedence(data):
    value = None
    expr = data
    pop = None
    while True:
        rvalue = None
        start, end = expression(expr)
        if start == 0 and end < len(expr):
            rvalue = parse_no_precedence(expr[1:end])
            left = re.match(r'\s*(\*|\+)?\s*(.*)', expr[end + 1:])
            op = left[1]
            expr = left[2]
        else:
            left = re.match(r'(\d+)\s*(\*|\+)?\s*(.*)', expr)
            assert left
            rvalue = int(left[1])
            op = left[2]
            expr = left[3]
        if pop is None:
            value = rvalue
        if pop == '+':
            value += rvalue
        if pop == '*':
            value *= rvalue
        if op is None:
            break
        pop = op
    return value


def parse_add_precedence(data, stop_mul=False):
    value = None
    expr = data
    pop = None
    while True:
        rvalue = None
        start, end = expression(expr)
        if start == 0 and end < len(expr):
            rvalue = parse_add_precedence(expr[1:end])[0]
            left = re.match(r'\s*(\*|\+)?\s*(.*)', expr[end + 1:])
            op = left[1]
            expr = left[2]
        else:
            left = re.match(r'(\d+)\s*(\*|\+)?\s*(.*)', expr)
            assert left
            rvalue = int(left[1])
            op = left[2]
            expr = left[3]
        if pop is None:
            value = rvalue
        if pop == '+':
            value += rvalue
        if pop == '*':
            if op == '+':
                rrvalue, expr, op = parse_add_precedence(expr, True)
                value *= rrvalue + rvalue
            else:
                value *= rvalue
        if op is None:
            break
        pop = op
        if stop_mul and pop == '*':
            return value, expr, pop
    return value, "", None


def calc(data):
    summa = 0
    for line in data:
        value = parse_no_precedence(line)
        summa += value
    print("sum is", summa)


def calc2(data):
    summa = 0
    for line in data:
        value = parse_add_precedence(line)[0]
        print(value)
        summa += value
    print("sum is", summa)