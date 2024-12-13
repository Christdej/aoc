import math
import os
import time

import numpy as np

from aoc.util import (
    find_neighbours,
    find_neighbours_one_pos,
    get_lines_through_pos_diagonal,
    get_lines_through_pos_up_down_left_right,
)


def find_neightbours_with_character_in_dir(arr, i, j, character, direction):
    ns = find_neighbours_one_pos(arr, i, j)
    for ni, n in enumerate(ns["neighbors"]):
        if ns["neighbors"][ni] == character:
            if [
                i - ns["pos_neighbors"][ni][0],
                j - ns["pos_neighbors"][ni][1],
            ] == direction:
                return ns["pos_neighbors"][ni]
    return []


def first_task(input_data: list[str]):
    arr = []
    for line in input_data:
        arr.append(list(line))
    nxs = find_neighbours(arr)
    c = 0
    for nx in nxs:
        if nx["value"] == "X":
            for n in nx["pos_neighbors"]:
                posx = n[0]
                posy = n[1]
                if arr[posx][posy] == "M":
                    dir = [nx["pos"][0] - posx, nx["pos"][1] - posy]
                    na = find_neightbours_with_character_in_dir(
                        arr, posx, posy, "A", dir
                    )
                    lennas = len(na)
                    if lennas == 2:
                        nss = find_neightbours_with_character_in_dir(
                            arr, na[0], na[1], "S", dir
                        )
                        if len(nss) == 2:
                            c += 1
    return c


def check_opposite(arr, px, py, nx, ny, character):
    dir = [px - nx, py - ny]
    opposite_dir = [-dir[0], -dir[1]]
    opposite_pos = [px + opposite_dir[0], py + opposite_dir[1]]
    ox = opposite_pos[0]
    oy = opposite_pos[1]
    if arr[ox][oy] == character:
        return True


def second_task(input_data: list[str]):
    arr = []
    for line in input_data:
        arr.append(list(line))
    nas = find_neighbours(arr)
    c = 0
    for na in nas:
        if na["value"] == "A":
            nax = na["pos"][0]
            nay = na["pos"][1]
            # udlr = get_lines_through_pos_up_down_left_right(arr, nax, nay)
            # # print("UDLR: ", udlr)
            # if udlr:
            #     if "M" in udlr[0] and "S" in udlr[0]:
            #         if "M" in udlr[1] and "S" in udlr[1]:
            #             c += 1

            diag = get_lines_through_pos_diagonal(arr, nax, nay)
            if diag:
                if "M" in diag[0] and "S" in diag[0]:
                    if "M" in diag[1] and "S" in diag[1]:
                        c += 1
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
