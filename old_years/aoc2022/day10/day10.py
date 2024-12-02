import os
from copy import copy

import numpy as np

# [TIME, VALUE]

CYCLE = 0
VALUE = 1
CYCLE0 = 0
CYCLE_INC = 40

CRT = np.zeros(6 * 40)
CRT_CYCLE = 0


def parse_data(data):
    temp = []
    for l in data:
        if l == "noop":
            temp.append(0)
        else:
            _, v = l.split(" ")
            temp.append(0)
            temp.append(int(v))
    return temp


def exec_command(l):
    global VALUE
    VALUE += l


def draw():
    global CRT_CYCLE
    temp = CRT_CYCLE % 40
    if temp - 1 == VALUE or temp == VALUE or temp + 1 == VALUE:
        CRT[CYCLE] = 1


dirname = os.path.dirname(__file__)
with open(dirname + "/" + "input") as f:
    lines = f.readlines()
data = []
for l in lines:
    e = l.strip()
    data.append(e)
data = parse_data(data)

print(data)
signal_sum = 0
print("LEN DATA: ", len(data))
for l in data:
    temp = copy(VALUE)
    draw()
    exec_command(l)
    CYCLE += 1
    CRT_CYCLE += 1
    # if CYCLE >= CYCLE0 and CYCLE0 <= 220:
    #     print("CYCLE: ", CYCLE)
    #     print("VALUE: ", VALUE)
    #     v = CYCLE0 * temp
    #     signal_sum += v
    #     print("PRODUCT: ", v)
    #     CYCLE0 += CYCLE_INC
CRT = ["#" if i == 1 else "." for i in CRT]
CRT = np.reshape(CRT, (6, 40))
CRT = ["".join(a) for a in CRT]
for i in CRT:
    print(i)
# print("CRT: \n", CRT)
