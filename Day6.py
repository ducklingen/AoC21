from helpers import AoCHelper

input = AoCHelper.read_input_lines("day6/input1.txt")


def init_dictionary(input_line):
    fishs = AoCHelper.extract_numbers(input_line)[0]
    fish_dict = {}

    for n in range(9):
        fish_dict[n] = len([fish for fish in fishs if fish == n])

    return fish_dict

def run_simulation(lenght, fish_dict):
    for i in range(lenght):
        new_fish_dict = {}

        for key in fish_dict:
            if key == 0:
                new_fish_dict[8] = fish_dict[0]
                new_fish_dict[6] = fish_dict[0] + fish_dict[7]

            if key > 0 and key != 7:
                new_fish_dict[key - 1] = fish_dict[key]

        fish_dict = new_fish_dict

    return fish_dict

dict = init_dictionary(input)
part_one_dict = run_simulation(80, dict)
part_one_res = sum([part_one_dict[k] for k in range(9)])
assert part_one_res == 360268
print(f"Part one: {part_one_res}")

dict = init_dictionary(input)
part_two_dict = run_simulation(256, dict)
part_two_res = sum([part_two_dict[k] for k in range(9)])
assert part_two_res == 1632146183902
print(f"Part one: {part_two_res}")