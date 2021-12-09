from helpers import AoCHelper, GlobalVariables

input_lines = AoCHelper.read_input_lines("day9/input1.txt")
grid = [list(map(int, list(line))) for line in input_lines]


def get_low_points(grid):
    low_points = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbours = AoCHelper.get_neighbours(i, j, grid, GlobalVariables.cardinal_directions)

            if all(grid[i][j] < int(n) for n in neighbours if n != '.'):
                low_points.append((i,j))

    return low_points


def get_basin(i, j, grid, precursors):
    basin = [(i,j)]
    precursors.append((i,j))

    for x, y in GlobalVariables.cardinal_directions:
        if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]):
            if (grid[i + x][j + y]) < 9 and not((i+x, j+y) in precursors):
                basin += get_basin(i+x, j+y, grid, precursors)

    return basin


low_points = get_low_points(grid)
basins = []

for lp in low_points:
    basins.append(get_basin(lp[0], lp[1], grid, []))

basins.sort(reverse=True, key=len)

low_points_sum = sum(grid[p[0]][p[1]] + 1 for p in low_points)
assert low_points_sum == 524
print(f"Part 1: {low_points_sum}")

basin_product = AoCHelper.prod(map(len, basins[:3]))
assert basin_product == 1235430
print(f"Part 2: {basin_product}")
