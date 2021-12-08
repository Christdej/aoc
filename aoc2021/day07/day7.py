import numpy as np

# def parse_crabs(data):
#     crabs = np.zeros((9))
#     for i in data:
#         crabs[i] += 1
#     crabs[0] = -1
#     return crabs


def whales(data):
    min_val = np.min(data)
    max_val = np.max(data)
    min_fuel = max_val * len(data) * 1000000
    for i in range(min_val, max_val):
        temp_min = 0
        for e in data:
            diff = np.abs(i - e)
            temp_min += diff * (diff + 1) / 2
        if temp_min < min_fuel:
            min_fuel = temp_min
    return min_fuel


data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
# data = parse_crabs(data)
print(data)
print(whales(data))
assert whales(data) == 168

with open("input") as f:
    lines = f.readlines()

data = [e.strip().split(",") for e in lines][0]
data = [int(e) for e in data]
# data = parse_crabs(data)
print(whales(data))
