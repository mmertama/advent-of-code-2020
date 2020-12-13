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
    #ids = [0 if x == 'x' else int(x) for x in data[1].split(',')]
    ids = [7, 13, 0, 0, 59, 0, 31, 19]
    zipped = zip([x for x in ids if x > 0], [ids.index(x) for x in ids if x > 0])
    id_values = sorted(zipped, reverse=True)
    #ids_values =
    #ids_values.sort(reverse=True)
    #ids_deltas =
    #ids_deltas.sort(key=ids_values.__getitem__, reverse=True)
    #values = {v: v for v in ids if v != 0}

    id_values.pop(0)
    max_val = max(ids)
    max_val_index = ids.index(max_val)
    t = max_val - max_val_index
    r = range(0, len(id_values))
    while True:
        #delta = 0
        #ii = [0] * len(ids_values)
        found = True
        for i in id_values:
            if (t + i[1]) % i[0] > 0:
                found = False
                break
            #ii[i] = d
        if found:
            print(t)
            return
        #print(t, delta, ii)
        t += max_val


def find_timestamp_t(data):
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












