from collections import Counter

from helpers import AoCHelper
import time

start_time = time.time()

input_lines = AoCHelper.read_input_lines("day14/input1.txt")

template = input_lines[0]
instructions = {}

for i in range(2, len(input_lines)):
    pos, val = input_lines[i].split(' -> ')
    instructions[pos] = val


def run_game(game_lenght, instructions, template):
    changes = {pos: [pos[0] + instructions[pos], instructions[pos] + pos[1]] for pos in instructions}
    pair_counter = Counter()
    letter_counter = Counter(template)

    for ins in instructions:
        pair_counter[ins] = template.count(ins)

    for n in range(game_lenght):
        c_new = Counter()
        letter_counter += {k : sum(pair_counter[ins] for ins in pair_counter if instructions[ins] == k) for k in instructions.values()}

        for ins in instructions:
            c_new[ins] += sum(pair_counter[change] for change in changes if ins in changes[change])

        pair_counter = c_new

    return max(letter_counter.values()) - min(letter_counter.values())


part_one_res = run_game(10, instructions, template)
assert part_one_res == 2068
print(f"Part 1: {part_one_res}")

part_two_res = run_game(40, instructions, template)
assert part_two_res == 2158894777814
print(f"Part 2: {part_two_res}")

print("--- %s seconds ---" % (time.time() - start_time))