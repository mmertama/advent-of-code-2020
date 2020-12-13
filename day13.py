import functools

example = '''939
7,13,x,x,59,x,31,19'''

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
    print(earliest, timetable[earliest], wait_time, earliest * wait_time)


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


def find_timestamp(data):
    ids = [0 if x == 'x' else int(x) for x in data[1].split(',')]
    #ids = [2, 3, 5]
    ids_values = [x for x in ids if x > 0]
    ids_deltas = [ids.index(x) for x in ids if x > 0]
    #values = {v: v for v in ids if v != 0}

    max_val = max(ids)
    max_val_index = ids.index(max_val)
    t = max_val - max_val_index
    r = range(0, len(ids_values))
    while True:
        delta = 0
        ii = [0] * len(ids_values)
        for i in r:
            d = (t + ids_deltas[i]) % ids_values[i]
            if d > delta:
                delta = d
                break
            ii[i] = d
        if delta == 0:
            print(t)
            return
        #print(t, delta, ii)
        t += max_val












