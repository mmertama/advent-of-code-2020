import functools

example = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''


def kind(x, y, data):
    if y < 0:
        return None
    if y >= len(data):
        return None
    if x < 0:
        return None
    if x >= len(data[0]):
        return None
    return data[y][x]


def count_occupied(x, y, data):
    adjacent = ((x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                (x - 1, y), (x + 1, y),
                (x - 1, y + 1), (x, y + 1), (x + 1, y + 1))
    empties = 0
    for p in adjacent:
        if kind(p[0], p[1], data) == '#':
            empties += 1
    return empties


def sight(x, y, p, data):
    x1 = x + p[0]
    y1 = y + p[1]
    k = kind(x1, y1, data)
    if k == '#':
        return 1
    if k == 'L':
        return 0
    if k is None:
        return 0
    return sight(x1, y1, p, data)


def count_occupied_sight(x, y, data):
    see_to = ((-1, -1), (0, -1), (1, -1),
                (-1, 0), (1, 0),
                (-1, 1), (0, 1), (1, 1))
    empties = 0
    for s in see_to:
        empties += sight(x, y, s, data)
    return empties


def generate_next(data, limit, see_function):
    line_len = len(data[0])
    is_changed = False
    next_frame = [[None] * len(data[0]) for i in range(len(data))]
    for j in range(0, len(data)):
        for i in range(0, line_len):
            seat = kind(i, j, data)
            next_seat = seat
            if seat == 'L':
                if see_function(i, j, data) == 0:
                    next_seat = '#'
                    is_changed = True
            elif seat == '#':
                if see_function(i, j, data) >= limit:
                    next_seat = 'L'
                    is_changed = True
            assert not data[j][i] == '.' or next_seat == '.'
            next_frame[j][i] = next_seat
    return next_frame, is_changed


def seat_occupation_count(input_data):
    data = [list(line) for line in input_data]
    while True:
        data, changes = generate_next(data, 4, count_occupied)
        if not changes:
            break
    print("occupied:", functools.reduce(lambda a, l: functools.reduce(lambda acc, s: acc + 1 if s == '#' else acc, l, a), data, 0))


def seat_occupation_count_sight(input_data):
    data = [list(line) for line in input_data]
    while True:
        data, changes = generate_next(data, 5, count_occupied_sight)
        if not changes:
            break
    print("sight occupied:", functools.reduce(lambda a, l: functools.reduce(lambda acc, s: acc + 1 if s == '#' else acc, l, a), data, 0))

