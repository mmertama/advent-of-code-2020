import day1
import day2
import day3
import day4
import day5


def read_local_lines(str):
    return str.splitlines()


def read_remote_lines(fn):
    lines = []
    with open(fn) as f:
        for l in f:
            lines.append(l.rstrip())
    return lines


if __name__ == "__main__":
    #day1.find_two_factors(read_local_lines(day1.example))
    day1.find_two_factors(read_remote_lines('data/input.txt'))
    #day1.find_three_factors(read_local_lines(day1.example))
    day1.find_three_factors(read_remote_lines('data/input.txt'))
    #day2.validate_passwords(read_local_lines(day2.example))
    day2.validate_passwords(read_remote_lines('data/input2.txt'))
    #day2.validate_passwords_2(read_local_lines(day2.example))
    day2.validate_passwords_2(read_remote_lines('data/input2.txt'))
    #day3.navigate_thru_trees(3, 1, read_local_lines(day3.example))
    day3.navigate_thru_trees(3, 1, read_remote_lines('data/input3.txt'))
    #day3.navigate_thru_trees2(read_local_lines(day3.example))
    day3.navigate_thru_trees2(read_remote_lines('data/input3.txt'))
    #day4.check_passports_loose(read_local_lines(day4.example))
    day4.check_passports_loose(read_remote_lines('data/input4.txt'))
    #day4.check_passports_strict(read_local_lines(day4.example))
    #day4.check_passports_strict(read_local_lines(day4.example_invalids))
    #day4.check_passports_strict(read_local_lines(day4.example_valids))
    day4.check_passports_strict(read_remote_lines('data/input4.txt'))
    #day5.find_seat(read_local_lines(day5.example))
    day5.find_seat(read_remote_lines('data/input5.txt'))