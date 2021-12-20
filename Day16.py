from helpers import AoCHelper
from itertools import product
from sys import maxsize
from queue import PriorityQueue
import binascii
import time

start_time = time.time()

input_lines = AoCHelper.read_input_lines("day16/input1.txt")
input = input_lines[0]

ins = bin(int(input, 16))[2:]

index = 0

version = int(ins[index:index + 3], 2)
index += 3
type = int(ins[index:index + 3], 2)
index += 3

print(f"Version: {version}")
print(f"Type: {type}")

print(ins[index:])

print("--- %s seconds ---" % (time.time() - start_time))