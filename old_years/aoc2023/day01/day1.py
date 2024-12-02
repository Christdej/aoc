number = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def strip_to_ints(line):
    # data = []
    first_i = len(line)
    first_c = -1
    last_i = 0
    last_c = -1
    for i, c in enumerate(line):
        if c.isdigit():
            if first_i > i:
                first_i = i
                first_c = c
            if last_i < i:
                last_i = i
                last_c = c
            # data.append(c)
    # print("AFTER DIGIT LOOP")
    # print(first_c)
    # print(last_c)

    for key, value in number.items():
        first_str = line.find(key)
        if first_str == -1:
            continue
        if first_str < first_i:
            first_i = first_str
            first_c = value

        last_str = line.rfind(key)
        if last_str == -1:
            continue
        if last_str > last_i:
            last_i = last_str
            last_c = value
    # print("AFTER STR LOOP")
    # print(first_c)
    # print(last_c)
    # data.append([str(first_c), str(last_c)])
    if first_c == -1:
        first_c = last_c
    if last_c == -1:
        last_c = first_c
    return [str(first_c), str(last_c)]


def string_to_number(c):
    if c == "one":
        return 1
    elif c == "two":
        return 2
    elif c == "three":
        return 3
    elif c == "four":
        return 4


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


# assert sonar_sweep(data, window_size=3) == 5


with open("input") as f:
    lines = f.readlines()
data = []
for e in lines:
    e = e.strip()
    data.append(strip_to_ints(e))
    # data.append(e)
    # if e.isdigit():
    #     data.append(int(e))
    # else:
    #     data.append(-1)
print(data)

# result = []
# for l in data:
#     result.append([l[0], l[-1]])
# print(result)

s = 0
for l in data:
    s += int(l[0] + l[1])
    # s += l[1]

print(s)
# sums = sum_with_spaces(data)
# sums.sort(reverse=True)
# print(sums[0])
# print(sum(sums[0:3]))
# data = [int(e) for e in data if (e != "")]
# print(data)
# print(sonar_sweep(data, window_size=3))
