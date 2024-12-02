import math
import re
from dataclasses import dataclass
from functools import total_ordering
from itertools import cycle

import networkx as nx
import numpy as np

# def calc_down(line):
#     m = []
#     m.append(line)
#     prev_line = line
#     while True:
#         temp = []
#         for i, v in enumerate(prev_line[:-1]):
#             temp.append(prev_line[i + 1] - v)
#         m.append(temp)
#         prev_line = temp
#         if all([v == 0 for v in temp]):
#             break
#     return m


# def calc_history(line):
#     s = 0
#     prev_line = line
#     s += line[-1]
#     while True:
#         temp = []
#         for i, v in enumerate(prev_line[:-1]):
#             temp.append(prev_line[i + 1] - v)
#         prev_line = temp
#         s += prev_line[-1]
#         if all([v == 0 for v in temp]):
#             break
#     return s


def calc_history(line):
    s = 0
    prev_line = line
    s += line[0]
    c = 0
    while True:
        temp = []
        for i, v in enumerate(prev_line[:-1]):
            temp.append(prev_line[i + 1] - v)
        prev_line = temp
        # print("C: ", c)
        # print("PREV LINE: ", prev_line)
        if c % 2 == 1:
            s += prev_line[0]
        else:
            s -= prev_line[0]

        c += 1
        if all([v == 0 for v in temp]):
            break
    return s


with open("input") as f:
    lines = f.readlines()

data = []
for l in lines:
    data.append([int(number) for number in re.findall(r"[-+]?\d+", l)])
print(data)

s = 0
for l in data:
    s += calc_history(l)
    # m = reversed(m)
    # next_in_history = calc_up(m)
    # s += next_in_history
    # print("M: ", m)
print("S: ", s)
