import os
from copy import copy

import numpy as np

N = 10000
GRID = np.zeros((N, N), dtype=int)

SNAKE = np.zeros((10, 2), dtype=int)


def parse_data(data):
    temp = []
    for l in data:
        d, v = l.split(" ")
        if d == "L":
            temp.append([-int(v), 0])
        if d == "R":
            temp.append([int(v), 0])
        if d == "U":
            temp.append([0, int(v)])
        if d == "D":
            temp.append([0, -int(v)])
    return temp


def distance_from_head(head, tail):
    dist = np.abs(np.array(head) - np.array(tail)).sum()
    return dist


def is_diagonal(head, tail):
    if head[0] != tail[0] and head[1] != tail[1]:
        return True
    return False


def move(x, y):
    global SNAKE
    l = 0
    # ll = 1
    k = x
    if x == 0 and y != 0:
        l = 1
        # ll = 0
        k = y
    for i in range(abs(k)):
        prev_head = copy(SNAKE[0])
        if k > 0:
            SNAKE[0, l] += 1
        if k < 0:
            SNAKE[0, l] -= 1
        for sx in range(1, len(SNAKE)):
            if sx == len(SNAKE) - 1:
                update_grid(SNAKE[sx])
            dist = distance_from_head(SNAKE[sx - 1], SNAKE[sx])
            if dist > 2 and is_diagonal(SNAKE[sx - 1], SNAKE[sx]):
                temp_head = copy(SNAKE[sx])
                SNAKE[sx] = copy(prev_head)
                prev_head = temp_head
            elif dist == 2 and not is_diagonal(SNAKE[sx - 1], SNAKE[sx]):
                temp_head = copy(SNAKE[sx])
                SNAKE[sx] = prev_head
                prev_head = temp_head
        print(GRID)
        print(SNAKE)
        # print("LOOP")

    return


def update_grid(pos):
    global GRID
    # print("POS: ", pos)
    GRID[pos[0], pos[1]] += 1


dirname = os.path.dirname(__file__)
with open(dirname + "/" + "input_example") as f:
    lines = f.readlines()
data = []
for l in lines:
    e = l.strip()
    data.append(e)

data = parse_data(data)

for m in data:
    move(m[0], m[1])
# update_grid([0, 0])
counts = (GRID > 0).sum()
# unique, counts = np.unique(GRID, return_counts=True)
# cs = dict(zip(unique, counts))
# print(GRID)
print("COUNT: ", counts)

# DOES NOT WORK ATM, tried to change, but failed
