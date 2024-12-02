import re
from functools import lru_cache

def find_mirror(pattern):
    l = len(pattern)
    for r in pattern:


data = []
pattern = []
for line in open("input_ex"):
    if not line.strip():
        data.append(pattern)
        pattern = []
        continue
    pattern.append(line.strip())
data.append(pattern)
# print(data)

for pattern in data:
    print(pattern)
