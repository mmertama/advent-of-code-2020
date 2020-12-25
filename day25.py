import math
example='''5764801
17807724'''


def get_loop_size(pub):
    loops = 1
    v0 = 1
    while True:
        v0 *= 7
        v0 %= 20201227
        if v0 == pub:
            break
        loops += 1
    return loops


def verify(loop_size, subject_number):
    v0 = 1
    for loop in range(0, loop_size):
        v0 *= subject_number
        v0 %= 20201227
    return v0


def crack_the_key(input_keys):
    card = int(input_keys[0])
    door = int(input_keys[1])

    card_loop_size = get_loop_size(card)
    v0 = verify(card_loop_size, door)

    print("code:", v0)

