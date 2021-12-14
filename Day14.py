from collections import Counter

from helpers import AoCHelper
import time

start_time = time.time()

input_lines = AoCHelper.read_input_lines("day14/test1.txt")

template = input_lines[0]
instructions = {}

for i in range(2, len(input_lines)):
    pos, val = input_lines[i].split(' -> ')
    instructions[pos] = val

changes = { pos : [pos[0] + instructions[pos], instructions[pos] + pos[1]] for pos in instructions}

c = Counter()

for ins in instructions:
    c[ins] = 1 if ins in template else 0

for n in range(10):
    c_new = Counter()

    for ins in instructions:
        new_occurences = 0

        for change in changes:
            if ins in changes[change]:
                new_occurences += 1 * c[change]

        c_new[ins] += new_occurences

    c = c_new

    print(f"Finished round {n}")

max_occurences = max(c.values())
min_occurences = min(c.values())
part_one_res = max_occurences - min_occurences
print(part_one_res)


print("--- %s seconds ---" % (time.time() - start_time))