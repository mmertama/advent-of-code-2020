
def print_grid(grid):
    minz = min(grid.keys())
    maxz = max(grid.keys())
    miny = 0
    maxy = 0
    minx = 0
    maxx = 0
    for z, planes in grid.items():
        if len(planes):
            miny = min(miny, min(planes))
            maxy = max(maxy, max(planes))
        for lines in grid[z].values():
            if len(lines):
                minx = min(minx, min(lines))
                maxx = max(maxx, max(lines))
    for z in range(minz, maxz + 1):
        print(z, minx, '-', maxx)
        for y in range(miny, maxy + 1):
            print((str(y).ljust(3)), end='')
            for x in range(minx, maxx + 1):
                if z not in grid or y not in grid[z] or x not in grid[z][y]:
                    print(".", end='')
                else:
                    print("#", end='')
            print("")
        print("")


def print_hyper_grid(grid):
    minw = min(grid.keys())
    maxw = max(grid.keys())
    minz = 0
    maxz = 0
    miny = 0
    maxy = 0
    minx = 0
    maxx = 0
    for w, hyper_cube in grid.items():
        minz = min(minz, min(hyper_cube))
        maxz = max(maxz, max(hyper_cube))
        for z, planes in hyper_cube.items():
            if len(planes):
                miny = min(miny, min(planes))
                maxy = max(maxy, max(planes))
            for lines in grid[z].values():
                if len(lines):
                    minx = min(minx, min(lines))
                    maxx = max(maxx, max(lines))

    for w in range(minw, maxw + 1):
        for z in range(minz, maxz + 1):
            print("z=", z, "w=", w)
            for y in range(miny, maxy + 1):
                print((str(y).ljust(3)), end='')
                for x in range(minx, maxx + 1):
                    if w not in grid or z not in grid[w] or y not in grid[w][z] or x not in grid[w][z][y]:
                        print(".", end='')
                    else:
                        print("#", end='')
                print("")
            print("")
        print("")


def print_grid(grid):
    print("***")
    for line in grid:
        for cell in line:
            print(cell, end=" ")
        print(" ")


def print_grid_data(grid, images):
    for line in grid:
        line_count = len(images[list(images.keys())[0]]['data'])
        for ln in range(0, line_count):
            for cell in line:
                print(images[cell]['data'][ln], end="")
                print(" ", end=" ")
            print(" ")
        print(" ")
