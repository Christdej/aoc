import os

import numpy as np


def parse_data(data):
    sensors = set()
    beacons = set()
    for l in data:
        e = l.strip()
        s, b = e.split(": closest beacon is at x=")
        sx, sy = s.split(", y=")
        sx = int(sx.split("x=")[1])
        sy = int(sy)
        bx, by = b.split(", y=")
        bx = int(bx)
        by = int(by)
        d = distance([sx, sy], [bx, by])
        sensors.add((sx, sy, d))
        beacons.add((bx, by))
    return sensors, beacons


def distance(s, b):
    return np.abs(np.array(s) - np.array(b)).sum()


# def make_grid(data):
#     grid = set()
#     for l in data:
#         s = l[0]
#         b = l[1]
#         d = distance(s, b)
#         for x in range(s[0] - d, s[0] + d):
#             for y in range(s[1] - d, s[1] + d):
#                 if distance(s, [x, y]) <= d:
#                     grid.add((x, y))
#     return grid


def is_possible(x, y):
    for sx, sy, d in sensors:
        if distance([x, y], [sx, sy]) <= d:
            if (x, y) not in beacons:
                return False
    return True


def no_beacon(y):
    c = 0
    for x in range(
        min(x - d for x, _, d in sensors),
        max(x + d for x, _, d in sensors),
    ):
        if not is_possible(x, y):
            c += 1
    return c


def find_neigh(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def part2():
    # m = 20
    m = 4000000
    for sx, sy, d in sensors:
        pp = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
        for sdx in range(d + 2):
            sdy = (d + 1) - sdx
            for ppx, ppy in pp:
                tempx = sx + (sdx * ppx)
                tempy = sy + (sdy * ppy)
                if not (0 <= tempx <= m and 0 <= tempy <= m):
                    continue
                if is_possible(tempx, tempy):
                    return tempx * 4000000 + tempy


dirname = os.path.dirname(__file__)
with open(dirname + "/" + "input") as f:
    lines = f.readlines()
sensors, beacons = parse_data(lines)
# print("SENSORS: ", sensors)
# print("BEACONS: ", beacons)
# Y = 2000000
# Y = 10
# print("PART 1: ", no_beacon(Y))

print("PART 2: ", part2())
