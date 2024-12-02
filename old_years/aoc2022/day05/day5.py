import re
from collections import deque


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def prepare_moves(moves):
    temp = []
    for e in moves:
        a, b = e.split("from")
        a = re.findall(r"\d", a)
        a = "".join(a)
        move = int(a)
        b, c = b.split("to")
        stack_from = int(b.strip())
        stack_to = int(c.strip())
        temp.append([move, stack_from, stack_to])
    return temp


def prepare_cargo(cargo):
    n = len("".join(cargo[-1].split()))
    data = [[] for _ in range(n)]
    for i, e in enumerate(cargo[:-1]):
        c = 1
        for j in range(n):
            if c > len(e):
                break
            if e[c].isupper():
                data[j].append(e[c])
            c += 4
    temp = []
    for i in data:
        queue = deque(i)
        queue.reverse()
        temp.append(queue)
    return temp


def rearrange_cargo(cargo, move):
    x = move[0]
    from_ = move[1]
    to_ = move[2]
    temp = []
    for i in range(x):
        popped = cargo[from_ - 1].pop()
        temp.append(popped)
    temp.reverse()
    cargo[to_ - 1].extend(temp)
    return cargo


with open("input") as f:
    lines = f.readlines()
data = []

break_line = 0
for i, e in enumerate(lines):
    e = e.strip()
    # print(e)
    if not e:
        break_line = i
    data.append(e)
cargo = lines[:break_line]
moves = data[break_line + 1 :]

cargo = prepare_cargo(cargo)
moves = prepare_moves(moves)
print("CARGO: ", cargo)
print("MOVES: ", moves)

for m in moves:
    cargo = rearrange_cargo(cargo, m)
    # print(cargo)

text = ""
for i in cargo:
    if len(i) < 1:
        continue
    text += i.pop()
print(cargo)
print(text)
