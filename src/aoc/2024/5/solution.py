import math
import os
import time

import numpy as np


def fix_input(input_data: list[str]):
    rules = {}
    # print("INPUT: ", input_data)
    flag = False
    updates = []
    for l in input_data:
        if len(l) == 0:
            flag = True
            continue
        if flag:
            updates.append([int(x) for x in l.split(",")])
        else:
            a, b = [int(x) for x in l.split("|")]
            if a not in rules:
                rules[a] = set()
            rules[a].add(b)
    return rules, updates


def first_task(input_data: list[str]):
    rules, updates = fix_input(input_data)
    # print("RULES: ", rules)
    # print("UPDATES: ", updates)
    c = 0
    for u in updates:
        read = set()
        for n in u:
            should_add = True
            if n in rules and len(rules[n].intersection(read)) > 0:
                should_add = False
                break
            read.add(n)
        if should_add:
            c += u[len(u) // 2]
    return c


def find_invalid(n, i, rules):
    v = n[i]
    if v not in rules:
        return -1
    for j in range(i):
        if n[j] in rules[v]:
            return j
    return -1


def sort_updates(u, rules, step=0):
    # print("UPDATE: ", u)
    p = -1
    for i in range(len(u)):
        p = find_invalid(u, i, rules)
        if p != -1:
            u = u[:p] + [u[i]] + u[p:i] + u[i + 1 :]
            print("U:", u)
            print("P: ", p)
            print("I: ", i)
            print("UI: ", u[i])
            print("U : P ", u[:p], u[p:i], u[i + 1 :])
            break
    if p == -1:
        return u
    return sort_updates(u, rules, step + 1)


def second_task(input_data: list[str]):
    rules, updates = fix_input(input_data)
    # print("RULES: ", rules)
    # print("UPDATES: ", updates)
    c = 0
    for u in updates:
        read = set()
        for n in u:
            should_add = False
            if n in rules and len(rules[n].intersection(read)) > 0:
                should_add = True
                break
            read.add(n)
        if should_add:
            new_u = sort_updates(u, rules)
            # print("NEW: ", new_u)
            c += new_u[len(new_u) // 2]
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
