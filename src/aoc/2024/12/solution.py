import math
import os
import time

import numpy as np

from aoc.util import create_graph, depth_first_search, dfs_graph


def first_task(input_data: list[str]):
    # G = create_graph(input_data)
    G = {
        (i) + (j) * 1j: e for i, row in enumerate(input_data) for j, e in enumerate(row)
    }
    # print("G: ", G)
    # dirs = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    dirs = (1, -1, 1j, -1j)
    visited = set()

    def dfs(p, t, region, fence, dr=None):
        # print("P: ", p)
        # print("E: ", e)
        # print("Region: ", region)
        # print("Fence: ", fence)
        if p in visited and G.get(p) == t:
            return
        if G.get(p) != t:
            return fence.add((p, dr))
        visited.add(p), region.add(p)
        for dr in dirs:
            dfs(p + dr, t, region, fence, dr)
        neighbors = {(p + dr * 1j, dr) for p, dr in fence}
        # print("Neighbors: ", neighbors)
        return len(region), len(fence), len(fence - neighbors)

    regions = [dfs(p, e, set(), set()) for p, e in G.items() if p not in visited]
    # print("Regions: ", regions)
    # print("visited: ", visited)
    part1 = sum(area * perim for area, perim, _ in regions)
    print("Part1: ", part1)

    # G = create_graph(input_data)
    # print("G: ", G)
    # regions = []
    # fence = []
    # # visited = set()

    # def dfs_graph(G, p, t, visited=None):
    #     print("P: ", p)
    #     print("T: ", t)
    #     if visited is None:
    #         visited = set()
    #     if p in visited and G.get(p) == t:
    #         return visited
    #     if G.get(p) != t:
    #         return set()
    #     visited.add(p)
    #     print("Visited: ", visited)
    #     neighbours = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    #     for a in neighbours:
    #         temp = (p[0] + a[0], p[1] + a[1])
    #         print("Temp: ", temp)
    #         visited, region = dfs_graph(
    #             G, (p[0] + a[0], p[1] + a[1]), t, region, visited
    #         )
    #     return visited, region

    # for p, v in G.items():
    #     region = set()
    #     #     # temp = []
    #     #     if p in visited:
    #     #         continue
    #     temp = dfs_graph(G, p, v)
    #     regions.append(temp)
    # print("Regions: ", regions)
    return part1


def second_task(input_data: list[str]):
    G = {
        (i) + (j) * 1j: e for i, row in enumerate(input_data) for j, e in enumerate(row)
    }
    # print("G: ", G)
    # dirs = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    dirs = (1, -1, 1j, -1j)
    visited = set()

    def dfs(p, t, region, fence, dr=None):
        # print("P: ", p)
        # print("E: ", e)
        # print("Region: ", region)
        # print("Fence: ", fence)
        if p in visited and G.get(p) == t:
            return
        if G.get(p) != t:
            return fence.add((p, dr))
        visited.add(p), region.add(p)
        for dr in dirs:
            dfs(p + dr, t, region, fence, dr)
        neighbors = {(p + dr * 1j, dr) for p, dr in fence}
        # print("Neighbors: ", neighbors)
        return len(region), len(fence), len(fence - neighbors)

    regions = [dfs(p, e, set(), set()) for p, e in G.items() if p not in visited]
    part2 = sum(area * sides for area, _, sides in regions)
    return part2


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
