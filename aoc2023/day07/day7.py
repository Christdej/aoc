import re
from dataclasses import dataclass
from functools import total_ordering

import numpy as np


@total_ordering
@dataclass(eq=False)
class Hand:
    hand: str
    bid: int

    def __eq__(self, other) -> bool:
        self_type = determine_type(self)
        other_type = determine_type(other)
        if self_type == other_type:
            return hands_equal(self, other)
        return False

    def __lt__(self, other) -> bool:
        self_type = determine_type(self)
        other_type = determine_type(other)
        if self_type != other_type:
            return self_type > other_type
        return hand_1_stronger(self, other)


def determine_type(hand: Hand):
    cards = list(hand.hand)
    print("CARDS: ", cards)
    cc = []
    set_cards = set(cards)
    n_j = cards.count("J")
    if n_j:
        set_cards.remove("J")
    for c in set_cards:
        cc.append(cards.count(c))
    cc.sort(reverse=True)
    print("CC: ", cc)
    if not cc:
        return 7
    cc[0] += n_j
    if len(cc) == 1:
        return 7
    if cc[0] == 4:
        return 6
    if cc[0] == 3:
        if cc[1] == 2:
            return 5
        return 4
    if cc[0] == 2:
        if cc[1] == 2:
            return 3
        return 2
    return 1


def hands_equal(hand1: Hand, hand2: Hand) -> bool:
    cards1 = list(hand1.hand)
    cards2 = list(hand2.hand)
    for i, k in enumerate(cards1):
        if k != cards2[i]:
            return False
    return True


def hand_1_stronger(hand1: Hand, hand2: Hand) -> bool:
    card_strength = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "J": 0,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
    }
    cards1 = list(hand1.hand)
    cards2 = list(hand2.hand)
    for i, k in enumerate(cards1):
        if card_strength[k] > card_strength[cards2[i]]:
            return True
        if card_strength[k] < card_strength[cards2[i]]:
            return False
    return False


with open("input") as f:
    lines = f.readlines()


data = [l.strip() for l in lines]
hands = []
for l in data:
    hand, bid = l.split(" ")
    h = Hand(hand, int(bid))
    hands.append(h)

hands.sort(reverse=True)
total_winning = 0
for i, h in enumerate(hands):
    total_winning += h.bid * (i + 1)
# print("SORTED HANDS: ", hands)
print(total_winning)
