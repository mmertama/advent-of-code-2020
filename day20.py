import itertools

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

seamonster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]


def generate_borders(data):
    image = data['data']
    data['borders'][0] = [x for x in image[0]]
    data['borders'][1] = [image[x][-1] for x in range(0, len(image))]
    data['borders'][2] = [image[-1][x] for x in range(0, len(image))]
    data['borders'][3] = [image[x][0] for x in range(0, len(image))]


def rotate(images, key):
    neighs = images[key]['neigh']
    tmp = neighs[3]
    neighs[3] = neighs[2]
    neighs[2] = neighs[1]
    neighs[1] = neighs[0]
    neighs[0] = tmp
    neighs = images[key]['borders']
    tmp = neighs[3]
    neighs[3] = neighs[2]
    neighs[2] = neighs[1]
    neighs[1] = neighs[0]
    neighs[0] = tmp
    images[key]['borders'] = neighs
    images[key]['orientation'] += 1
    images[key]['orientation'] %= 4


def set_neigh(images, key, pos, neigh):
    n = images[key]['neigh']
    if neigh == '1171':
        print("nka")
    if n[pos] is not None:
        print("HERE", key, neigh, pos, images[key]['orientation'], images[neigh]['orientation'], n)
    #pos -= images[key]['orientation']
    #pos %= 4
    if n[pos] is not None:
        print("GERE", key, neigh, pos, images[key]['orientation'], images[neigh]['orientation'], n)
    #assert n[pos] is None
    n[pos] = neigh


def do_match(images, key_i, key_j):
    matches = []

    def loop():
        nonlocal matches
        borders_i = images[key_i]['borders']
        borders_j = images[key_j]['borders']
        matches = []
        for bi in range(0, len(borders_i)):
            for bj in range(0, len(borders_j)):
                if borders_i[bi] == borders_j[bj]:
                    matches.append((bi, bj))
                elif borders_i[bi][::-1] == borders_j[bj]:
                    #print("flippable", key_i, key_j, bi, bj)
                    if bi == 0 or bi == 2:
                        flip_horizontal(images, key_i)
                    else:
                        flip_vertical(images, key_i)
                    return False
                    #matches.append((bi, bj))
                    #images[key_i]['flip'].add(key_j)
        return True

    while not loop():
        None

    for m in matches:
        set_neigh(images, key_i, m[0], key_j)
        set_neigh(images, key_j, m[1], key_i)
        #rotate(images, key_i, m[0], key_j)
        #rotate(images, key_j, m[1], key_i)
    return True


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


def image_rotated(data, t):
    for r in range(0, t):
        array = [[] for x in range(0, len(data))]
        for line in data:
            ln = 0
            for item in data:
                array[ln].append(item)
                ln += 1
        new_data = []
        for d in array:
            new_data.append(''.join(d))
        data = new_data
    return new_data


def image_flip_horizontal(data):
    new_data = []
    for line in data:
        new_line = line[::-1]
        new_data.append(new_line)
    return data


def image_flip_vertical(data):
    new_data = data[::-1]
    return data


def flip_horizontal(images, key):
    data = images[key]['data']
    new_data = []
    for line in data:
        new_line = line[::-1]
        new_data.append(new_line)
    images[key]['data'] = new_data
    generate_borders(images[key])


def flip_vertical(images, key):
    data = images[key]['data']
    new_data = data[::-1]
    images[key]['data'] = new_data
    generate_borders(images[key])


'''
def flip(images, key):
    data = images[key]['data']
    new_data = []
    for i in range(1, len(data) + 1):
        line = data[len(data) - i][::-1]
        new_data.append(line)
    images[key]['data'] = new_data
    generate_borders(images[key])

    neighs = images[key]['neigh']

    neighs[1], neighs[3] = neighs[3], neighs[1]
    neighs[2], neighs[0] = neighs[0], neighs[2]

    #flipped = images[key]['flip']

    #print("flip", key)

    #images[key]['flip'] = []

    #for f in flipped:
    #    flip(images, f)

    #neigh = [x for x in images[key]['neigh'] if x is not None]
    #images[key]['flip'] = set(x for x in neigh if x not in images[key]['flip'])
'''


def has_monster(data, i, j):
    for jj in range(0, len(seamonster)):
        sea_line = data[j + jj]
        seamonster_line = seamonster[jj]
        for ii in range(0, len(seamonster_line)):
            if seamonster_line[ii] == '#' and sea_line[i + ii] != '#':
                return False
    return True


