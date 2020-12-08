import re

example = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''


def parse(pd, data):
    m = re.match(r'\s*(jmp|nop|acc)\s+([+-]\d+)', data[pd])
    assert m
    op = m[1]
    param = int(m[2])
    return op, param


def execute(pc, data, acc):
    lines_visited = set()
    while pc < len(data):
        if pc in lines_visited:
            return False, acc
        op, param = parse(pc, data)
        lines_visited.add(pc)
        if op == 'jmp':
            pc += param
            continue
        elif op == 'acc':
            acc += param
        pc += 1
    return True, acc


def detect_loop(data):
    success, acc = execute(0, data, 0)
    print("acc on loop", acc)


def detect_invalid_instruction(data):
    pd = 0
    instructions_visited = set()
    acc= 0
    while True:
        op, param = parse(pd, data)
        if op == 'jmp':
            if pd in instructions_visited:
                pd += param
                continue
            else:  # nop
                instructions_visited.add(pd)
                success, new_acc = execute(pd + 1, data, acc)
                if success:
                    print("Fix", "\'" + data[pd] + "\'", "at", pd, "did the job, acc:", new_acc)
                    return;
                else:
                    continue # redo this line, with a jump
        elif op == 'nop':
            if pd in instructions_visited:
                None # this is nop
            else:  # jmp
                instructions_visited.add(pd)
                success, new_acc = execute(pd + param, data, acc)
                if success:
                    print("Fix", "\'" + data[pd] + "\'", "at", pd, "did the job, acc:", new_acc)
                    return;
                else:
                    continue
        else:  # op == 'acc'
            acc += param
        pd += 1


