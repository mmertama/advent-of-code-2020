example1 = "0,3,6"
data = "0,13,16,17,1,10,6"


def play_memory(line):
    input_list = [int(x) for x in line.split(',')]
    memory = {x: input_list.index(x) + 1 for x in input_list[:-1]}
    number_spoken = input_list[-1]
    turn = len(input_list)
    while turn < 2020:
        turn += 1
        if number_spoken not in memory:
            memory[number_spoken] = turn - 1
            number_spoken = 0
        else:
            new_number_spoken = (turn - 1) - memory[number_spoken]
            memory[number_spoken] = turn - 1
            number_spoken = new_number_spoken
    print("at:", turn, "number spoken:", number_spoken)

