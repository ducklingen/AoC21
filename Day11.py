from itertools import combinations_with_replacement

from helpers.GlobalVariables import all_directions
from helpers import AoCHelper

input_lines = AoCHelper.read_input_lines("day11/input1.txt")
grid = [list(map(int, l)) for l in input_lines]

step = 0
flashes = 0

while True:
    step += 1

    for x, y in AoCHelper.get_all_coordinates_in_grid(10, 10):
        grid[x][y] = grid[x][y] + 1

    while len([(x, y) for (x, y) in AoCHelper.get_all_coordinates_in_grid(10, 10) if grid[x][y] > 9]) > 0:
        for x, y in AoCHelper.get_all_coordinates_in_grid(10, 10):
            if grid[x][y] > 9:
                for n, m in all_directions:
                    if 0 <= x + n < len(grid) and 0 <= y + m < len(grid[0]):
                        if 0 < grid[x+n][y+m] < 10:
                            grid[x+n][y+m] = grid[x+n][y+m] + 1

                grid[x][y] = 0

    flashes_in_step = len([(x, y) for (x, y) in AoCHelper.get_all_coordinates_in_grid(10, 10) if grid[x][y] == 0])

    if step <= 100:
        flashes += flashes_in_step

    if  flashes_in_step == 100:
        print(f"Finished at step {step}")
        break

assert flashes == 1700
print(f"Part 1: {flashes}")

assert step == 273
print(f"Part 2: {step}")
