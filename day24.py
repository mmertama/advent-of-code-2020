example = '''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew'''

directions = {
    'e': (-1, 1, 0),
    'se': (-1, 0, 1),
    'sw': (0, -1, 1),
    'w': (1, -1, 0),
    'nw': (1, 0, -1),
    'ne': (0, 1, -1)}


def get_tile_address(position, instruction):
    direction = instruction[0]
    new_position = (
            position[0] + direction[0],
            position[1] + direction[1],
            position[2] + direction[2])
    if len(instruction) == 1:
        return new_position
    return get_tile_address(new_position, instruction[1:])


def get_black_tiles(data):
    instructions = []
    for line in data:
        i = 0
        instruction = []
        while i < len(line):
            c1 = line[i]
            i += 1
            if c1 == 'e' or c1 == 'w':
                instruction.append(directions[c1])
            else:
                c2 = line[i]
                instruction.append(directions[c1 + c2])
                i += 1
        instructions.append(instruction)

    black_tiles_list = []
    origin = (0, 0, 0)
    for instruction in instructions:
        tile = get_tile_address(origin, instruction)
        if tile in black_tiles_list:
            black_tiles_list.remove(tile)
        else:
            black_tiles_list.append(tile)
    return black_tiles_list


def get_neighbors(tile):
    return [(
        tile[0] + d[0],
        tile[1] + d[1],
        tile[2] + d[2]) for d in directions.values()]


def set_tiles(data):
    tiles = get_black_tiles(data)
    print("Black tiles count:", len(tiles))


def set_tiles_daily(data, days):
    black_tiles = frozenset(get_black_tiles(data))
    for day in range(0, days):
        flippable_black = []
        flippable_white = []
        all_neighbors = set()
        for tile in black_tiles:
            neighbors = get_neighbors(tile)
            black_neighbors = [x for x in neighbors if x in black_tiles]
            black_neighbors_count = len(black_neighbors)
            if black_neighbors_count == 0 or black_neighbors_count > 2:
                if tile not in flippable_black:
                    flippable_black.append(tile)
            for n in neighbors:
                all_neighbors.add(n)
        white_neighbors = [x for x in all_neighbors if x not in black_tiles]
        for tile in white_neighbors:
            neighbors = get_neighbors(tile)
            black_neighbors = [x for x in neighbors if x in black_tiles]
            if len(black_neighbors) == 2:
                if tile not in flippable_white:
                    flippable_white.append(tile)

        non_removed = [p for p in black_tiles if p not in flippable_black]
        black_tiles = frozenset(flippable_white + non_removed)

    print("Day", days, len(black_tiles))

