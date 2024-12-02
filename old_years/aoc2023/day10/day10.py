# import math
# import re
# from dataclasses import dataclass
# from functools import total_ordering
# from itertools import cycle

# import networkx as nx
# import numpy as np

# with open("input_ex") as f:
#     lines = f.readlines()

# data = []
# for l in lines:
#     data.append(l.strip())
# print(data)

# arr = np.array(data)

# print(arr)

# s, t = open("input_ex").read().splitlines(), dict(
#     zip("|-LJ7FS.", (16644, 1344, 1284, 324, 16704, 17664, 17988, 0))
# )
# print("16644: ", bin(16644))
# print("1344 : ", bin(1344))
# print("1284 : ", bin(1284))
# print("324  : ", bin(324))
# print("16704: ", bin(16704))
# print("17664: ", bin(17664))
# print("17988: ", bin(17988))
# print("s: ", s)
# print("t: ", t)
# g, n = [
#     (t[c] >> i + j) & 3 for r in s for i in (0, 6, 12) for c in r for j in (0, 2, 4)
# ], 3 * len(s)

# print("g: ", g)
# print("n: ", n)

# g = []
# n = 3 * len(s)

# for r in s:
#     for i in (0, 6, 12):
#         for c in r:
#             for j in (0, 2, 4):
#                 print("i: ", i, bin(i))
#                 print("j: ", j, bin(j))
#                 print("c: ", c)
#                 print("t[c]: ", t[c], bin(t[c]))
#                 g.append((t[c] >> i + j) & 3)
# print("g_new: ", g)
# print("n_new: ", n)

# import operator as o


# def f(s, v=0):
#     return len(
#         [
#             o.setitem(g, p, s.append(p) or 2)
#             for q in s
#             for p in (q - n, q + n, q + 1, q - 1)
#             if v <= g[p] < 2
#         ]
#     )


# print(
#     (f([g.index(2)], 1) - 1) // 6,
#     f([0])
#     and n * n // 9
#     - sum(g[n * i + 1 : n * i + n + 1 : 3].count(2) for i in range(1, n, 3)),
# )


def findNext(cur, x, y):
    if cur == "7":
        return [[x - 1, y], [x, y + 1]]
    elif cur == "J":
        return [[x - 1, y], [x, y - 1]]
    elif cur == "F":
        return [[x + 1, y], [x, y + 1]]
    elif cur == "L":
        return [[x + 1, y], [x, y - 1]]
    elif cur == "-":
        return [[x - 1, y], [x + 1, y]]
    elif cur == "|":
        return [[x, y + 1], [x, y - 1]]


with open("input") as f:
    pipes = f.read().splitlines()

for i in range(len(pipes)):
    if "S" in pipes[i]:
        start = [pipes[i].index("S"), i]

stepmap = [["."] * len(pipe) for pipe in pipes]
steps, curQueue, nextQueue = 1, [], []

shapeFlag = 0
shapeMap = {11: "-", 101: "J", 1001: "7", 110: "L", 1010: "F", 1100: "|"}

if pipes[start[1]][start[0] - 1] in ["F", "L", "-"]:
    shapeFlag += 1
    curQueue.append((start[0] - 1, start[1]))
if pipes[start[1]][start[0] + 1] in ["J", "7", "-"]:
    shapeFlag += 10
    curQueue.append((start[0] + 1, start[1]))
if pipes[start[1] - 1][start[0]] in ["F", "7", "|"]:
    shapeFlag += 100
    curQueue.append((start[0], start[1] - 1))
if pipes[start[1] + 1][start[0]] in ["J", "L", "|"]:
    shapeFlag += 1000
    curQueue.append((start[0], start[1] + 1))

stepmap[start[1]][start[0]] = shapeMap[shapeFlag]

while curQueue:
    x, y = curQueue.pop()
    stepmap[y][x] = pipes[y][x]
    nextSteps = findNext(pipes[y][x], x, y)
    for step in nextSteps:
        if stepmap[step[1]][step[0]] == ".":
            nextQueue.append(step)

    if not curQueue:
        curQueue = nextQueue
        nextQueue = []
        steps += 1

newMap, newlines = [], []
for j, line in enumerate(stepmap):
    i = 0

    newline = []
    while i < len(line):
        if line[i] in ["L", "F", "-"]:
            line.insert(i + 1, "-")
        else:
            line.insert(i + 1, ".")
        if line[i] in ["F", "|", "7"]:
            newline += ["|", "."]
        else:
            newline += [".", "."]
        i += 2
    newlines.append(newline)

bigmap = [None] * (len(stepmap) * 2)
bigmap[::2] = stepmap
bigmap[1::2] = newlines
bigmap.insert(0, ["."] * len(bigmap[0]))

curQueue = [[0, 0]]
while curQueue:
    x, y = curQueue.pop()
    bigmap[y][x] = "O"
    try:
        if bigmap[y][x - 1] == ".":
            curQueue.append([x - 1, y])
    except:
        pass
    try:
        if bigmap[y][x + 1] == ".":
            curQueue.append([x + 1, y])
    except:
        pass
    try:
        if bigmap[y + 1][x] == ".":
            curQueue.append([x, y + 1])
    except:
        pass
    try:
        if bigmap[y - 1][x] == ".":
            curQueue.append([x, y - 1])
    except:
        pass

# for line in stepmap:
#    print(" ".join([str(x) for x in line[::2]]))

print(steps - 1)
print(sum(line[::2].count(".") for line in stepmap))
