import math
import os
import time

import numpy as np


def first_task(input_data: list[str]):
    l1 = []
    l2 = []
    for line in input_data:
        a, b = line.split("   ")
        l1.append(int(a))
        l2.append(int(b))
    l1.sort()
    l2.sort()
    s = sum(abs(l1[i] - l2[i]) for i in range(len(l1)))
    # print(s)
    return s


def second_task(input_data: list[str]):
    l1 = []
    l2 = []
    for line in input_data:
        a, b = line.split("   ")
        l1.append(int(a))
        l2.append(int(b))
    similarity_score = 0
    for c in l1:
        a = c * l2.count(c)
        # print("ASDASD: ", a)
        similarity_score += a
    return similarity_score


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
