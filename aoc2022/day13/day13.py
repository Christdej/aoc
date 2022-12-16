import functools
import os


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def parse_data(data):
    temp = []
    for l in data:
        if l != "":
            temp.append(eval(l))
    # temp = list(chunks(temp, 2))
    return temp


def tolist(a):
    return a if type(a) == list else [a]


def right_order(one, two):
    if type(one) == type(two) == int:
        return one - two
    one = tolist(one)
    two = tolist(two)
    for x, y in zip(one, two):
        # r = right_order(x, y)
        if (r := right_order(x, y)) != 0:
            return r
    return len(one) - len(two)


dirname = os.path.dirname(__file__)
with open(dirname + "/" + "input") as f:
    lines = f.readlines()
data = []
for l in lines:
    e = l.strip()
    data.append(e)
data = parse_data(data)

indices = 0
for i, (one, two) in enumerate(zip(data[::2], data[1::2]), start=1):
    test = right_order(one, two)
    if test < 0:
        indices += i
print("PART 1 INDICES: ", indices)

data.append([[2]])
data.append([[6]])
s = sorted(data, key=functools.cmp_to_key(right_order))
print("S: ", s)

key = 1
for i, v in enumerate(s, start=1):
    if v in [[[2]], [[6]]]:
        print("IDX: ", i)
        key = key * (i)

print("PART 2 KEY: ", key)
