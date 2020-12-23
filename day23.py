
example = "389125467"
data = "624397158"


#class CircleBuffer:
#    def __init__(self, data):
#        self.array = data
#
#    def rotate_left(self, count):
#        return self.array[count:] + self.array[:count]
#
#    def index(selfs, data):

def rotate_left(array, count):
    return array[count:] + array[:count]

def iterate(cups, ci, rounds):
    min_cups = min(cups)
    max_cups = max(cups)
    pi_len = len(cups)
    for move in range(0, rounds):
        pi_start = ci + 1

        if pi_start >= pi_len:
            pi_start = 0
        pi_end = pi_start + 3

        if pi_end < pi_len:
            pick = cups[pi_start:pi_end]
        else:
            pick = cups[pi_start:] + cups[:pi_end % pi_len]

        current = cups[ci]
        destination = current - 1
        while True:
            if destination < min_cups:
                destination = max_cups
            if destination not in pick:
                break
            destination -= 1

        print("-- move", move + 1, "--")
        print("cups:",
              ' '.join([str(x) for x in cups[:ci]]),
              '(' + str(current) + ')', ' '.join([str(x) for x in cups[ci + 1:]]))
        #      #' '.join([str(x) for x in cups[ci + 1:20]]) + '...' +
        #      #' '.join([str(x) for x in cups[-20:]]))
        print("pick up:", ','.join([str(x) for x in pick]))

        #print("destination:", destination, "at", cups.index(destination), "ci", ci, "current", current)

        #if pups:
        #    stop_at = len(cups) / 3
        #    fill0 = [x for r in range(pups, stop_at, 3)]
        #    fill1 = [x for r in range(cups[-1], pups, -3)]
        #    pups = [cups[:pups]] + []
        #print("")

        cups = [p for p in cups if p not in pick]
        di = cups.index(destination)

        for d in range(0, len(pick)):
            at_pos = di + 1 + d
            cups.insert(at_pos, pick[d])

        new_ci = cups.index(current)
        cups = rotate_left(cups, new_ci - ci if new_ci - ci else ci - new_ci)

        ci += 1
        #if cups[ci] >= early_end:
        #    pups = True
            #break
        if ci >= pi_len:
            ci = 0

    return cups, ci, move + 1


def play_cups_order(input_data, rounds):
    cups = [int(x) for x in input_data]
    cups, _, r = iterate(cups, 0, rounds)
    assert r == rounds
    order = []
    at = cups.index(1)
    for c in range(0, len(cups) - 1):
        at += 1
        order.append(str(cups[at % len(cups)]))
    print("order", order, ''.join(order))


def play_cups_find(input_data, rounds, input_len):
    cups = [int(x) for x in input_data]
    cups += [x for x in range(len(input_data), input_len + 1)]
    cups, ci, r = iterate(cups, 0, rounds)
    at = cups.index(1)
    m1 = at % len(cups)
    m2 = at % len(cups)
    print("stars at", m1, m2, m1 * m2)

