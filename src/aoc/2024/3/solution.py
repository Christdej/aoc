import math
import os
import re
import time

import numpy as np


def parse_input(input_data: str):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input_data)
    return matches


def first_task(input_data: list[str]):
    c = 0
    for line in input_data:
        matches = parse_input(line)
        for match in matches:
            c += int(match[0]) * int(match[1])
    return c


def clean(string):
    # pattern = r"don't\(\)(?:(?!don't\(\)).)*?do\(\)"
    pass


def second_task(input_data: list[str]):
    c = 0
    long_string = ""
    for line in input_data:
        long_string += line
    ss = long_string.split("don't()")
    muls = parse_input(ss[0])
    for mul in muls:
        c += int(mul[0]) * int(mul[1])
    for s in ss[1:-1]:
        dos = s.split("do()")
        for do in dos[1:]:
            muls = parse_input(do)
            for mul in muls:
                c += int(mul[0]) * int(mul[1])

    # muls = parse_input(string)
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
