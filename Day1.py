from helpers import AoCHelper

input = AoCHelper.read_input_lines("day1/input1.txt")
numbers = list(map(int, input))


def simpleIncreases(inputNumbers):
    return sum([inputNumbers[i] < inputNumbers[i+1] for i in range(len(inputNumbers)-1)])


def rollingSumIncreases(inputNumbers):
    return sum([inputNumbers[i] < inputNumbers[i+3] for i in range(len(inputNumbers)-3)])


simpleIncreases = simpleIncreases(numbers)
assert simpleIncreases == 1162
print(f"Part 1: {simpleIncreases}")

rollingSumIncreases = rollingSumIncreases(numbers)
assert rollingSumIncreases == 1190
print(f"Part 2: {rollingSumIncreases}")

