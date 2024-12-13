import math
import os
import time

import numpy as np


def first_task(input_data: list[str]):
    data = []
    for l in input_data:
        data.append([int(x) for x in l.split(" ")])
    diff = []
    for d in data:
        diff.append([d[i + 1] - d[i] for i in range(len(d) - 1)])
    c = 0
    min_lim = -3
    max_lim = 3
    print("DIFF: ", diff)
    for d in diff:
        if all(min_lim <= x <= -1 for x in d):
            c += 1
        if all(max_lim >= x >= 1 for x in d):
            c += 1
    return c


def second_task(input_data: list[str]):
    data = []
    for l in input_data:
        data.append([int(x) for x in l.split(" ")])
    c = 0
    min_lim = -3
    max_lim = 3
    for d in data:
        diff = [d[i + 1] - d[i] for i in range(len(d) - 1)]
        if all(min_lim <= x <= -1 for x in diff):
            c += 1
            continue
        if all(max_lim >= x >= 1 for x in diff):
            c += 1
            continue
        for j in range(len(d)):
            temp = d[:j] + d[j + 1 :]
            ddiff = [temp[i + 1] - temp[i] for i in range(len(temp) - 1)]
            # print("TEMP: ", temp)
            if all(min_lim <= x <= -1 for x in ddiff):
                c += 1
                break
            if all(max_lim >= x >= 1 for x in ddiff):
                c += 1
                break
    # diff = []
    # for d in data:
    #     diff.append([d[i + 1] - d[i] for i in range(len(d) - 1)])
    # print("DIFF: ", diff)
    # for d in diff:
    #     if all(min_lim <= x <= -1 for x in d):
    #         c += 1
    #         continue
    #     if all(max_lim >= x >= 1 for x in d):
    #         c += 1
    #         continue
    # remove the line if c += 1
    return c


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = list(map(lambda line: line.strip(), open(input_file, "r")))

    t_start = time.time()
    first_answer = first_task(input_data)
    t_end = time.time()
    first_time = round(t_end - t_start, 2)
    if first_answer is not None:
        # Create part1
        filename = os.path.join(os.path.dirname(__file__), "part1.txt")
        with open(filename, "w") as file:
            file.write(str(first_answer))

    print("#############################")
    print("The answer to the 1st task is")
    print(first_answer, f"in {first_time} seconds")

    t_start = time.time()
    second_answer = second_task(input_data)
    t_end = time.time()
    second_time = round(t_end - t_start, 3)
    if second_answer is not None:
        # Create part2
        filename = os.path.join(os.path.dirname(__file__), "part2.txt")
        with open(filename, "w") as file:
            file.write(str(second_answer))

    print()
    print("The answer to the 2nd task is")
    print(second_answer, f"in {second_time} seconds")
    print("#############################")


if __name__ == "__main__":
    run_day()
