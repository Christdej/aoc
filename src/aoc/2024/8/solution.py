import itertools
import math
import os
import time

import numpy as np


def parse_input(input_data: list[str]):
    ant = {}
    arr = [[0 for i in range(len(input_data[0]))] for j in range(len(input_data))]
    for x, line in enumerate(input_data):
        for y, c in enumerate(line):
            if c != ".":
                if c not in ant:
                    ant[c] = [[x, y]]
                else:
                    ant[c].append([x, y])
    return ant, arr


def calc_antinodes(pair):
    pair1 = pair[0]
    pair2 = pair[1]
    diff1 = [pair1[0] - pair2[0], pair1[1] - pair2[1]]
    diff2 = [pair2[0] - pair1[0], pair2[1] - pair1[1]]
    pos1 = [pair1[0] + diff1[0], pair1[1] + diff1[1]]
    pos2 = [pair2[0] + diff2[0], pair2[1] + diff2[1]]
    return pos1, pos2


def check_inside(pos, arr):
    return 0 <= pos[0] < len(arr) and 0 <= pos[1] < len(arr[0])


def first_task(input_data: list[str]):
    ant, arr = parse_input(input_data)
    for key, value in ant.items():
        pairs = list(itertools.combinations(value, 2))
        for pair in pairs:
            pos1, pos2 = calc_antinodes(pair)
            if check_inside(pos1, arr):
                arr[pos1[0]][pos1[1]] = 1
            if check_inside(pos2, arr):
                arr[pos2[0]][pos2[1]] = 1
    c = sum(arr.count(1) for arr in arr)
    return c


def second_task(input_data: list[str]):
    return None


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
