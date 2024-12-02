import math
import re
from dataclasses import dataclass
from functools import total_ordering
from itertools import cycle

import networkx as nx
import numpy as np

with open("input") as f:
    lines = f.read()

# instructions = list(lines[0].strip())
# data = [l.strip() for l in lines[2:]]

# g = {}
# for l in data:
#     node, dest = l.split(" = ")
#     node = node.strip()
#     dest = [dest[1:4], dest[6:9]]
#     g[node] = dest
# print(g)

# final_dest = "ZZZ"
# # curr_node = "AAA"
# start_nodes = []
# for key, value in g.items():
#     if key.endswith("A"):
#         start_nodes.append(key)
# # print("START NODES: ", start_nodes)
# circle_lens = []
# temp_nodes = []
# for i, n in enumerate(start_nodes):
#     c = 0
#     while True:
#         idx = c % len(instructions)
#         curr_inst = instructions[idx]
#         if curr_inst == "L":
#             curr_inst = 0
#         if curr_inst == "R":
#             curr_inst = 1
#             temp_nodes[i] = g[n][curr_inst]
#         if n == start_nodes:
#             break
#             # if curr_node == final_dest:
#             # break
#         c += 1
#     circle_lens.append[c + 1]
# print("C: ", c + 1)


def part2(puzzle_input):
    directions, connections = puzzle_input.split("\n\n")
    directions = [0 if d == "L" else 1 for d in directions]
    graph = {}
    regex = r"(\w{3}) = \((\w{3}), (\w{3})\)"
    for node, left, right in re.findall(regex, connections):
        graph[node] = [left, right]

    starting_nodes = [node for node in graph if node[2] == "A"]
    cycles = []
    for node in starting_nodes:
        for steps, d in enumerate(cycle(directions), start=1):
            node = graph[node][d]
            if node[2] == "Z":
                cycles.append(steps)
                break

    return math.lcm(*cycles)


print("Part 2:", part2(lines))
