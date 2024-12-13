import copy
import math
import os
import time
from pprint import pprint

import numpy as np


def parse_input(input_data: list[str]):
    arr = []
    pos = []
    dir = []
    for x, l in enumerate(input_data):
        t = []
        for y, c in enumerate(l):
            if c == "<":
                pos = [x, y]
                dir = [0, -1]
                t.append(0)
                continue
            elif c == ">":
                pos = [x, y]
                dir = [0, 1]
                t.append(0)
                continue
            elif c == "^":
                pos = [x, y]
                dir = [-1, 0]
                t.append(0)
                continue
            elif c == "v":
                pos = [x, y]
                dir = [1, 0]
                t.append(0)
                continue
            elif c == "#":
                t.append(1)
                continue

            t.append(0)
        arr.append(t)
    return arr, pos, dir


def next_dir(dir):
    if dir == [-1, 0]:
        return [0, 1]
    if dir == [0, 1]:
        return [1, 0]
    if dir == [1, 0]:
        return [0, -1]
    if dir == [0, -1]:
        return [-1, 0]
    return None


def move_one(arr, pos, dir):
    x, y = pos
    dx, dy = dir
    new_pos = [x + dx, y + dy]
    if (
        new_pos[0] < 0
        or new_pos[0] >= len(arr)
        or new_pos[1] < 0
        or new_pos[1] >= len(arr[0])
    ):
        return [], dir

    if arr[new_pos[0]][new_pos[1]] == 1:
        return pos, next_dir(dir)
    return new_pos, dir


def mark_arr(arr, pos):
    x, y = pos
    arr[x][y] = 1
    return arr


def check_loop(p_arr, pos, dir):
    temp = (pos[0], pos[1], dir[0], dir[1])
    if temp in p_arr:
        return True
    return False


def first_task(input_data: list[str]):
    arr, pos, dir = parse_input(input_data)
    p_arr = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]
    while True:
        p_arr = mark_arr(p_arr, pos)
        pos, dir = move_one(arr, pos, dir)
        if not pos:
            break

    c = sum(x.count(1) for x in p_arr)
    return c


def second_task(input_data: list[str]):
    s_arr, s_pos, s_dir = parse_input(input_data)
    arr = copy.deepcopy(s_arr)
    pos = copy.deepcopy(s_pos)
    dir = copy.deepcopy(s_dir)
    path = set()
    while True:
        path.add((pos[0], pos[1]))
        pos, dir = move_one(arr, pos, dir)
        if not pos:
            break
    c = 0
    for p in path:
        arr = copy.deepcopy(s_arr)
        pos = copy.deepcopy(s_pos)
        dir = copy.deepcopy(s_dir)
        temp_arr = copy.deepcopy(arr)
        temp_arr[p[0]][p[1]] = 1

        p_arr = set()
        while True:
            p_arr.add((pos[0], pos[1], dir[0], dir[1]))
            pos, dir = move_one(temp_arr, pos, dir)
            if not pos:
                break
            if (pos[0], pos[1], dir[0], dir[1]) in p_arr:
                c += 1
                break
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
