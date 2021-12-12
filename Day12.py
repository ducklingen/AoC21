from helpers import AoCHelper

input_lines = AoCHelper.read_input_lines("day12/input1.txt")

edges = []
easy_paths = []
hard_paths = []

for i in input_lines:
    a, b = i.split('-')
    edges.append((a, b))
    edges.append((b, a))


def get_paths(path, edges, easy):
    new_paths = []

    if path[-1] == 'end':
        return [path]

    for e in edges:
        if e[0] == path[-1]:
            if e[1] == 'start':
                continue

            lower_case_entries = [x for x in path if x.islower()]

            if e[1].islower() and e[1] in lower_case_entries:
                if easy or len(lower_case_entries) > len(set(lower_case_entries)):
                    continue

            new_paths += get_paths(path + [e[1]], edges, easy)

    return new_paths


for e in edges:
    if e[0] == 'start':
        easy_paths += get_paths([e[0], e[1]], edges, True)
        hard_paths += get_paths([e[0], e[1]], edges, False)

assert len(easy_paths) == 3421
print(len(easy_paths))

assert len(hard_paths) == 84870
print(len(hard_paths))