import numpy as np


def is_tree_visisble(height, i, j):
    global DATA
    nr = len(DATA)
    nc = len(DATA[0])
    if i == 0 or i == nr - 1:
        return True
    if j == 0 or j == nc - 1:
        return True
    if all(k < height for k in DATA[i, :j]):
        return True
    if all(k < height for k in DATA[i, j + 1 :]):
        return True
    if all(k < height for k in DATA[:i, j]):
        return True
    if all(k < height for k in DATA[i + 1 :, j]):
        return True
    return False


def scenic_score(height, i, j):
    global DATA
    nr = len(DATA)
    nc = len(DATA[0])
    if i == 0 or i == nr - 1:
        return 0
    if j == 0 or j == nc - 1:
        return 0
    c = 1
    temp = DATA[i, :j]
    c = c * scenic(temp[::-1], height)

    temp = DATA[i, j + 1 :]
    c = c * scenic(temp, height)

    temp = DATA[:i, j]
    c = c * scenic(temp[::-1], height)

    temp = DATA[i + 1 :, j]
    c = c * scenic(temp, height)

    return c


def scenic(neigh, height):
    if len(neigh) == 1:
        return 1
    for ix, i in enumerate(neigh):
        if i >= height:
            return ix + 1
    return len(neigh)


with open("input") as f:
    lines = f.readlines()
DATA = []
for l in lines:
    e = l.strip()
    DATA.append([int(a) for a in list(e)])
DATA = np.array(DATA)
n_trees = 0
best = 0
best_i = 0
best_j = 0
for i, r in enumerate(DATA):
    for j, c in enumerate(r):
        if is_tree_visisble(c, i, j):
            n_trees += 1
        score = scenic_score(c, i, j)
        if score > best:
            best = score
            best_i = i
            best_j = j

print("N TREES: ", n_trees)
print("BEST SCORE: ", best)
print("BEST I: ", best_i)
print("BEST J: ", best_j)
