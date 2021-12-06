import numpy as np


def parse_line(line):
    return list(map(int, list(line)))


def parse_data(data):
    y = len(data[0])
    x = len(data)
    m = np.zeros((x, y))
    for i, l in enumerate(data):
        m[i, :] = parse_line(l)
    return m


def binary_diagnostic_part1(data):
    x = len(data[0])
    y = len(data)
    c = np.zeros((x, 2))
    m = parse_data(data)

    ones = np.count_nonzero(m == 1, axis=0)
    c[:, 0] = np.subtract((np.ones(x) * y), ones)
    c[:, 1] = ones

    gamma_rate = np.argmax(c, axis=1)
    epsilon_rate = np.argmin(c, axis=1)
    gamma_num = int("".join(map(str, gamma_rate)), 2)
    epsilon_num = int("".join(map(str, epsilon_rate)), 2)
    return gamma_num * epsilon_num


def binary_diagnostic_part2(data):
    m = parse_data(data)
    x = len(data[0])
    temp_m_oxygen = parse_data(data)
    oxygen_num = 0

    for i in range(x):
        y = len(temp_m_oxygen)
        c = np.zeros((x, 2))
        ones = np.count_nonzero(temp_m_oxygen == 1, axis=0)
        c[:, 0] = np.subtract((np.ones(x) * y), ones)
        c[:, 1] = ones
        if c[i, 0] > c[i, 1]:
            bla = np.squeeze(np.where(c[:, 1] < c[:, 0]))
            oxygen_rate = np.ones(x)
            for e in bla:
                oxygen_rate[e] = 0
        else:
            bla = np.squeeze(np.where(c[:, 1] >= c[:, 0]))
            oxygen_rate = np.zeros(x)
            for e in bla:
                oxygen_rate[e] = 1

        if oxygen_rate[i] == 0:
            mask = np.where(temp_m_oxygen[:, i] == 0)
        else:
            mask = np.where(temp_m_oxygen[:, i] == 1)
        temp_m_oxygen = np.squeeze(temp_m_oxygen[mask, :], axis=0)
        if len(temp_m_oxygen) == 1:
            break

    temp_m_co2 = parse_data(data)
    co2_num = 0
    for i in range(x):
        y = len(temp_m_co2)
        c = np.zeros((x, 2))
        ones = np.count_nonzero(temp_m_co2 == 1, axis=0)
        c[:, 0] = np.subtract((np.ones(x) * y), ones)
        c[:, 1] = ones
        if c[i, 0] <= c[i, 1]:
            bla = np.squeeze(np.where(c[:, 1] >= c[:, 0]))
            co2_rate = np.ones(x)
            for e in bla:
                co2_rate[e] = 0
        else:
            bla = np.squeeze(np.where(c[:, 1] < c[:, 0]))
            co2_rate = np.zeros(x)
            for e in bla:
                co2_rate[e] = 1
        if co2_rate[i] == 0:
            mask = np.where(temp_m_co2[:, i] == 0)
        else:
            mask = np.where(temp_m_co2[:, i] == 1)
        temp_m_co2 = np.squeeze(temp_m_co2[mask, :], axis=0)
        if len(temp_m_co2) == 1:
            break

    oxygen_rate = [int(e) for e in temp_m_oxygen[0]]
    oxygen_num = int("".join(map(str, oxygen_rate)), 2)

    co2_rate = [int(e) for e in temp_m_co2[0]]
    co2_num = int("".join(map(str, co2_rate)), 2)
    return oxygen_num * co2_num


data = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]
assert binary_diagnostic_part1(data) == 198
assert binary_diagnostic_part2(data) == 230

with open("input") as f:
    lines = f.readlines()

data = [e.strip() for e in lines]

print(binary_diagnostic_part1(data))
print(binary_diagnostic_part2(data))
