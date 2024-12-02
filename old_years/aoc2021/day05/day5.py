import numpy as np
from numpy.lib.twodim_base import diag
from numpy.typing import _16Bit


def points_are_diag(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    # if (x1 == y2 and y1 == x2) or (x1 == y1 and x2 == y2):
    #     return True
    if x2 > x1:
        start_x = x1
        end_x = x2
    else:
        start_x = x2
        end_x = x1
    if y2 > y1:
        start_y = y1
        end_y = y2
    else:
        start_y = y2
        end_y = y1
    for i in range(end_x - start_x):
        start_x += 1
        start_y += 1
    if start_x == end_x and start_y == end_y:
        return True
    return False


def diag_points(p1, p2):
    temps = []
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    # temps.append([x1, y1])
    n_points = abs(x1 - x2) + 1
    if x2 > x1:
        iter_x = +1
    else:
        iter_x = -1
    if y2 > y1:
        iter_y = +1
    else:
        iter_y = -1
    temp_x = x1
    temp_y = y1
    for j in range(n_points):
        temps.append([temp_x, temp_y])
        temp_x += iter_x
        temp_y += iter_y
    return temps


def fill_grid(points):
    x1s = points[:, 0, 0]
    y1s = points[:, 0, 1]
    x2s = points[:, 1, 0]
    y2s = points[:, 1, 1]
    max_x = np.max([np.max(x1s), np.max(x2s)])
    max_y = np.max([np.max(y1s), np.max(y2s)])
    grid = np.zeros((max_x + 1, max_y + 1))
    print(np.shape(grid))
    for i, p in enumerate(points):
        p1 = p[0]
        p2 = p[1]
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        # print("P1: ", p1)
        # print("P2: ", p2)
        if points_are_diag(p1, p2):
            temps = diag_points(p1, p2)
            for temp_p in temps:
                grid[temp_p[0], temp_p[1]] += 1

        elif x1 == x2:
            if y1 > y2:
                grid[x1, y2 : y1 + 1] += 1
            else:
                grid[x1, y1 : y2 + 1] += 1
        elif y1 == y2:
            if x1 > x2:
                grid[x2 : x1 + 1, y1] += 1
            else:
                grid[x1 : x2 + 1, y1] += 1
        # print(grid.T)
    return grid


def parse_data(data):
    n = len(data)
    points = np.zeros((n, 2, 2), dtype=int)
    for i, l in enumerate(data):
        s = l.split(" -> ")
        points[i, 0] = [int(e) for e in s[0].split(",")]
        points[i, 1] = [int(e) for e in s[1].split(",")]
    return points


def hydrothermal_venture(data):
    grid = fill_grid(data)
    c = np.count_nonzero(
        grid > 1,
    )
    return c


data = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]

data = parse_data(data)
# print(diag_points([8, 0], [0, 8]))
# print(hydrothermal_venture(data))
assert hydrothermal_venture(data) == 12


with open("input") as f:
    lines = f.readlines()

data = [e for e in lines]
points = parse_data(data)
# print(points)


print(hydrothermal_venture(points))
