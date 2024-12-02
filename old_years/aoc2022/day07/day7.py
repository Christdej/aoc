import random
import re
import string
from collections import deque

import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout, write_dot


def change_dir(graph, line, current_dir):
    if line.startswith("$"):
        if line.endswith("ls"):
            return current_dir
        if line.endswith(".."):
            if current_dir == 0:
                return current_dir
            # print("LINE: ", line)
            # print("CURRENT DIR: ", current_dir)
            return list(graph.predecessors(current_dir))[0]
        if line.endswith("/"):
            return 0
        new_dir = line.split(" ")[-1]
        # if new in graph.successors(current_dir):
        #     print("NEW ALREADY EXISTS")
        #     return
        succ = list(graph.successors(current_dir))
        # print("SUCC: ", succ)
        # nodes = G.nodes[succ]
        # node = [x for x, y in G.nodes(data=True) if y["label"] == new_dir and x in succ]
        node = []
        for x, y in graph.nodes(data=True):
            # print("X: ", x)
            # print("Y: ", y)
            if y["label"] == new_dir:
                if x in succ:
                    node.append(x)

        if len(node) > 1:
            print("NEW DIR: ", new_dir)
            print("NODES: ", node)
            print("LINE: ", line)
            print("CURRENT DIR: ", current_dir)
            print("THIS SHOULD NOT HAPPEND")
        if len(node) == 0:
            print("EMPTY NODE")
        node = node[0]
        return node
    return current_dir


def add_size(graph, line, current_dir):
    if line.startswith("$"):
        return
    if not line.startswith("dir"):
        size, file = line.split(" ")
        size = int(size)
        extend_graph(graph, file, current_dir, weight=size)
    elif line.startswith("dir"):
        new_dir = line.split(" ")[-1]
        # print("NEW DIR: ", new_dir)
        extend_graph(graph, new_dir, current_dir)


NODE_NUMBER = 1


def extend_graph(graph, new, current_dir, weight=0):
    # if new in graph.nodes():
    #     print("NODE ALREADY EXISTS")
    #     new = new + "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    # if new in graph.successors(current_dir):
    #     print("NEW ALREADY EXISTS")
    #     return
    # if new in graph.nodes():
    #     print("NEW EXISTS GLOBAL")
    #     # new = new + "".join(random.choices(string.ascii_uppercase + string.digits, k=4))

    #     graph.add_node(new, weight=weight)
    #     graph.add_edge(current_dir, new)
    #     return
    global NODE_NUMBER
    # print(NODE_NUMBER)
    # print("CURRENT DIR: ", current_dir)
    # print("NODE NUMBER: ", NODE_NUMBER)
    graph.add_node(NODE_NUMBER, label=new, weight=weight)
    graph.add_edge(current_dir, NODE_NUMBER)
    NODE_NUMBER += 1


with open("input") as f:
    lines = f.readlines()
data = []
for l in lines:
    e = l.strip()
    data.append(e)

G = nx.DiGraph()
G.add_node(0, label="/")
current_dir = 0
for l in data:
    current_dir = change_dir(G, l, current_dir)
    add_size(G, l, current_dir)

TOTAL_SPACE = 70000000
NEEDED_SPACE = 30000000

tot_sizes = dict()
for node in G.nodes:
    # S = G.subgraph(node)
    dec = nx.descendants(G, node)
    tot_size = 0
    for s in dec:
        n = G.nodes[s]
        w = n["weight"]
        if w:
            tot_size += w
    # print("TOT SIZE: ", tot_size)
    tot_sizes[node] = tot_size
# write_dot(G, "test.dot")
# plt.title("graph")
# pos = graphviz_layout(G, prog="dot")
# nx.draw(G, pos, with_labels=True, font_weight="bold")
# plt.savefig("graph.png")
# print(G.nodes(data=True))
# print(G.edges(data=True))
# print(tot_sizes)
c = 0
print("TOT SIZE: ", tot_sizes)
root_size = tot_sizes[0]
available_space = TOTAL_SPACE - root_size
space_required = NEEDED_SPACE - available_space
print("ROOT SIZE: ", root_size)
print("SPACE_REQ: ", space_required)
# biggest = max(tot_sizes, key=tot_sizes.get)
closes = 99999999999999
for key, value in tot_sizes.items():
    if value > space_required and value < closes:
        closes = value
print(closes)
# print(tot_sizes[biggest])
