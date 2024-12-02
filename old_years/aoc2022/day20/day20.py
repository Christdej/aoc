import os
from copy import copy

import numpy as np


def parse_data(data):
    temp = []
    for i, l in enumerate(data):
        e = l.strip()
        temp.append((int(e), i))
    return temp


def part1(l):
    vals = [a[0] for a in l]
    idxs = [a[1] for a in l]
    for i in range(len(vals)):
        j = idxs.index(i)
        idxs.pop(j)
        tar = (j + vals[i]) % len(idxs)
        idxs.insert(tar, i)

    i = idxs.index(vals.index(0))
    return sum(vals[idxs[(i + x) % len(idxs)]] for x in [1000, 2000, 3000])


def part2(l):
    vals = [a[0] * 811589153 for a in l]
    idxs = [a[1] for a in l]
    for _ in range(10):
        for i in range(len(vals)):
            j = idxs.index(i)
            idxs.pop(j)
            tar = (j + vals[i]) % len(idxs)
            idxs.insert(tar, i)
    i = idxs.index(vals.index(0))
    return sum(vals[idxs[(i + x) % len(idxs)]] for x in [1000, 2000, 3000])


dirname = os.path.dirname(__file__)
with open(dirname + "/" + "input") as f:
    lines = f.readlines()
data = parse_data(lines)
# print("DATA: ", data)

print("PART 1: ", part1(data))
print("PART 2: ", part2(data))


# x = [int(x) * 811589153 for x in open("input_example")]
# j = list(range(len(x)))

# for _ in range(10):
#     for i in range(len(x)):
#         c = j.index(i)
#         j.pop(c)
#         j.insert((c + x[i]) % len(j), i)

# z = j.index(x.index(0))
# print(sum(x[j[(z + i) % len(j)]] for i in [1000, 2000, 3000]))
