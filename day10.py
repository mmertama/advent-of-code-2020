import functools

example1= '''16
10
15
5
1
11
7
19
6
12
4'''

example2 = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''


def build_chain(current_jolt, jolts, pos):
    chain = []
    for i in range(pos, len(jolts)):
        jolt = jolts[i]
        if jolt - current_jolt <= 3:
            chain.append(jolt)
            sub_chain = build_chain(jolt, jolts, i + 1)
            if sub_chain is not None:
                chain.extend(sub_chain)
                return chain
        else:
            return None
    return chain


def find_jolts(data):
    jolts = sorted([int(x) for x in data])
    jolts.append(jolts[-1] + 3)
    chain = build_chain(0, jolts, 0)
    jolt1 = 0
    jolt3 = 0
    chain.insert(0, 0)
    for i in range(1, len(chain)):
        if chain[i - 1] - chain[i] == -1:
            jolt1 += 1
        if chain[i - 1] - chain[i] == -3:
            jolt3 += 1
    print("differences of one jolt:", jolt1, ", three jolt:", jolt3, "mul:", str(jolt1 * jolt3))


def count_build_chains0(current_jolt, jolts, pos):
    if pos == len(jolts):
        return 0
    chains = 0
    for i in range(pos, len(jolts)):
        jolt = jolts[i]
        if jolt - current_jolt <= 3:
            chains += count_build_chains0(jolt, jolts, i + 1)
        else:
            return chains
    return chains + 1


done_calculations = None


def count_build_chains(current_jolt, jolts, pos):
    if pos == len(jolts):
        return 0
    if pos in done_calculations:
        return done_calculations[pos]
    chains = 0
    for i in range(pos, len(jolts)):
        jolt = jolts[i]
        if jolt - current_jolt <= 3:
            chains += count_build_chains(jolt, jolts, i + 1)
        else:
            done_calculations[pos] = chains
            return chains
    done_calculations[pos] = chains + 1
    return chains + 1


def find_jolt_permutations_slow(data):
    jolts = sorted([int(x) for x in data])
    chains = count_build_chains0(0, jolts, 0)
    print("chains:",  chains)


def find_jolt_permutations(data):
    global done_calculations
    done_calculations = {}
    jolts = sorted([int(x) for x in data])
    chains = count_build_chains(0, jolts, 0)
    print("chains:",  chains)