import os

import networkx as nx
import numpy as np

START = [0, 0]
END = [0, 0]
# ord("a") = 97
def cord(c):
    if c == "S":
        return 0
    if c == "E":
        return 25
    return ord(c) - 97


def find_neighbours(arr):

    neighbors = []

    for i in range(len(arr)):
        for j, value in enumerate(arr[i]):

            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
                # corners
                new_neighbors = []
                pos_neightbors = []
                if i != 0:
                    new_neighbors.append(arr[i - 1][j])  # top neighbor
                    pos_neightbors.append([i - 1, j])
                if j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i][j + 1])  # right neighbor
                    pos_neightbors.append([i, j + 1])
                if i != len(arr) - 1:
                    new_neighbors.append(arr[i + 1][j])  # bottom neighbor
                    pos_neightbors.append([i + 1, j])
                if j != 0:
                    new_neighbors.append(arr[i][j - 1])  # left neighbor
                    pos_neightbors.append([i, j - 1])

            else:
                # add neighbors
                new_neighbors = [
                    arr[i - 1][j],  # top neighbor
                    arr[i][j + 1],  # right neighbor
                    arr[i + 1][j],  # bottom neighbor
                    arr[i][j - 1],  # left neighbor
                ]
                pos_neightbors = [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]]

            neighbors.append(
                {
                    "value": value,
                    "pos": [i, j],
                    "neighbors": new_neighbors,
                    "pos_neighbors": pos_neightbors,
                }
            )

    return neighbors


def parse_data(data):
    global START
    global END
    temp = []
    for i, l in enumerate(data):
        a = list(l)
        for j, b in enumerate(a):
            if b == "S":
                START = [i, j]
            if b == "E":
                END = [i, j]
        a = [cord(c) for c in a]
        temp.append(a)
    return np.array(temp)


dirname = os.path.dirname(__file__)
with open(dirname + "/" + "input") as f:
    lines = f.readlines()
data = []
for l in lines:
    e = l.strip()
    data.append(e)
data = parse_data(data)
# print("DATA: ", data)
neigh = find_neighbours(data)
# print("NEIGH: ", neigh)

G = nx.DiGraph()
c = 0
for n in neigh:
    G.add_node(c, pos=n["pos"])
    c += 1

# START_NODE = G.nodes[0]
START_NODES = []
END_NODE = G.nodes[0]
indexes = np.where(data == 0)
indexes = list(map(list, zip(indexes[0], indexes[1])))
# indexes = list(zip(indexes[0], indexes[1]))
# print("IDX: ", indexes)
for x, y in G.nodes(data=True):
    if y["pos"] in indexes:
        START_NODES.append(x)
    if y["pos"] == END:
        END_NODE = x
# print("START NODES: ", START_NODES)

for i, n in enumerate(neigh):
    # print("N: ", n)
    v = n["value"]
    ns = n["neighbors"]
    tn = n["pos"]
    pos_ns = n["pos_neighbors"]
    for j, k in enumerate(ns):
        if k <= v + 1:
            this_node = G.nodes[0]
            neigh_node = G.nodes[0]
            for x, y in G.nodes(data=True):
                if y["pos"] == tn:
                    this_node = x
                if y["pos"] == pos_ns[j]:
                    neigh_node = x
                # if y["pos"] == u:
                # print("START CALLED")
                # sn = x
                # if y["pos"] == END:
                # print("END CALLED")
                # END_NODE = x
            # print("THIS NODE: ", this_node)
            # print("NEIGH NODE: ", neigh_node)
            G.add_edge(this_node, neigh_node)
sp = 1000
sn = G.nodes()[0]
for u in START_NODES:
    try:
        p = nx.shortest_path(G, source=u, target=END_NODE)
        if len(p) - 1 < sp:
            sp = len(p) - 1
    except:
        print("NO PATH")
        continue


# print("GRAPH NODES: ", G.nodes())
# print("GRAPH EDGES: ", G.edges())
# print("DATA: \n", data)
# print("START: ", START)
# print("END: ", END)

# print("PATH: ", p)
print("SHORTEST PATH: ", sp)


"""
for x, y in graph.nodes(data=True):
            # print("X: ", x)
            # print("Y: ", y)
            if y["label"] == new_dir:
                if x in succ:
                    node.append(x)
"""
