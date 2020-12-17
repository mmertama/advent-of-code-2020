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
import day11
import day12
import day13
import day14
import day15
import day16
import day17

import time


def read_example(str):
    return str.splitlines()


def read_input(fn):
    lines = []
    with open(fn) as f:
        for l in f:
            lines.append(l.rstrip())
    return lines


if __name__ == "__main__":
    '''
    print("day 1")
    #day1.find_two_factors(read_example(day1.example))
    day1.find_two_factors(read_input('data/input.txt'))
    #day1.find_three_factors(read_example(day1.example))
    day1.find_three_factors(read_input('data/input.txt'))

    print("day 2")
    #day2.validate_passwords(read_example(day2.example))
    day2.validate_passwords(read_input('data/input2.txt'))
    #day2.validate_passwords_2(read_example(day2.example))
    day2.validate_passwords_2(read_input('data/input2.txt'))

    print("day 3")
    #day3.navigate_thru_trees(3, 1, read_example(day3.example))
    day3.navigate_thru_trees1(3, 1, read_input('data/input3.txt'))
    #day3.navigate_thru_trees2(read_example(day3.example))
    day3.navigate_thru_trees2(read_input('data/input3.txt'))

    print("day 4")
    # day4.check_passports_loose(read_example(day4.example))
    day4.check_passports_loose(read_input('data/input4.txt'))
    #day4.check_passports_strict(read_example(day4.example))
    #day4.check_passports_strict(read_example(day4.example_invalids))
    #day4.check_passports_strict(read_example(day4.example_valids))
    day4.check_passports_strict(read_input('data/input4.txt'))

    print("day 5")
    #day5.find_seat(read_example(day5.example))
    day5.find_seat(read_input('data/input5.txt'))

    print("day 6")
    #day6.check_custom_declaration_forms_any(read_example(day6.example))
    day6.check_custom_declaration_forms_any(read_input('data/input6.txt'))
    #day6.check_custom_declaration_forms_all(read_example(day6.example))
    day6.check_custom_declaration_forms_all(read_input('data/input6.txt'))

    print("day 7")
    #day7.luggage_processor(read_example(day7.example), 'shiny gold')
    day7.luggage_processor(read_input('data/input7.txt'), 'shiny gold')
    #day7.luggage_processor_content(read_example(day7.example), 'shiny gold')
    #day7.luggage_processor_content(read_example(day7.example2), 'shiny gold')
    day7.luggage_processor_content(read_input('data/input7.txt'), 'shiny gold')

    print("day 8")
    #day8.detect_loop(read_example(day8.example))
    day8.detect_loop(read_input('data/input8.txt'))
    #day8.detect_invalid_instruction(read_example(day8.example))
    day8.detect_invalid_instruction(read_input('data/input8.txt'))

    print("day 9")
    #day9.find_mismatch(5, read_example(day9.example1))
    day9.find_mismatch(25, read_input('data/input9.txt'))
    #day9.find_contiguous_range(5, read_example(day9.example1))
    day9.find_contiguous_range(25, read_input('data/input9.txt'))

    print("day 10")
    #day10.find_jolts(read_example(day10.example1))
    #day10.find_jolts(read_example(day10.example2))
    day10.find_jolts(read_input('data/input10.txt'))
    #day10.find_jolt_permutations(read_example(day10.example1))
    #day10.find_jolt_permutations(read_example(day10.example2))
    day10.find_jolt_permutations(read_input('data/input10.txt'))
    
    print("day 11")
    #day11.seat_occupation_count(read_example(day11.example))
    day11.seat_occupation_count(read_input('data/input11.txt'))
    #day11.seat_occupation_count_sight(read_example(day11.example))
    day11.seat_occupation_count_sight(read_input('data/input11.txt'))
    
    print("day 12")
    #day12.navigation_distance(read_example(day12.example))
    day12.navigation_distance(read_input('data/input12.txt'))
    #day12.navigation_distance_waypoint(read_example(day12.example))
    day12.navigation_distance_waypoint(read_input('data/input12.txt'))
    
    print("day13")
    #day13.find_bus(read_example(day13.example))
    day13.find_bus(read_input('data/input13.txt'))
    #tic = time.perf_counter()
    #day13.find_timestamp(read_example(day13.example5))
    #toc = time.perf_counter()
    #print(f"timed: {toc - tic:0.4f} seconds", flush=True)
    #tic = time.perf_counter()
    #day13.find_timestamp_dummy_but_much_faster(read_example(day13.example5))
    #toc = time.perf_counter()
    #print(f"timed: {toc - tic:0.4f} seconds", flush=True)
    #tic = time.perf_counter()
    day13.find_timestamp(read_input('data/input13.txt'))
    #toc = time.perf_counter()
    #print(f"timed: {toc - tic:0.4f} seconds", flush=True)

    print("day14")
    #day14.init_program(read_example(day14.example))
    day14.init_program(read_input('data/input14.txt'))
    #day14.init_program_2(read_example(day14.example2))
    day14.init_program_2(read_input('data/input14.txt'))

    print("day15")
    #day15.play_memory(day15.example1, 2020)
    day15.play_memory(day15.data, 2020)
    #tic = time.perf_counter()
    day15.play_memory(day15.data, 30000000)
    #toc = time.perf_counter()
    #print(f"timed: {toc - tic:0.4f} seconds", flush=True)
    
    #day16.ticket_errors_scan(read_example(day16.example1))
    day16.ticket_errors_scan(read_input('data/input16.txt'))
    day16.find_my_ticket_departure(read_input('data/input16.txt'))
    '''
    #day17.boot_cubes_3d(read_example(day17.example), 6)
    day17.boot_cubes_3d(read_input('data/input17.txt'), 6)
    #day17.boot_cubes_4d(read_example(day17.example), 6)
    day17.boot_cubes_4d(read_input('data/input17.txt'), 6)
