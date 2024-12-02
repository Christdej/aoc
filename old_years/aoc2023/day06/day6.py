import re

import numpy as np

# with open("input") as f:
#     lines = f.readlines()

# time = [int(number) for number in re.findall(r"\d+", lines[0])]
# dist = [int(number) for number in re.findall(r"\d+", lines[1])]

# v0 = 0
# a = 1
# total_c = []
# for tr, d in zip(time, dist):
#     temp_c = 0
#     for t in range(tr + 1):
#         if d < t * (tr - t):
#             temp_c += 1
#     total_c.append(temp_c)

# print("TOTAL: ", total_c)
# print("PROD TOT: ", np.prod(total_c))

with open("input") as f:
    lines = f.readlines()

time = [number for number in re.findall(r"\d+", lines[0])]
time = int("".join(time))
dist = [number for number in re.findall(r"\d+", lines[1])]
dist = int("".join(dist))

v0 = 0
a = 1
# total_c = []
# for tr, d in zip(time, dist):
temp_c = 0
for t in range(time + 1):
    if dist < t * (time - t):
        temp_c += 1
# total_c.append(temp_c)

print("TOTAL: ", temp_c)
# print("PROD TOT: ", np.prod(total_c))
