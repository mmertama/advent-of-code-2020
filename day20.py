
example='''Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
'''


seamonster = ["                  # ",
              "#    ##    ##    ###",
              " #  #  #  #  #  #   "]


def get_borders(image):
    return [[x for x in image[0]],
            [image[x][-1] for x in range(0, len(image))],
            [image[-1][x] for x in range(0, len(image))],
            [image[x][0] for x in range(0, len(image))]]


def set_neigh(images, key, pos, neigh):
    n = images[key]['neigh']
    assert n[pos] is None
    n[pos] = neigh


def match_all(images):
    ops = [lambda data: data,
           lambda data: image_flip_vertical(data),
           lambda data: image_flip_horizontal(data),
           lambda data: image_flip_horizontal(image_flip_vertical(data)),
           lambda data: image_rotated(data),
           lambda data: image_flip_vertical(image_rotated(data)),
           lambda data: image_flip_horizontal(image_rotated(data)),
           lambda data: image_flip_horizontal(image_flip_vertical(image_rotated(data)))]

    keys = list(images.keys())
    deadlock_ops = [0] * len(keys)
    all_matches = []

    def run():
        all_matches.clear()
        for i in range(0, len(keys)):
            current_i = keys[i]
            current_tile_i = images[current_i]
            data_i = current_tile_i['data']
            op_i = current_tile_i['op']
            test_data_i = ops[op_i](data_i)
            borders_i = get_borders(test_data_i)
            matches = []
            for j in range(0, len(keys)):
                if i == j:
                    continue
                current_j = keys[j]
                current_tile_j = images[current_j]
                data_j = current_tile_j['data']
                op_j = current_tile_j['op']
                test_data_j = ops[op_j](data_j)
                borders_j = get_borders(test_data_j)
                ranges = [(0, 2), (2, 0), (1, 3), (3, 1)]
                for r in ranges:
                    if borders_i[r[0]] == borders_j[r[1]]:
                        matches.append((current_i, current_j, r[0], r[1]))
            if len(matches) < 1:
                current_tile_i['op'] += 1
                if current_tile_i['op'] >= len(ops):
                    nonlocal deadlock_ops
                    for index in range(0, len(keys)):
                        key = keys[index]
                        images[key]['op'] = deadlock_ops[index]
                    images[deadlock_ops[0]]['op'] += 1
                    for index in range(1, len(keys)):
                        if images[deadlock_ops[i - 1]]['op'] < len(ops):
                            break
                        images[deadlock_ops[i]]['op'] += 1
                        images[deadlock_ops[i - 1]]['op'] = 0
                    assert images[deadlock_ops[-1]]['op'] < len(ops)
                return False
            all_matches.append(matches)
        print("do we have corners?", len([x for x in all_matches if len(x) == 2]))
        return len([x for x in all_matches if len(x) == 2]) == 4

    while not run():
        None

    for k in keys:
        op = images[k]['op']
        images[k]['data'] = ops[op](images[k]['data'])

    for matches in all_matches:
        for match in matches:
            key_i = match[0]
            key_j = match[1]
            borders_i = get_borders(images[key_i]['data'])
            borders_j = get_borders(images[key_j]['data'])
            for bi in borders_i:
                for bj in borders_j:
                    if bi == bj:
                        set_neigh(images, key_i, borders_i.index(bi), key_j)



def get_corners(images):
    corner_list = []
    for k, v in images.items():
        count = 0
        for b in v['neigh']:
            if b is not None:
                count += 1
        if count == 2:
            corner_list.append(k)
    return corner_list


def image_rotated(data):
    new_data = [""] * len(data[0])
    line_len = len(data[0])
    lines_len = len(data)
    for line_pos in range(0, line_len):
        for p in range(0, lines_len):
            c = data[lines_len - p - 1][line_pos]
            new_data[line_pos] += c
    return new_data


