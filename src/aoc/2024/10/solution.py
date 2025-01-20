import math
import os
import time

import numpy as np

neighbours = {(-1, 0), (0, 1), (1, 0), (0, -1)}


def depth_first_search(arr, start_x, start_y, target, prev=-1):
    if (
        start_x < 0
        or start_x >= len(arr)
        or start_y < 0
        or start_y >= len(arr[start_x])
    ):
        return set()
    v = arr[start_x][start_y]
    if v != prev + 1:
        return set()
    if v == target:
        return {(start_x, start_y)}
    r = set()
    for a in neighbours:
        r = r.union(depth_first_search(arr, start_x + a[0], start_y + a[1], target, v))
    return r


def parse_input(input_data: list[str]):
    arr = [[int(x) for x in l.strip()] for l in input_data]
    return arr


def first_task(input_data: list[str]):
    arr = parse_input(input_data)
    s = 0
    # print("ARR: ", arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                r = depth_first_search(arr, i, j, 9)
                s += len(r)
                # print("R: ", r)
    return s


def depth_first_search2(arr, start_x, start_y, target, prev=-1):
    if (
        start_x < 0
        or start_x >= len(arr)
        or start_y < 0
        or start_y >= len(arr[start_x])
    ):
        return 0
    v = arr[start_x][start_y]
    if v != prev + 1:
        return 0
    if v == target:
        return 1
    r = 0
    for a in neighbours:
        r += depth_first_search2(arr, start_x + a[0], start_y + a[1], target, v)
    return r


def second_task(input_data: list[str]):
    arr = parse_input(input_data)
    s = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                r = depth_first_search2(arr, i, j, 9)
                s += r
    return s


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
