import functools
import sys

example1 = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''


def mismatch(preamble_len, data):
    window = []
    for i in range(0, preamble_len):
        window.append(int(data[i]))

    def find_sum(number):
        for v in range(0, preamble_len):
            for w in range(v + 1, preamble_len):
                mul = window[v] + window[w]
                if mul == number:
                    return True
        return False

    for i in range(preamble_len, len(data)):
        value = int(data[i])
        if not find_sum(value):
            return value, i
        window.pop(0)
        window.append(value)
    return None


def find_mismatch(preamble_len, data):
    value, i = mismatch(preamble_len, data)
    print("not found", value, "at", i)


def find_contiguous_range(preamble_len, data):
    value, i = mismatch(preamble_len, data)
    low = 0
    high = 1
    sum_value = int(data[low])
    while high < len(data):
        new_sum = sum_value + int(data[high])
        if new_sum == value:
            min_in_range = functools.reduce(lambda a, x: min(a, int(x)), data[low:high], sys.maxsize)
            max_in_range = functools.reduce(lambda a, x: max(a, int(x)), data[low:high], 0)
            print("contiguous range:", low, '-', high, min_in_range,'+', max_in_range,'=', min_in_range + max_in_range)
            return
        elif new_sum < value:
            high += 1
            sum_value = new_sum
        elif new_sum > value:
            low += 1
            high = low + 1
            sum_value = int(data[low])
            assert sum_value < value
        assert low < high
    assert False

