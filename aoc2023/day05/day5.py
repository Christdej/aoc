# import re


# def create_map(m, dest, source, r):
#     m[0].extend(list(range(dest, dest + r)))
#     m[1].extend(list(range(source, source + r)))
#     return m


# def update(m, seeds):
#     new_seeds = []
#     for i, s in enumerate(seeds):
#         source_idx = [i for i, j in enumerate(m[1]) if j == s]
#         if source_idx:
#             new_seeds.append(m[0][source_idx[0]])
#         else:
#             new_seeds.append(s)
#     return new_seeds


# with open("input_ex") as f:
#     lines = f.readlines()

# data = []
# lines = [l.strip() for l in lines if l]
# lines = [l for l in lines if l]
# # print(lines)
# s = lines[0]
# s = [int(number) for number in re.findall(r"\d+", s)]
# # print(s)
# do_map = 0
# dest = 0
# source = 0
# r = 0
# temp = []
# for i, e in enumerate(lines[1:]):
#     e = [int(number) for number in re.findall(r"\d+", e)]
#     if not e:
#         if temp:
#             data.append(temp)
#             temp = []
#     else:
#         temp.append(e)
# data.append(temp)
# ses = []
# ses.append(s)
# for i, m in enumerate(data):
#     sm = [[], []]
#     new_seed = []
#     for l in m:
#         sm = create_map(sm, l[0], l[1], l[2])
#     # print("SM: ", sm)
#     for v in s:
#         s_idx = [i for i, j in enumerate(sm[1]) if j == v]
#         if s_idx:
#             new_seed.append(sm[0][s_idx[0]])
#         else:
#             new_seed.append(v)
#     ses.append(new_seed)
# print("data: ", data)
# print("sm: ", sm)
# print("ses: ", ses)

# from typing import List

# file = open("./input").read().strip().split("\n\n")

# seeds = [int(x) for x in file[0].replace("seeds: ", "").split(" ")]

# # Map format: [[destination_range_start, source_range_start, range_length], ...]
# maps = [
#     [[int(y) for y in x.split(" ")] for x in file[i].splitlines()[1::]]
#     for i in range(1, 8)
# ]


# def x_to_y(step: int, m: List[List[int]]) -> int:
#     for destination_range_start, source_range_start, range_length in m:
#         if step >= source_range_start and step < source_range_start + range_length:
#             step = destination_range_start + (step - source_range_start)
#             break

#     return step


# r = float("inf")

# for seed in seeds:
#     for m in maps:
#         seed = x_to_y(seed, m)
#     r = min(r, seed)

# print(r)

from typing import List

file = open("./input").read().strip().split("\n\n")

seeds = [int(x) for x in file[0].replace("seeds: ", "").split(" ")]
ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

# Map format: [[destination_range_start, source_range_start, range_length], ...]
maps = [
    [[int(y) for y in x.split(" ")] for x in file[i].splitlines()[1::]]
    for i in range(1, 8)
]

# Reverse the maps
maps = [[(end, start, range_length) for start, end, range_length in m] for m in maps][
    ::-1
]


def x_to_y(step: int, m: List[List[int]]) -> int:
    for destination_range_start, source_range_start, range_length in m:
        if step >= source_range_start and step < source_range_start + range_length:
            step = destination_range_start + (step - source_range_start)
            break

    return step


def find_location(seed):
    x = seed
    for m in maps:
        x = x_to_y(x, m)

    return x


def contains(seed):
    return any(start <= seed < end for start, end in ranges)


location = 0
while True:
    seed = find_location(location)
    if contains(seed):
        print(f"r: {location}")
        break

    location += 1

    # Print progress
    if location % 1_000_000 == 0:
        print(location)
