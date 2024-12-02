def sum_with_spaces(list):
    sums = []
    temp_sum = 0
    for i in list:
        if i == -1:
            sums.append(temp_sum)
            temp_sum = 0
        else:
            temp_sum += i
    return sums


# assert sonar_sweep(data, window_size=3) == 5


with open("input") as f:
    lines = f.readlines()
data = []
for e in lines:
    e = e.strip()
    if e.isdigit():
        data.append(int(e))
    else:
        data.append(-1)

sums = sum_with_spaces(data)
sums.sort(reverse=True)
print(sums[0])
print(sum(sums[0:3]))
# data = [int(e) for e in data if (e != "")]
# print(data)
# print(sonar_sweep(data, window_size=3))
