from helpers import AoCHelper
from itertools import product
from sys import maxsize
from queue import PriorityQueue
import binascii
import sys
import time

start_time = time.time()

input_lines = AoCHelper.read_input_lines("day16/input1.txt")
input = input_lines[0]

ins = bin(int(input, 16))[2:].zfill(len(input) * 4)

def extract_number(input, index, size):
    return int(input[index:index + size], 2), index + size


def unpack_easy(input, index, number_of_packages, end_of_package):
    version_sum = 0
    unpacked = 0

    while unpacked < number_of_packages and index < end_of_package:
        version, index = extract_number(input, index, 3)
        version_sum += version
        type, index = extract_number(input, index, 3)

        if type == 4:
            lit_val_string = ''
            last_pack = False

            while not last_pack:
                if input[index] == '0':
                    last_pack = True

                lit_val_string += input[index + 1: index + 5]
                index += 5

        else:
            lenght_type, index = extract_number(input, index, 1)

            if lenght_type == 0:
                lenght, index = extract_number(input, index, 15)
                version_addition, index = unpack_easy(input, index, maxsize, index + lenght)
                version_sum += version_addition
            else:
                number_of_sub_packages, index = extract_number(input, index, 11)
                version_addition, index = unpack_easy(input, index, number_of_sub_packages, maxsize)
                version_sum += version_addition

        unpacked += 1

    return version_sum, index


part_one_res = unpack_easy(ins, 0, 1, len(ins))[0]
assert part_one_res == 949
print(f"Part 1: {part_one_res}")

print("--- %s seconds ---" % (time.time() - start_time))