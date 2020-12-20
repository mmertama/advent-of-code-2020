example = '''.#.
..#
###'''


def get_actives(cloud, coordinates, is_same=True):
    actives = 0
    p = coordinates[0]
    if len(coordinates) > 1:
        for w in range(p - 1, p + 2):
            if w not in cloud:
                continue
            actives += get_actives(cloud[w], coordinates[1:], is_same and w == p)
    else:
        for x in range(p - 1, p + 2):
            if x not in cloud:
                continue
            if not (is_same and p == x):
                if cloud[x]:
                    actives += 1
    return actives


def add_empty(cloud, coordinate, x):
    if len(coordinate) == 0:
        for xx in range(x - 1, x + 2):
            if xx not in cloud:
                cloud[xx] = False
    else:
        p = coordinate[0]
        for r in range(p - 1, p + 2):
            if r not in cloud:
                cloud[r] = {}
            add_empty(cloud[r], coordinate[1:], x)


def get_cloud(universe, cloud, sub_cloud, coordinate=[]):
    for d, sub_space in universe.items():
        if d not in sub_cloud:
            sub_cloud[d] = {}
        if isinstance(sub_space, set):
            for x in sub_space:
                sub_cloud[d][x] = True
                add_empty(cloud, coordinate + [d], x)
        else:
            get_cloud(sub_space, cloud, sub_cloud[d], coordinate + [d])


def make_iterator(cloud):
    it = iter(cloud.items())
    return [(it, None)]


def iterate(iterator, depth=0):
    try:
        it = iterator[depth][0]
        current_value = iterator[depth][1]
        if current_value is None:
            current_value = next(it)
        key, value = current_value

        if depth == len(iterator) - 1:
            if isinstance(value, bool):
                return [key], value
            else:
                iterator += make_iterator(value)

        iterator[depth] = (it, current_value)
        value = iterate(iterator, depth + 1)
        if value is None:
            next_item = next(it)
            iterator[depth] = (it, next_item)
            return iterate(iterator, depth)
        return [key] + value[0], value[1]
    except StopIteration:
        iterator.pop(depth)
        return None


def remove(universe, coordinate):
    p = coordinate[0]
    if len(coordinate) == 1:
        universe.remove(p)
        return len(universe)
    else:
        child_len = remove(universe[p], coordinate[1:])
        if child_len == 0:
            universe.pop(p)
        return len(universe)


def add(universe, coordinate):
    p = coordinate[0]
    if len(coordinate) == 1:
        universe.add(p)
    else:
        if p not in universe:
            if len(coordinate) == 2:
                universe[p] = set()
            else:
                universe[p] = {}
        add(universe[p], coordinate[1:])


def calc_next(universe, coordinates=[]):
    cloud = {}
    get_cloud(universe, cloud, cloud)
    iterator = make_iterator(cloud)
    while True:
        value = iterate(iterator)
        if value is None:
            break
        coordinates, is_active = value
        actives = get_actives(cloud, coordinates)

        if is_active:
            if not (actives == 2 or actives == 3):
                remove(universe, coordinates)
        else:
            if actives == 3:
                add(universe, coordinates)


def count_active(grid):
    actives = 0
    for p in grid.values():
        if isinstance(p, set):
            actives += len(p)
        else:
            actives += count_active(p)
    return actives


def boot_cubes(data, dimensions, cycles):
    plane = {}
    for y in range(0, len(data)):
        line = set()
        for x in range(0, len(data[y])):
            if data[y][x] == '#':
                line.add(x)
        plane[y] = line
    grid = plane
    for i in range(2, dimensions):
        plane = {0: grid}
        grid = plane

    for r in range(0, cycles):
        calc_next(grid)

    print("actives in grid:", count_active(grid))
