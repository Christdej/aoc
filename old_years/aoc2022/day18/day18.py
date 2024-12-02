import os

import numpy as np


def parse_data(data):
    s = set()
    for l in data:
        e = l.strip().split(",")
        s.add(tuple((int(a) for a in e)))
    return s


def find_neighbours(arr):
    neighbors = []
    n = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
    for pos in arr:
        new_neighbors = []
        for p in n:
            new_neighbors.append(tuple((sum(x) for x in zip(p, pos))))
        neighbors.append({"pos": pos, "neigh": new_neighbors})
    return neighbors


def fn(pos):
    n = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
    neigh = []
    for p in n:
        neigh.append(tuple((sum(x) for x in zip(p, pos))))
    return neigh


def part1(data):
    neigh = find_neighbours(data)
    c = 0
    for n in neigh:
        for i in n["neigh"]:
            print("I: ", i)
            if not i in data:
                c += 1
    return c


def part2(data):
    minx = min(x for x, _, _ in data)
    maxx = max(x for x, _, _ in data)
    miny = min(y for _, y, _ in data)
    maxy = max(y for _, y, _ in data)
    minz = min(z for _, _, z in data)
    maxz = max(z for _, _, z in data)
    water = set()
    test = [(minx - 1, miny - 1, minz - 1)]
    while test:
        x, y, z = test.pop()
        water.add((x, y, z))
        neigh = fn((x, y, z))
        for i, j, k in neigh:
            if (
                minx - 1 <= i <= maxx + 1
                and miny - 1 <= j <= maxy + 1
                and minz - 1 <= k <= maxz + 1
            ):
                if (i, j, k) not in data and (i, j, k) not in water:
                    test.append((i, j, k))
    return sum((i, j, k) in water for x, y, z in data for i, j, k in fn((x, y, z)))


dirname = os.path.dirname(__file__)
with open(dirname + "/" + "input") as f:
    lines = f.readlines()
data = parse_data(lines)
# print("DATA: ", data)

print("PART 1: ", part1(data))

print("PART 2: ", part2(data))