def order_tiles(images):

    def rotate_all():
        failed = {}
        for im in images.keys():
            neigh = images[im]['neigh']
            failed[im] = 0
            for r in range(0, 4):
                if neigh[r] is not None:
                    nim = images[neigh[r]]['neigh']
                    if r == 0 and im != nim[2]:
                        failed[im] += 1
                    if r == 1 and im != nim[3]:
                        failed[im] += 1
                    if r == 2 and im != nim[0]:
                        failed[im] += 1
                    if r == 3 and im != nim[1]:
                        failed[im] += 1

        worst = max(failed, key=failed.get)
        nl = len([x for x in images[worst]['neigh'] if x is not None])
        print(worst, failed[worst], nl)
        if failed[worst] == nl:
            rotate(images, worst)
            return False
        return True

    while not rotate_all():
        None

    def flip_all():
        failed_v = {}
        failed_h = {}
        for im in images.keys():
            neigh = images[im]['neigh']
            failed_v[im] = 0
            failed_h[im] = 0
            for r in range(0, 4):
                if neigh[r] is not None:
                    nim = images[neigh[r]]['neigh']
                    if r == 0 and im != nim[2]:
                        failed_h[im] += 1
                    if r == 1 and im != nim[3]:
                        failed_v[im] += 1
                    if r == 2 and im != nim[0]:
                        failed_h[im] += 1
                    if r == 3 and im != nim[1]:
                        failed_v[im] += 1

        worst_v = max(failed_h, key=failed_v.get)
        worst_h = max(failed_v, key=failed_h.get)
        nv = images[worst_v]['neigh']
        nh = images[worst_v]['neigh']
        nl_v = len([x for x in range(0, len(nv)) if nv[x] is not None and x == 0 or x == 2])
        nl_h = len([x for x in range(0, len(nh)) if nh[x] is not None and x == 1 or x == 3])
        print(worst_v, worst_h,
              failed_v[worst_v], failed_h[worst_h],
              nl_v, nl_h)
        if failed_v[worst_v] == nl_v:
            neighs = images[worst_v]['neigh']
            neighs[1], neighs[3] = neighs[3], neighs[1]
            return False
        if failed_h[worst_h] == nl_h:
            neighs = images[worst_v]['neigh']
            neighs[2], neighs[0] = neighs[0], neighs[2]
            return False
        return True

    while not flip_all():
        None


    pos = {0: (0, 3),
           1: (0, 1),
           2: (2, 1),
           3: (2, 3)}

    top_left = None
    for cor in get_corners(images):
        if images[cor]['neigh'][0] == None and images[cor]['neigh'][3] == None:
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

    data = []
    for ln in grid:
        cell = ln[0]
        for d in range(1, len(images[cell]['data']) - 1):
            content = images[cell]['data'][d][1:-1]
            data.append(content)
        print("C", cell)
    print(len(data))
    ln_no = 0
    for ln in grid:
        for c in range(1, len(ln)):
            if ln_no >= len(data):
                ln_no = 0
            cell = ln[c]
            for d in range(1, len(images[cell]['data']) - 1):
                content = images[cell]['data'][d][1:-1]
                data[ln_no] += content
                ln_no += 1
    print("\n".join(data))
    
    seamonster_height = len(seamonster)
    seamonster_width = len(seamonster[1])

    test_array = [lambda _:None,
                  lambda x: image_rotated(x, 1),
                  lambda x: image_rotated(x, 2),
                  lambda x: image_rotated(x, 3),
                  lambda x: image_flip_horizontal(x),
                  lambda x: image_flip_vertical(x)]

    tests = []
    for r in range(1, len(test_array)):
        tests.append(itertools.combinations(test_array, r))

    for test in tests:
        test_data = data
        for puff in test:
            test_data = puff[0](test_data)
            assert test_data is not None
        for j in range(0, len(test_data) - seamonster_height):
            line = test_data[j]
            for i in range(0, len(line) - seamonster_width):
                if has_monster(test_data, i, j):
                    print("monster", i, j)
    

def make_image(image_data):
    return {'data': image_data, 'borders': [None] * 4, 'neigh': [None] * 4, 'orientation': 0}


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

    for image in images.values():
       generate_borders(image)

    keys = [x for x in images.keys()]

    def run():
        for i in range(0, len(keys)):
            for j in range(i + 1, len(keys)):
                if not do_match(images, keys[i], keys[j]):
                    return False
        return True

    run()

    mul = 1
    for m in get_corners(images):
       mul *= int(m)
    print("corners:", mul)

    order_tiles(images)


