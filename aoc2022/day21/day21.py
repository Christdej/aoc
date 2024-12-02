import operator
import os

import numpy as np


def parse_data(data):
    s = []
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "==": operator.eq,
    }
    for l in data:
        n, o = l.strip().split(": ")
        o = o.strip()
        if o.isdigit():
            s.append({"name": n, "number": int(o)})
        else:
            o1, op, o2 = o.split(" ")
            if n == "root":
                s.append({"name": n, "o1": o1, "o2": o2, "op": ops["=="]})
            s.append({"name": n, "o1": o1, "o2": o2, "op": ops[op]})
    return s


def command(monkey):
    # global DATA
    # print("MOKNEY: ", monkey)
    if "number" in monkey:
        return monkey["number"]
    else:
        o1 = monkey["o1"]
        o1 = [m for m in DATA if m["name"] == o1][0]
        o2 = monkey["o2"]
        o2 = [m for m in DATA if m["name"] == o2][0]
        op = monkey["op"]
        return op(command(o1), command(o2))


def part1():
    m = [m for m in DATA if m["name"] == "root"][0]
    return command(m)


def part2():
    from functools import reduce

    parse = lambda line: {line[:4]: line[6:-1].split(" ")}
    ast_nodes = reduce(lambda a, b: a | b, (parse(x) for x in open("input")))

    def sub(name):
        expr = ast_nodes[name]
        if name == "humn":
            return "humn"
        if len(expr) == 1:
            return expr[0]
        left, op, right = expr
        if name == "root":
            op = "-"
        return f"({sub(left)}){op}({sub(right)})"

    fn = eval(f"lambda humn: {sub('root')}")
    a, b = [x * 100000000000000 for x in [-1, 1]]
    while True:
        c = (b + a) // 2
        if fn(c) == 0:
            print(c)
            break
        if fn(c) * fn(a) < 0:
            b = c
        else:
            a = c
    print("A, B: ", a, b)


dirname = os.path.dirname(__file__)
with open(dirname + "/" + "input") as f:
    lines = f.readlines()
DATA = parse_data(lines)
# print("DATA: ", DATA)

print("PART 1: ", part1())

print("PART 2: ", part2())
