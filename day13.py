import functools

example = '''939
7,13,x,x,59,x,31,19'''

example1 = '''0
17,x,13,19'''

example2 = '''0
67,7,59,61'''

example3 = '''0
67,x,7,59,61'''

example4 = '''0
67,7,x,59,61'''

example5 = '''0
1789,37,47,1889'''


def find_bus(data):
    timestamp = int(data[0])
    ids = [int(x) for x in data[1].split(',') if x != 'x']
    timetable = {k: timestamp + (k - timestamp % k) for k in ids}

    earliest = min(timetable, key=timetable.get)
    wait_time = timetable[earliest] - timestamp
    print("earliest:", earliest, "at:", timetable[earliest], "wait time:", wait_time, "wait:", earliest * wait_time)


def find_timestamp_dummy(data):
    ids = [0 if x == 'x' else int(x) for x in data[1].split(',')]
    t = 0
    while True:
        t += 1
        found = True
        for i in range(0, len(ids)):
            if not found or ids[i] == 0:
                continue
            m = (t + i) % ids[i]
            found = found and m == 0
        if found:
            print(t)
            return


def find_timestamp_dummy_but_much_faster(data):
    ids = [0 if x == 'x' else int(x) for x in data[1].split(',')]
    zipped = zip([x for x in ids if x > 0], [ids.index(x) for x in ids if x > 0])
    id_values = sorted(zipped, reverse=True)
    id_values.pop(0)
    max_val = max(ids)
    max_val_index = ids.index(max_val)
    t = max_val - max_val_index
    r = range(0, len(id_values))
    while True:
        found = True
        for i in id_values:
            if (t + i[1]) % i[0] > 0:
                found = False
                break
        if found:
            print(t)
            return
        t += max_val


def find_timestamp(data):
    ids = [0 if x == 'x' else int(x) for x in data[1].split(',')]
    zipped = zip([x for x in ids if x > 0], [ids.index(x) for x in ids if x > 0])
    id_values = sorted(zipped)
    t = id_values[0][0] - id_values[0][1]
    step = id_values[0][0]
    to = 1
    while True:
        if (t + id_values[to][1]) % id_values[to][0] == 0:
            step = 1
            for i in range(0, to + 1):
                step *= id_values[i][0]
            to += 1
            if to == len(id_values):
                print("timestamp", t)
                return
            continue
        t += step














