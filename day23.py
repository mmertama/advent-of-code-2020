
example = "389125467"
data = "624397158"


class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node


class CircleList:
    def __init__(self, array):
        self.node = None
        self.count = len(array)
        self.index = {}
        for x in reversed(array):
            self.node = Node(x, self.node)
            self.index[x] = self.node
        self.at(self.count - 1).next = self.node
        self.index_cache = self.node

    def at(self, index):
        s = self.node
        for r in range(0, index):
            s = s.next
        return s

    def find(self, value):
        return self.index[value]


def iterate(cups, ci, rounds):
    min_cups = min(cups)
    max_cups = max(cups)
    linked = CircleList(cups)
    c_item = linked.at(0)
    indicator = rounds / 100
    for move in range(0, rounds):

        picked0 = c_item.next
        picked1 = picked0.next
        picked2 = picked1.next

        c_current = c_item.value
        c_destination = c_current - 1

        while True:
            if c_destination < min_cups:
                c_destination = max_cups
            if c_destination != picked0.value and \
                    c_destination != picked1.value and \
                    c_destination != picked2.value:
                break
            c_destination -= 1

        '''
        print("-- move", move + 1, "--")
        print("cups:",
              ' '.join([str(x) for x in cups[:ci]]),
              '(' + str(c_item.value) + ')', ' '.join([str(x) for x in cups[ci + 1:]])
              if linked.count < 50 else
              ' '.join([str(x) for x in cups[ci + 1:20]]) + '...' +
              ' '.join([str(x) for x in cups[-20:]]))
        print("pick up:", ','.join([str(x) for x in [picked0.value, picked1.value, picked2.value]]))
        print("destination:", c_destination)
        '''

        d_node = linked.find(c_destination)
        c_item.next = picked2.next
        picked2.next = d_node.next
        d_node.next = picked0

        c_item = c_item.next
        if move % indicator == 0:
            print('.', end='', flush=True)
    print("")
    return linked


def play_cups_order(input_data, rounds):
    cups = [int(x) for x in input_data]
    linked = iterate(cups, 0, rounds)
    order = []
    at = linked.find(1)
    for c in range(0, len(cups) - 1):
        at = at.next
        order.append(str(at.value))
    print("order", order, ''.join(order))


def play_cups_find(input_data, rounds, input_len):
    cups = [int(x) for x in input_data]
    cups += [x for x in range(len(input_data) + 1, input_len + 1)]
    linked = iterate(cups, 0, rounds)
    at = linked.find(1)
    m1 = at.next.value
    m2 = at.next.next.value
    print("stars at", m1, m2, m1 * m2)

