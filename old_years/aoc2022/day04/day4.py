def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def make_set(start, stop):
    return set(range(start, stop + 1))


def setissubset(one, two):
    if one.issubset(two):
        return True
    if two.issubset(one):
        return True
    return False


def contains_same_value(one, two):
    for i in one:
        for j in two:
            if j == i:
                return True


with open("input") as f:
    lines = f.readlines()
data = []
for e in lines:
    e = e.strip()
    a, b = e.split(",")
    aa, ab = a.split("-")
    ba, bb = b.split("-")
    temp = [make_set(int(aa), int(ab)), make_set(int(ba), int(bb))]

    data.append(temp)
# print(data)
n = len(data)
# print(n)
c = 0
for i in data:
    # if setissubset(i[0], i[1]):
    if contains_same_value(i[0], i[1]):
        c += 1
print(c)
