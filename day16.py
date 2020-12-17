import re
import functools

example1 = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''

example2 = '''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''


def ticket_scan(data):
    section = 0
    info = {}
    my_ticket = None
    nearby_tickets = []
    for line in data:
        if len(line) == 0:
            section += 1
            continue
        if section == 0:
            m = re.match(r'\s*(.*)\s*:\s*(\d+)-(\d+)\s+or\s+(\d+)-(\d+)', line)
            assert m
            info[m[1]] = [(int(m[2]), int(m[3])), (int(m[4]), int(m[5]))]
        if section == 1:
            if re.match(r'(your ticket:)', line):
                continue
            my_ticket = [int(x) for x in line.split(',')]
        if section == 2:
            if re.match(r'(nearby tickets:)', line):
                continue
            nearby_tickets.append([int(x) for x in line.split(',')])

    invalid_values = []
    validated_tickets = []
    for ticket in nearby_tickets:
        valid_ticket = True
        for value in ticket:
            valid = False
            for limits in info.values():
                min0 = limits[0][0]
                max0 = limits[0][1]
                min1 = limits[1][0]
                max1 = limits[1][1]
                if min0 <= value <= max0 or min1 <= value <= max1:
                    valid = True
            if not valid:
                invalid_values.append(value)
                valid_ticket = False
        if valid_ticket:
            validated_tickets.append(ticket)
    error_rate = functools.reduce(lambda a, x: a + x, invalid_values, 0)
    return error_rate, validated_tickets, my_ticket, info


def ticket_errors_scan(data):
    result = ticket_scan(data)
    print("error rate:", result[0])


def find_my_ticket_departure(data):
    e, tickets, my_ticket, info = ticket_scan(data)

    results = {}

    for key, limits in info.items():
        validates = set()
        for index in range(0, len(info)):
            valid = True
            for ticket in tickets:
                value = ticket[index]
                min0 = limits[0][0]
                max0 = limits[0][1]
                min1 = limits[1][0]
                max1 = limits[1][1]
                if not (min0 <= value <= max0 or min1 <= value <= max1):
                    valid = False
                    break
            if valid:
                validates.add(index)
        results[key] = validates

    eliminated_results = {}
    while True:
        found = None
        for k, v in results.items():
            if len(v) == 1:
                found = v.pop()
                eliminated_results[k] = found
                break
        if not found:
            break
        for k in results.keys():
            if found in results[k]:
                results[k].remove(found)
    mul = 1
    for k, v in eliminated_results.items():
        if k.startswith("departure"):
            mul *= my_ticket[v]
    print("departure check:", mul)