def image_flip_horizontal(data):
    new_data = []
    for line in data:
        new_line = line[::-1]
        new_data.append(new_line)
    return new_data


def image_flip_vertical(data):
    new_data = data[::-1]
    return new_data


test = '''.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###'''


def has_monster(sea_data):
    monsters = [seamonster,
                image_flip_vertical(seamonster),
                image_flip_horizontal(seamonster),
                image_flip_horizontal(image_flip_vertical(seamonster)),
                image_rotated(seamonster),
                image_flip_vertical(image_rotated(seamonster)),
                image_flip_horizontal(image_rotated(seamonster)),
                image_flip_horizontal(image_flip_vertical(image_rotated(seamonster)))]

    monsters_found = []

    sea_height = len(sea_data)
    sea_width = len(sea_data[0])

    for monster in monsters:
        monster_height = len(monster)
        monster_width = len(monster[0])

        for j in range(0, sea_height - monster_height):
            for i in range(0, sea_width - monster_width):
                found = True
                for jj in range(0, monster_height):
                    sea_line = sea_data[j + jj]
                    monster_line = monster[jj]
                    for ii in range(0, len(monster_line)):
                        m = monster_line[ii]
                        s = sea_line[i + ii]
                        if m == '#' and s != '#':
                            found = False
                            break
                        #print(s, end='')
                    #print(" ")
                    if not found:
                        break
                if found:
                    monsters_found.append((i, j, monsters.index(monster)))
    print(monsters_found)
    return monsters_found


def calc_roughness(data, monsters):
    def calc_sharps(image):
        sharps = 0
        for line in image:
            sharps += sum(map(lambda x: 1 if '#' in x else 0, line))
        return sharps

    print(calc_sharps(data) - monsters * calc_sharps(seamonster))


def order_tiles(images):
    top_left = None
    for cor in get_corners(images):
        if images[cor]['neigh'][0] is None and images[cor]['neigh'][3] is None:
            top_left = cor
            break

    assert top_left is not None

    left_one = top_left
    line_one = top_left
    grid = []

    while True:
        line = []
        while True:
            if left_one is None:
                grid.append(line)
                break
            line.append(left_one)
            left_one = images[left_one]['neigh'][1]
        line_one = images[line_one]['neigh'][2]
        left_one = line_one
        if left_one is None:
            break

    print("***")
    for line in grid:
        for cell in line:
            print(cell, end=" ")
        print(" ")

    print("***")
    for line in grid:
        line_count = len(images[list(images.keys())[0]]['data'])
        for ln in range(0, line_count):
            for cell in line:
                print(images[cell]['data'][ln], end="")
                print(" ", end=" ")
            print(" ")
        print(" ")

    return grid


def make_sea_image(images, grid):
    data = []
    for ln in grid:
        for index in range(1, len(images[ln[0]]['data']) - 1):
            line = ""
            for cell in ln:
                content = images[cell]['data'][index][1:-1]
                line += content
            data.append(line)

    print("\n".join(data))

    return data


def make_image(image_data):
    return {'data': image_data,
            'neigh': [None] * 4,
            'op': 0}


def manage_images(data):
    key = None
    image_data = None
    images = {}
    for line in data:
        if len(line) == 0:
            if key is not None:
                images[key] = make_image(image_data)
            key = None
            continue
        if key is None:
            key = line.split(' ')[1][:-1]
            image_data = []
        else:
            image_data.append(line)

    if key is not None:
        images[key] = make_image(image_data)

    match_all(images)

    mul = 1
    for m in get_corners(images):
       mul *= int(m)
    print("corners:", mul)

    grid = order_tiles(images)

    #grid = [['1951','2311','3079'],
    #     ['2729','1427','2473'],
    #    ['2971','1489','1171']]

    sea_image = make_sea_image(images, grid)

    mon = has_monster(sea_image)
    if mon is not None:
        print("Monster!", mon)
    else:
        print("No Monster")

    calc_roughness(sea_image, len(mon))


