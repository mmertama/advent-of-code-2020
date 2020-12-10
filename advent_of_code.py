import day1
import day2
import day3
import day4
import day5
import day6
import day7
import day8
import day9
import day10


def read_local_lines(str):
    return str.splitlines()


def read_remote_lines(fn):
    lines = []
    with open(fn) as f:
        for l in f:
            lines.append(l.rstrip())
    return lines


if __name__ == "__main__":
    '''
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
    #day6.check_custom_declaration_forms_any(read_local_lines(day6.example))
    day6.check_custom_declaration_forms_any(read_remote_lines('data/input6.txt'))
    #day6.check_custom_declaration_forms_all(read_local_lines(day6.example))
    day6.check_custom_declaration_forms_all(read_remote_lines('data/input6.txt'))
    #day7.luggage_processor(read_local_lines(day7.example), 'shiny gold')
    day7.luggage_processor(read_remote_lines('data/input7.txt'), 'shiny gold')
    #day7.luggage_processor_content(read_local_lines(day7.example), 'shiny gold')
    #day7.luggage_processor_content(read_local_lines(day7.example2), 'shiny gold')
    day7.luggage_processor_content(read_remote_lines('data/input7.txt'), 'shiny gold')
    #day8.detect_loop(read_local_lines(day8.example))
    day8.detect_loop(read_remote_lines('data/input8.txt'))
    #day8.detect_invalid_instruction(read_local_lines(day8.example))
    day8.detect_invalid_instruction(read_remote_lines('data/input8.txt'))
    #day9.find_mismatch(5, read_local_lines(day9.example1))
    day9.find_mismatch(25, read_remote_lines('data/input9.txt'))
    #day9.find_contiguous_range(5, read_local_lines(day9.example1))
    day9.find_contiguous_range(25, read_remote_lines('data/input9.txt'))
    '''
    #day10.find_jolts(read_local_lines(day10.example1))
    #day10.find_jolts(read_local_lines(day10.example2))
    day10.find_jolts(read_remote_lines('data/input10.txt'))

    #day10.find_jolt_permutations(read_local_lines(day10.example1))
    #day10.find_jolt_permutations(read_local_lines(day10.example2))
    day10.find_jolt_permutations(read_remote_lines('data/input10.txt'))