import copy
import math
import os
import time
from itertools import batched

import numpy as np

from aoc.util import pairwise

"71801458638945906735378792713148808529464534303257235953879467313711717150491468856122209261207385896183975671231950194924687678691171917729439486819895574"

"0000000.111111112....33333........444444...555555"


def parse_input(input_data: list[str]):
    input_data = list(input_data[0])
    l = []
    id = []
    c = 0
    for i, d in enumerate(input_data):
        if i % 2 == 0:
            l.extend([1] * int(d))
            id.extend([c] * int(d))
            c += 1
        else:
            l.extend([0] * int(d))
            id.extend([-1] * int(d))
    return l, id


def first_task(input_data: list[str]):
    s, id = parse_input(input_data)
    for temp in enumerate(reversed(list(enumerate(s)))):
        i = temp[0]
        j, c = temp[1]
        if c == 1:
            if id.index(-1) > j:
                break
            si = s.index(0)
            s[si] = 1
            s[j] = 0
            id[si] = id[j]
            id[j] = -1
    count = 0
    for i, c in enumerate(id):
        if c != -1:
            count += i * int(c)
    return count


def second_task(input_data: list[str]):
    input_data = list(input_data[0])
    disc = []
    for i in range(len(input_data)):
        x = int(input_data[i])
        if i % 2 == 0:
            disc.append((i // 2, x))
        else:
            disc.append((-1, x))
    # print("DISC: ", disc)

    i = len(disc) - 1
    while i > 0:
        id, space = disc[i]
        if id == -1:
            i -= 1
            continue
        ni = -1
        for j in range(i):
            nid, nspace = disc[j]
            if nid == -1 and nspace >= space:
                ni = j
                break
        if ni == -1:
            i -= 1
            continue
        _, sspace = disc[ni]
        disc = (
            disc[:ni]
            + [(id, space), (-1, sspace - space)]
            + disc[ni + 1 : i]
            + [(-1, space)]
            + disc[i + 1 :]
        )
    # print("DISC: ", disc)
    sum = 0
    block = 0
    for i in disc:
        id, space = i
        if id == -1:
            block += space
            continue
        for j in range(space):
            sum += block * id
            block += 1
    return sum


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
