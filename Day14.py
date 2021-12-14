from collections import Counter

from helpers import AoCHelper
import time

start_time = time.time()

input_lines = AoCHelper.read_input_lines("day14/input1.txt")

template = list(input_lines[0])
instructions = {}

for i in range(2, len(input_lines)):
    pos, val = input_lines[i].split(' -> ')
    instructions[pos] = val

for n in range(10):
    print(f"Running step {n}")
    print("--- %s seconds ---" % (time.time() - start_time))
    insertions = []

    for i in range(len(template) - 1):
        for ins in instructions:
            if template[i] + template[i + 1] == ins:
                insertions.append((instructions[ins], i + 1, True))

    idx = 0
    while any(b for val, i, b in insertions):
        val, i, b = insertions[idx]
        template.insert(i, val)
        insertions[idx] = (val, i, False)

        for j in range(idx, len(insertions)):
            val2, i2, b2 = insertions[j]
            insertions[j] = (val2, i2 + 1, b2)

        idx += 1


c = Counter(''.join(template))
max_occurences = max(c.values())
min_occurences = min(c.values())

part_one_res = max_occurences - min_occurences
print(part_one_res)

print("--- %s seconds ---" % (time.time() - start_time))