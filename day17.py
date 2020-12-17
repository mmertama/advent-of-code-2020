example = '''.#.
..#
###'''


def get_actives(cloud, xx, yy, zz):
    actives = 0
    for z in range(zz - 1, zz + 2):
        if z not in cloud:
            continue
        for y in range(yy - 1, yy + 2):
            if y not in cloud[z]:
                continue
            for x in range(xx - 1, xx + 2):
                if x not in cloud[z][y]:
                    continue
                if x != xx or y != yy or z != zz:
                    if cloud[z][y][x]:
                        actives += 1
    return actives


def get_actives_w(cloud, xx, yy, zz, ww):
    actives = 0
    for w in range(ww - 1, ww + 2):
        if w not in cloud:
            continue
        for z in range(zz - 1, zz + 2):
            if z not in cloud[w]:
                continue
            for y in range(yy - 1, yy + 2):
                if y not in cloud[w][z]:
                    continue
                for x in range(xx - 1, xx + 2):
                    if x not in cloud[w][z][y]:
                        continue
                    if x != xx or y != yy or z != zz or w != ww:
                        if cloud[w][z][y][x]:
                            actives += 1
    return actives


def get_cloud(grid):
    cloud = {}
    for z, plane in grid.items():
        if z not in cloud:
            cloud[z] = {}
        for y, line in plane.items():
            if y not in cloud[z]:
                cloud[z][y] = {}
            for x in line:
                cloud[z][y][x] = True
                for zz in range(z - 1, z + 2):
                    if zz not in cloud:
                        cloud[zz] = {}
                    for yy in range(y - 1, y + 2):
                        if yy not in cloud[zz]:
                            cloud[zz][yy] = {}
                        for xx in range(x - 1, x + 2):
                            if (xx - 1) not in cloud[zz][yy]:
                                cloud[zz][yy][xx - 1] = False
                            if (xx + 1) not in cloud[zz][yy]:
                                cloud[zz][yy][xx + 1] = False
    return cloud


def get_cloud_w(hyper_grid):
    cloud = {}
    for w, hyper_cube in hyper_grid.items():
        if w not in cloud:
            cloud[w] = {}
        for z, plane in hyper_cube.items():
            if z not in cloud[w]:
                cloud[w][z] = {}
            for y, line in plane.items():
                if y not in cloud[w][z]:
                    cloud[w][z][y] = {}
                for x in line:
                    cloud[w][z][y][x] = True
                    for ww in range(w - 1, w + 2):
                        if ww not in cloud:
                            cloud[ww] = {}
                        for zz in range(z - 1, z + 2):
                            if zz not in cloud[ww]:
                                cloud[ww][zz] = {}
                            for yy in range(y - 1, y + 2):
                                if yy not in cloud[ww][zz]:
                                    cloud[ww][zz][yy] = {}
                                for xx in range(x - 1, x + 2):
                                    if (xx - 1) not in cloud[ww][zz][yy]:
                                        cloud[ww][zz][yy][xx - 1] = False
                                    if (xx + 1) not in cloud[ww][zz][yy]:
                                        cloud[ww][zz][yy][xx + 1] = False
    return cloud

'''
def add_empty_n(cloud, coordinates, x):
    sub_space = cloud
    for p in coordinates:
        for r in range(p - 1, p + 2):
            if r not in sub_space:
                sub_space[r] = {}
        sub_space = cloud[r]
    for xx in range(x - 1, x + 2):
        if (xx - 1) not in sub_space:
            sub_space[xx - 1] = False
        if (xx + 1) not in sub_space:
            sub_space[xx + 1] = False


def get_cloud_n(universe):
    cloud = {}
    root = universe
    cloud_space = cloud
    coordinate = []
    while True:
        for d, sub_space in root.items():
            coordinate.append(d)
            if d not in cloud_space:
                cloud_space[d] = {}
            if isinstance(sub_space, set):
                for x in sub_space:
                    cloud_space[d][x] = True
                    add_empty_n(cloud, coordinate, x)
            else:
                if d not in cloud_space:
                    cloud_space[d] = {}
                root = sub_space
                cloud_space = cloud_space[d]
            coordinate.pop()
    return cloud
'''

