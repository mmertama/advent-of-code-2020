## day 3

example='''..##.......
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
