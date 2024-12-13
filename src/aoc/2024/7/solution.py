import itertools
import math
import os
import time
from itertools import product
from operator import add, mul

import numpy as np


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


def process_ops(nums, ops):
    if len(nums) == 1:
        return nums[0]

    l, r, *rest = nums
    cur_op, *remaining_ops = ops

    return process_ops([cur_op(l, r), *rest], remaining_ops)


def process_line(line, include_concat=False):
    t, inp = line

    ops = [add, mul]
    if include_concat:
        ops.append(concat)

    for op_combo in product(ops, repeat=len(inp) - 1):
        if process_ops(inp, op_combo) == t:
            return t

    # if any(
    #     process_ops(inp, op_combo) == t
    #     for op_combo in product(ops, repeat=len(inp) - 1)
    # ):
    #     return t
    return 0


def first_task(input_data: list[str]):
    arr = []
    for line in input_data:
        equals, numbers = line.split(":")
        numbers = [int(x) for x in numbers.strip().split(" ")]
        arr.append([int(equals), numbers])
    c = 0
    for line in arr:
        c += process_line(line)
    return c


def second_task(input_data: list[str]):
    arr = []
    for line in input_data:
        equals, numbers = line.split(":")
        numbers = [int(x) for x in numbers.strip().split(" ")]
        arr.append([int(equals), numbers])
    c = 0
    for line in arr:
        c += process_line(line, include_concat=True)
    return c


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = list(map(lambda line: line.strip(), open(input_file, "r")))

    t_start = time.time()
    first_answer = first_task(input_data)
    t_end = time.time()
    first_time = round(t_end - t_start, 2)
    if first_answer is not None:
        # Create part1
        filename = os.path.join(os.path.dirname(__file__), "part1.txt")
        with open(filename, "w") as file:
            file.write(str(first_answer))

    print("#############################")
    print("The answer to the 1st task is")
    print(first_answer, f"in {first_time} seconds")

    t_start = time.time()
    second_answer = second_task(input_data)
    t_end = time.time()
    second_time = round(t_end - t_start, 3)
    if second_answer is not None:
        # Create part2
        filename = os.path.join(os.path.dirname(__file__), "part2.txt")
        with open(filename, "w") as file:
            file.write(str(second_answer))

    print()
    print("The answer to the 2nd task is")
    print(second_answer, f"in {second_time} seconds")
    print("#############################")


if __name__ == "__main__":
    run_day()
