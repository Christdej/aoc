import re
from collections import deque

examples = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]

expected_marker = [7, 5, 6, 10, 11]

# seq = [0, 1, 2, 3, 4, 5]
# window_size = 3


def sliding_window(seq, window_size):
    temp = []
    for i in range(len(seq) - window_size + 1):
        temp.append(seq[i : i + window_size])
    return temp


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


with open("input") as f:
    lines = f.readlines()
data = []
# for l in lines:
data = list(lines[0].strip())

data = sliding_window(data, 14)
# print(data)

for i, e in enumerate(data):
    s = set(e)
    if len(s) == 14:
        print(i + 14)
        break