def calc_next(grid):
    cloud = get_cloud(grid)
    for z, plane in cloud.items():
        for y, line in plane.items():
            for x, is_active in line.items():
                actives = get_actives(cloud, x, y, z)
                if is_active:
                    if not (actives == 2 or actives == 3):
                        grid[z][y].remove(x)
                        if len(grid[z][y]) == 0:
                            grid[z].pop(y)
                            if len(grid[z]) == 0:
                                grid.pop(z)
                else:
                    if actives == 3:
                        if z not in grid:
                            grid[z] = {}
                        if y not in grid[z]:
                            grid[z][y] = set()
                        grid[z][y].add(x)


def calc_next_w(hyper_grid):
    cloud = get_cloud_w(hyper_grid)
    for w, hyper_cube in cloud.items():
        for z, plane in hyper_cube.items():
            for y, line in plane.items():
                for x, is_active in line.items():
                    actives = get_actives_w(cloud, x, y, z, w)
                    if is_active:
                        if not (actives == 2 or actives == 3):
                            hyper_grid[w][z][y].remove(x)
                            if len(hyper_grid[w][z][y]) == 0:
                                hyper_grid[w][z].pop(y)
                                if len(hyper_grid[w][z]) == 0:
                                    hyper_grid[w].pop(z)
                                    if len(hyper_grid[w]) == 0:
                                        hyper_grid.pop(w)
                    else:
                        if actives == 3:
                            if w not in hyper_grid:
                                hyper_grid[w] = {}
                            if z not in hyper_grid[w]:
                                hyper_grid[w][z] = {}
                            if y not in hyper_grid[w][z]:
                                hyper_grid[w][z][y] = set()
                            hyper_grid[w][z][y].add(x)

'''
def calc_next_n(universe):
    cloud = get_cloud_n(universe)
    root = universe
    coordinates = []
    while True:
        for d, sub_space in root.items():
            coordinates.append(d)
            if isinstance(sub_space, hash):
                root = sub_space
            else:
                is_active = sub_space
                actives = get_actives_n(cloud, coordinates)
                if is_active:
                    if not (actives == 2 or actives == 3):
                        root.remove(d)
                    else:
                        if actives == 3:
                            if w not in hyper_grid:
                                hyper_grid[w] = {}
                            if z not in hyper_grid[w]:
                                hyper_grid[w][z] = {}
                            if y not in hyper_grid[w][z]:
                                hyper_grid[w][z][y] = set()
                            hyper_grid[w][z][y].add(x)
            if len(hyper_grid[w][z][y]) == 0:
                hyper_grid[w][z].pop(y)
                if len(hyper_grid[w][z]) == 0:
                    hyper_grid[w].pop(z)
                    if len(hyper_grid[w]) == 0:
                        hyper_grid.pop(w)
'''

def count_active(grid):
    actives = 0
    for plane in grid.values():
        for line in plane.values():
            actives += len(line)
    return actives


def count_active_w(hyper_grid):
    actives = 0
    for grid in hyper_grid.values():
        for plane in grid.values():
            for line in plane.values():
                actives += len(line)
    return actives


def boot_cubes_3d(data, cycles):
    grid = {}
    plane = {}
    for y in range(0, len(data)):
        line = set()
        for x in range(0, len(data[y])):
            if data[y][x] == '#':
                line.add(x)
        plane[y] = line
    grid[0] = plane

    for r in range(0, cycles):
        calc_next(grid)
    print("actives in grid:", count_active(grid))

'''
def boot_cubes(data, cycles):
    grid = {}
    plane = {}
    for y in range(0, len(data)):
        line = set()
        for x in range(0, len(data[y])):
            if data[y][x] == '#':
                line.add(x)
        plane[y] = line
    grid[0] = plane

    for r in range(0, cycles):
        calc_next_n(grid, 3)
    print("actives in grid:", count_active(grid))
'''

def boot_cubes_4d(data, cycles):
    hyper_cube = {}
    grid = {}
    plane = {}
    for y in range(0, len(data)):
        line = set()
        for x in range(0, len(data[y])):
            if data[y][x] == '#':
                line.add(x)
        plane[y] = line
    grid[0] = plane
    hyper_cube[0] = grid

    for r in range(0, cycles):
        calc_next_w(hyper_cube)

    print("active in hyper grid", count_active_w(hyper_cube))

