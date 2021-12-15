from helpers import AoCHelper
from itertools import product
from sys import maxsize
from queue import PriorityQueue
import time

start_time = time.time()

input_lines = AoCHelper.read_input_lines("day15/input1.txt")

# grid = [list(map(int, l)) for l in input_lines]

grid = []

for i in range(len(input_lines) * 5):
    h_line = []
    for j in range(5):
        h_line += [int(n) + j + (i // len(input_lines)) if int(n) + j + (i // len(input_lines)) <= 9 else int(n) + j + (i // len(input_lines)) - 9 for n in input_lines[i % len(input_lines)]]

    grid.append(h_line)


unvisited_nodes = list(product(range(len(grid)), range(len(grid[0]))))
tentative_nodes = [(0, 0)]

distance = {node: 0 if node == (0,0) else maxsize for node in unvisited_nodes}

x = y = 0

while (len(grid) - 1, len(grid[0]) - 1) in unvisited_nodes:
    for n, m in [(0,1), (1, 0), (-1, 0), (0, -1)]:
        if 0 <= x + n < len(grid) and 0 <= y + m < len(grid[0]) and (x + n, y + m) in unvisited_nodes:
            if distance[(x, y)] + grid[x + n][y + m] < distance[(x + n, y + m)]:
                distance[(x + n, y + m)] = distance[(x, y)] + grid[x + n][y + m]
                tentative_nodes.append((x + n, y + m))

    unvisited_nodes.remove((x, y))
    tentative_nodes.remove((x, y))

    lowest_value = maxsize

    for i, j in tentative_nodes:
        if distance[(i, j)] < lowest_value:
            lowest_value = distance[(i, j)]
            x = i
            y = j

print(distance[(len(grid) - 1, len(grid[0]) - 1)])

print("--- %s seconds ---" % (time.time() - start_time))