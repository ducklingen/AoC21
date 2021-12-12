from helpers import AoCHelper

input_lines = AoCHelper.read_input_lines("day12/input1.txt")

edges = []
for i in input_lines:
    a, b = i.split('-')
    edges.append((a, b))
    edges.append((b, a))


def get_paths(path, edges, easy):
    if path[-1] == 'end':
        return [path]

    new_paths = []
    for a, b in edges:
        if a == path[-1] and b != 'start':
            lc_entries = [x for x in path if x.islower()]

            if b.islower() and b in lc_entries and (easy or len(lc_entries) > len(set(lc_entries))):
                continue

            new_paths += get_paths(path + [b], edges, easy)

    return new_paths


easy_paths = []
hard_paths = []

for a, b in edges:
    if a == 'start':
        easy_paths += get_paths(['start', b], edges, True)
        hard_paths += get_paths(['start', b], edges, False)

assert len(easy_paths) == 3421
print(len(easy_paths))

assert len(hard_paths) == 84870
print(len(hard_paths))