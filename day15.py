example1 = "0,3,6"
data = "0,13,16,17,1,10,6"


def play_memory_easy_read(line, th):
    input_list = [int(x) for x in line.split(',')]
    memory = {x: input_list.index(x) + 1 for x in input_list[:-1]}
    number_spoken = input_list[-1]
    turn = len(input_list)
    while turn < th:
        turn += 1
        if number_spoken not in memory:
            memory[number_spoken] = turn - 1
            number_spoken = 0
        else:
            new_number_spoken = (turn - 1) - memory[number_spoken]
            memory[number_spoken] = turn - 1
            number_spoken = new_number_spoken
    print("at:", str(turn) + "th", "number spoken:", number_spoken)


def play_memory(line, th):
    input_list = [int(x) for x in line.split(',')]
    memory = [None] * th
    for i in range(0, len(input_list) - 1):
        memory[input_list[i]] = i + 1
    number_spoken = input_list[-1]
    turn = len(input_list)
    for turn in range(len(input_list), th):
        if memory[number_spoken] is None:
            memory[number_spoken] = turn
            number_spoken = 0
        else:
            memory[number_spoken], number_spoken = turn, turn - memory[number_spoken]
    print("at:", str(turn + 1) + "th", "number spoken:", number_spoken)
