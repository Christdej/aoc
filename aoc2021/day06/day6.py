import numpy as np


def parse_fish(data):
    fishes = np.zeros((9))
    for i in data:
        fishes[i] += 1
    fishes[0] = -1
    return fishes


def lanternfish(data, days=80):
    for i in range(days):
        temp = np.zeros((9))
        for j, e in enumerate(data):
            if e == -1:
                continue
            if j == 0:
                temp[8] += e
                temp[6] += e
            else:
                temp[j - 1] += data[j]
        # print(temp)
        data = temp

    return np.sum(data)


data = [3, 4, 3, 1, 2]
data = parse_fish(data)
print(data)
print(lanternfish(data))
assert lanternfish(data) == 5934
assert lanternfish(data, days=256) == 26984457539

with open("input") as f:
    lines = f.readlines()

data = [e.strip().split(",") for e in lines][0]
data = [int(e) for e in data]
data = parse_fish(data)
print(lanternfish(data, days=256))
