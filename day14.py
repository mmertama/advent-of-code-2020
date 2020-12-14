import re

example = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''

example2 = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''


def init_program(data):
    memory = {}
    mask = None
    for line in data:
        m = re.match(r'mask\s*=\s(.+)', line)
        if m:
            mask = list(m[1])
            continue
        m = re.match(r'mem\[(\d+)\]\s*=\s*(\d+)', line)
        assert m
        address = m[1]
        value = bin(int(m[2]))[2:]
        bits = ['0'] * 36
        for bi in range(0, len(value)):
            bits[36 - len(value) + bi] = value[bi]
        result = ['0'] * 36
        for b in range(0, 36):
            result[b] = '0' if mask[b] == '0' else ('1' if mask[b] == '1' else bits[b])
        memory[address] = result

    sum_val = 0
    for v in memory.values():
        bits = ''.join(v)
        integer = int(bits, 2)
        sum_val += integer
    print("init value:", sum_val)


def make_addresses(pos, mask, addr):
    result = addr[0:pos]
    result.extend([0] * (36 - pos))
    for b in range(pos, 36):
        if mask[b] == '0':
            result[b] = addr[b]
        elif mask[b] == '1':
            result[b] = '1'
        else:
            r0 = result[:b]
            r1 = result[:b]
            r0.append('0')
            r1.append('1')
            r0.extend(addr[b + 1:])
            r1.extend(addr[b + 1:])
            out = []
            out.extend(make_addresses(b + 1, mask, r0))
            out.extend(make_addresses(b + 1, mask, r1))
            return out
    return [result]


def init_program_2(data):
    memory = {}
    mask = None
    for line in data:
        m = re.match(r'mask\s*=\s(.+)', line)
        if m:
            mask = list(m[1])
            continue
        m = re.match(r'mem\[(\d+)\]\s*=\s*(\d+)', line)
        assert m
        address = bin(int(m[1]))[2:]
        value = bin(int(m[2]))[2:]

        bits = ['0'] * 36
        for bi in range(0, len(value)):
            bits[36 - len(value) + bi] = value[bi]

        address_bits = ['0'] * 36
        for bi in range(0, len(address)):
            address_bits[36 - len(address) + bi] = address[bi]

        addresses = make_addresses(0, mask, address_bits)

        for a in addresses:
            address_bits = ''.join(a)
            address = int(address_bits, 2)
            memory[address] = bits

    sum_val = 0
    sum_k = 0
    for k, v in memory.items():
        bits = ''.join(v)
        sum_k += int(k)
        integer = int(bits, 2)
        sum_val += integer
    print("init2 value:", sum_val)

