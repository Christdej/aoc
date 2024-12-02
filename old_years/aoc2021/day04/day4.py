import numpy as np


def check_board(board):
    for r in board:
        if np.count_nonzero(r) == 5:
            return True
    for c in board.T:
        if np.count_nonzero(c) == 5:
            return True
    return False


def num_won_boards(boards):
    # n_boards = np.shape(boards)[0]
    won_boards = 0
    not_won = -1
    for i, b in enumerate(boards):
        if check_board(b):
            won_boards += 1
        else:
            not_won = i
    return not_won, won_boards


def mark_board(board, m_board, num):
    for i, r in enumerate(board):
        for j, v in enumerate(r):
            if v == num:
                m_board[i, j] = 1


def bingo(numbers, boards):
    n_boards = np.shape(boards)[0]
    marked_boards = np.zeros((n_boards, 5, 5))
    last_marked = -1
    for num in numbers:
        for i, board in enumerate(boards):
            m_board = marked_boards[i]
            mark_board(board, m_board, num)
            # if check_board(m_board):
            #     return num, board, m_board
        j, won_boards = num_won_boards(marked_boards)
        if j > 0:
            last_marked = j
        print("LAST MARKED: ", j)
        if won_boards == n_boards:
            return num, boards[last_marked], marked_boards[last_marked]


def parse_input(data):
    numbers = [int(e) for e in data[0].split(",")]
    n_boards = int((len(data) - 1) / 6)
    boards = np.zeros((n_boards, 5, 5))
    c = 0
    c2 = 0
    for l in data[2:]:
        bla = [int(e) for e in (l.split())]
        if len(bla) > 0:
            boards[c, c2, :] = bla
            c2 += 1
            c2 = c2 % 5
        else:
            c += 1
    return numbers, boards


def giant_squid(numbers, boards):
    num, board, m_board = bingo(numbers, boards)
    print(num, board, m_board)
    unmarked_sum = 0
    for i, r in enumerate(board):
        for j, v in enumerate(r):
            if m_board[i, j] == 0:
                unmarked_sum += v
    return unmarked_sum * num


boards = np.zeros((3, 5, 5))
boards[0, :, :] = [
    [22, 13, 17, 11, 0],
    [8, 2, 23, 4, 24],
    [21, 9, 14, 16, 7],
    [6, 10, 3, 18, 5],
    [1, 12, 20, 15, 19],
]
boards[1, :, :] = [
    [3, 15, 0, 2, 22],
    [9, 18, 13, 17, 5],
    [19, 8, 7, 25, 23],
    [20, 11, 10, 24, 4],
    [14, 21, 16, 12, 6],
]
boards[2, :, :] = [
    [14, 21, 17, 24, 4],
    [10, 16, 15, 9, 19],
    [18, 8, 23, 26, 20],
    [22, 11, 13, 6, 5],
    [2, 0, 12, 3, 7],
]
numbers = [
    7,
    4,
    9,
    5,
    11,
    17,
    23,
    2,
    0,
    14,
    21,
    24,
    10,
    16,
    13,
    6,
    15,
    25,
    12,
    22,
    18,
    20,
    8,
    19,
    3,
    26,
    1,
]


assert giant_squid(numbers, boards) == 1924


with open("input") as f:
    lines = f.readlines()

data = [e for e in lines]
numbers, boards = parse_input(data)
print(numbers)
print(boards)

print(giant_squid(numbers, boards))
