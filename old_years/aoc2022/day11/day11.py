import math
import operator
import os
from copy import copy, deepcopy
from dataclasses import dataclass

import numpy as np


# @dataclass
class Monkey:
    def __init__(self, n) -> None:
        self.n = n
        self.wl = []
        self.operation = lambda n: n + 1
        self.test = lambda d: d % 1 == 0
        self.res = [0, 0]
        self.mod = 0


def parse_data(data):
    monkeys = []
    _, n = data[0].split(" ")
    n = n[:-1]
    monkey = None
    # monkeys.append(monkey)
    ops = {"+": operator.add, "*": operator.mul}
    for l in data:
        if l.startswith("Monkey"):
            m, n = l.split(" ")
            n = n[:-1]
            monkey = Monkey(int(n))
            monkeys.append(monkey)
        if l.startswith("Starting items"):
            _, items = l.split(":")
            for i in items.split(","):
                i = i.strip()
                monkey.wl.append(int(i))
        if l.startswith("Operation"):
            _, operation_a = l.split("=")
            operation_a = operation_a.strip()
            for o in ops:
                if o in operation_a:
                    _, op = operation_a.split(o)
                    op = op.strip()
                    temp = copy(ops[o])
                    if op == "old":
                        monkey.operation = lambda a, temp=temp: temp(a, a)
                    else:
                        asd = copy(int(op))
                        monkey.operation = lambda a, asd=asd, temp=temp: temp(a, asd)
        if l.startswith("Test"):
            _, test = l.split("by")
            test = test.strip()
            test = copy(int(test))
            monkey.mod = test
            monkey.test = lambda d, test=test: d % test == 0
        if l.startswith("If true"):
            sp = l.split(" ")
            monkey.res[0] = int(sp[-1].strip())
        if l.startswith("If false"):
            sp = l.split(" ")
            monkey.res[1] = int(sp[-1].strip())
    return monkeys


dirname = os.path.dirname(__file__)
with open(dirname + "/" + "input") as f:
    lines = f.readlines()
data = []
for l in lines:
    e = l.strip()
    data.append(e)
monkeys = parse_data(data)
# m0 = monkeys[0]
# m1 = monkeys[1]
# print(m0.operation(2))
# print(m0.test(23))
# print(m1.operation(2))
# print(m1.test(19))
# print(data)

inspections = np.zeros(len(monkeys), dtype=int)
prod = 1
for p in monkeys:
    prod *= p.mod
for i in range(10000):
    for j, m in enumerate(monkeys):
        for item in m.wl:
            worry_level = m.operation(item)
            # if worry_level % 2 == 0:
            #     worry_level = int(worry_level / 2)
            # worry_level = math.floor(worry_level / 3)
            worry_level = worry_level % prod
            new_monkey = m.res[1]
            if m.test(worry_level):
                new_monkey = m.res[0]
                # worry_level = worry_level / m.mod
            monkeys[new_monkey].wl.append(worry_level)
            inspections[j] += 1
        m.wl = []
print("INSPECTIONS: ", inspections)
inspections.sort()
print("MB: ", inspections[-1] * inspections[-2])
