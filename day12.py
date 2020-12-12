
example = '''F10
N3
F7
R90
F11'''


def navigation_distance(data):
    we = 0
    ns = 0
    directions = ['E', 'S', 'W', 'N']

    def move(d, m):
        nonlocal ns, we
        if d == 'N':
            ns -= m
        if d == 'S':
            ns += m
        if d == 'E':
            we += m
        if d == 'W':
            we -= m

    current_direction = 0

    for line in data:
        op = line[:1]
        pa = int(line[1:])
        if op in directions:
            move(op, pa)
        if op == 'L':
            tl = current_direction - int(pa / 90)
            tr = tl % 4
            current_direction = tl if tl >= 0 else tr
            assert 0 <= current_direction < len(directions)
        if op == 'R':
            tr = current_direction + int(pa / 90)
            tl = tr % 4
            current_direction = tr if tr < 4 else tl
            assert 0 <= current_direction < len(directions)
        if op == 'F':
            move(directions[current_direction], pa)

    print("Position is", ns, we, "Manhattan distance:", abs(ns + we))


def navigation_distance_waypoint(data):
    waypoint_we = 10
    waypoint_ns = -1

    we = 0
    ns = 0

    directions = ['E', 'S', 'W', 'N']

    def move(d, m):
        nonlocal waypoint_ns, waypoint_we
        if d == 'N':
            waypoint_ns -= m
        if d == 'S':
            waypoint_ns += m
        if d == 'E':
            waypoint_we += m
        if d == 'W':
            waypoint_we -= m

    def rotate(r):
        nonlocal waypoint_ns, waypoint_we
        if r == 1:
            waypoint_we, waypoint_ns = waypoint_ns * -1, waypoint_we
        if r == 2:
            waypoint_we, waypoint_ns = waypoint_we * -1, waypoint_ns * -1
        if r == 3:
            waypoint_we, waypoint_ns = waypoint_ns, waypoint_we * -1

    for line in data:
        op = line[:1]
        pa = int(line[1:])
        if op in directions:
            move(op, pa)
        if op == 'L':
            r = int(pa / 90)
            rotate(4 - r)
        if op == 'R':
            r = int(pa / 90)
            rotate(r)

        if op == 'F':
            we += waypoint_we * pa
            ns += waypoint_ns * pa

    print("Position using waypoints is", ns, we, "Manhattan distance:", abs(ns) + abs(we))




