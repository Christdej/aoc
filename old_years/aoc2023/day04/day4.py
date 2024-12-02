import re

import numpy as np

# def check_card(line):
#     points = 0
#     wn = line[0]
#     mn = line[1]
#     for i in mn:
#         if i in wn:
#             points += 1
#     return points


# with open("input_ex") as f:
#     lines = f.readlines()
# data = []
# for e in lines:
#     e = e.split("|")
#     wn = e[0].split(":")[1].strip().split(" ")
#     wn = [int(n) for n in wn if n]
#     mn = e[1].strip().split(" ")
#     mn = [int(n) for n in mn if n]
#     data.append([wn, mn])
# print(data)
# points_cards = np.ones((len(data), 1), dtype=int)
# n_cards = np.zeros((len(data), 1), dtype=int)

# for i, l in enumerate(data):
#     n_cards[i] = check_card(l)

# print(n_cards)

# for i, l in enumerate(n_cards):
#     print("i: ", i)
#     print("l :", l)
#     for k in range(l[0] - 1):
#         points_cards[i + k + 1] += 1
#     for j in points_cards[i]:
#         points_cards[i + j + 1] += 1
#     n_cards[i] = check_card(l)

# print(points_cards)


input_data = open("input").read().splitlines()
card_counter = {card_number: 1 for card_number in range(1, len(input_data) + 1)}
for card_number, line in enumerate(input_data, start=1):
    left, right = line.split(":")[1].split("|")
    winning_numbers = {int(number) for number in re.findall(r"\d+", left)}
    my_numbers = {int(number) for number in re.findall(r"\d+", right)}
    num_matches = len(winning_numbers & my_numbers)

    for won_copies in range(card_number + 1, card_number + 1 + num_matches):
        card_counter[won_copies] += card_counter[card_number]

print(sum(card_counter.values()))
