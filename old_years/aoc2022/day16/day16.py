import os

import networkx as nx
import numpy as np

T0 = 30
G = nx.DiGraph()


def parse_data(data):
    temp = []
    for l in data:
        e = l.strip().split(" ")
        v = e[1]
        r = int(e[4].split("=")[1][0:-1])
        lt = l.strip().split("valve")[1]
        lt = e[9:]
        lead = [t.strip().split(",")[0] for t in lt]
        temp.append({"name": v, "rate": r, "lead": lead})
    for i in temp:
        G.add_node(i["name"], rate=i["rate"])
    for i in temp:
        for n in i["lead"]:
            w = 25 - i["rate"]
            G.add_edge(i["name"], n, rate=w)
    return temp


def part1():
    paths = []
    cycles = nx.recursive_simple_cycles(G)
    weights = nx.get_edge_attributes(G, "rate")
    for c in cycles:
        cycles.append(c[0])
        sumw = sum([weights[(c[i - 1], c[i])] for i in range(1, len(c))])
    # for n in G.nodes():
    #     path = [p for p in nx.all_shortest_paths(G, "AA", n)]
    #     paths.append({"start": "AA", "end": n, "paths": path})
    print("PATHS: ", cycles)


def part2():
    return


dirname = os.path.dirname(__file__)
with open(dirname + "/" + "input") as f:
    lines = f.readlines()
data = parse_data(lines)
print("DATA: ", data)
print("PART 1: ", part1())
print("PART 2: ", part2())


import os
from collections import defaultdict
from functools import partial
from itertools import combinations, product
from math import inf as INFINITY
from operator import itemgetter


def floyd_warshall(g):
    distance = defaultdict(lambda: defaultdict(lambda: INFINITY))

    for a, bs in g.items():
        distance[a][a] = 0

        for b in bs:
            distance[a][b] = 1
            distance[b][b] = 0

    for a, b, c in product(g, g, g):
        bc, ba, ac = distance[b][c], distance[b][a], distance[a][c]

        if ba + ac < bc:
            distance[b][c] = ba + ac

    return distance


def score(rates, valves):
    s = 0
    for v, t in valves.items():
        s += rates[v] * t
    return s


def solutions(distance, rates, valves, time=30, cur="AA", chosen={}):
    for nxt in valves:
        new_time = time - distance[cur][nxt] - 1
        if new_time < 2:
            continue

        new_chosen = chosen | {nxt: new_time}
        yield from solutions(distance, rates, valves - {nxt}, new_time, nxt, new_chosen)

    yield chosen


graph = defaultdict(list)
rates = {}

dirname = os.path.dirname(__file__)
with open(dirname + "/" + "input") as f:
    for fields in map(str.split, f):
        src = fields[1]
        dsts = list(map(lambda x: x.rstrip(","), fields[9:]))
        rate = int(fields[4][5:-1])

        rates[src] = rate

        for dst in dsts:
            graph[src].append(dst)

good = frozenset(filter(rates.get, graph))
distance = floyd_warshall(graph)
score = partial(score, rates)
best = max(map(score, solutions(distance, rates, good)))

print("BEST PART 1: ", best)


maxscore = defaultdict(int)

for solution in solutions(distance, rates, good, 26):
    k = frozenset(solution)
    s = score(solution)

    if s > maxscore[k]:
        maxscore[k] = s

best = max(
    sa + sb for (a, sa), (b, sb) in combinations(maxscore.items(), 2) if not a & b
)
print("BEST PART 2: ", best)
