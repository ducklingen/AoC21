from helpers import AoCHelper

input = AoCHelper.read_input_lines("day1/input1.txt")
numbers = list(map(int, input))


def simpleIncreases(inputNumbers):
    init = 0
    count = 0

    for i in inputNumbers[1:]:
        if i > init:
            count += 1

        init = i

    return count


def rollingSumIncreases(inputNumbers):
    rollingSum = inputNumbers[0] + inputNumbers[1] + inputNumbers[2]
    count = 0

    for i in range(len(inputNumbers)-3):
        newSum = inputNumbers[i + 1] + inputNumbers[i + 2] + inputNumbers[i + 3]

        if newSum > rollingSum:
            count += 1

        rollingSum = newSum

    return count


simpleIncreases = simpleIncreases(numbers)
assert simpleIncreases == 1162
print(f"Part 1: {simpleIncreases}")

rollingSumIncreases = rollingSumIncreases(numbers)
assert rollingSumIncreases == 1190
print(f"Part 2: {rollingSumIncreases}")

