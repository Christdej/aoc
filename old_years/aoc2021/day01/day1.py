def sliding_windows(data, window_size):
    windows = []
    for i in range(len(data) - window_size + 1):
        windows.append(data[i : i + window_size])
    return windows


def sonar_sweep(data, window_size=1):
    r = sliding_windows(data, window_size=window_size)
    f = r[0]
    n = 0
    for i in r[1:]:
        if sum(i) > sum(f):
            n += 1
        f = i
    return n


data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

assert sonar_sweep(data, window_size=3) == 5


with open("input") as f:
    lines = f.readlines()

data = [int(e) for e in lines]

print(sonar_sweep(data, window_size=3))
