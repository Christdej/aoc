def find_common_char(l1, l2, l3):
    chars = []
    # print("L1: ", l1)
    # print("L2: ", l2)
    # if len(l1) != len(l2):
    #     print("PLING")
    #     return
    for i in l1:
        for j in l2:
            for k in l3:
                if i == j and j == k and k == i:
                    # print(i)
                    # print(j)
                    chars.append(i)
                # print(chars)
    # if len(chars) > 1:
    #     print(chars)
    return chars[0]


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def points_for_char(char):
    if char.islower():
        return ord(char) - 96
    if char.isupper():
        return ord(char) - 64 + 26


with open("input") as f:
    lines = f.readlines()
data = []
for e in lines:
    e = e.strip()
    # d = e.split(" ")
    data.append(e)
# print(data)

points = 0
data = chunks(data, 3)
for i in data:
    # c = find_common_char(i[: len(i) // 2], i[len(i) // 2 :])
    print(i)
    # temp = data[i : i + window_size]
    c = find_common_char(i[0], i[1], i[2])
    print(c)
    points += points_for_char(c)
print(points)


# print(opponentdata)
# print(mydata)
