import math
import os
import time
from functools import cache

import numpy as np


def parse_input(input_data: list[str]):
    return [x for x in input_data[0].split(" ")]


def first_task(input_data: list[str]):
    stones = parse_input(input_data)
    # print("STONES: ", stones)
    for i in range(25):
        for si, s in enumerate(stones):
            if s == "0":
                stones[si] = "1"
                continue
            if len(s) % 2 == 0:
                a = s[: len(s) // 2]
                b = s[len(s) // 2 :]
                stones[si] = [str(int(a)), str(int(b))]
                continue
            else:
                stones[si] = str(int(s) * 2024)
        flat_list = []
        for l in stones:
            if isinstance(l, list):
                flat_list.extend([y for y in l])
            else:
                flat_list.append(l)
        stones = flat_list  # maybe deep cpoy
    return len(stones)


@cache
def blink(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        return blink(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        n = len(str(stone))
        left = int(str(stone)[: n // 2])
        right = int(str(stone)[n // 2 :])
        return blink(left, blinks - 1) + blink(right, blinks - 1)
    else:
        return blink(stone * 2024, blinks - 1)


def second_task(input_data: list[str]):
    stones = [int(x) for x in input_data[0].split(" ")]
    print("STONES: ", stones)
    c = 0
    for s in stones:
        c += blink(s, 75)
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
