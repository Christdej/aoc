def find_neighbours_one_pos(arr, i, j):
    new_neighbors = []
    ns = get_neighbors_indexes(arr, i, j)
    for t in ns:
        new_neighbors.append(arr[t[0]][t[1]])
    return {
        "value": arr[i][j],
        "pos": [i, j],
        "neighbors": new_neighbors,
        "pos_neighbors": ns,
    }


def get_neighbors_indexes(array, row, col):
    neighbors = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i == row and j == col:
                continue
            if 0 <= i < len(array) and 0 <= j < len(array[0]):
                neighbors.append([i, j])
    return neighbors


def get_valid_numbers(data):
    valid_numbers = []
    for j, l in enumerate(data):
        number = ""
        poses = []
        for i, c in enumerate(l):
            if c.isdigit():
                number += c
                poses.append([j, i])
                if i == len(l) - 1:
                    valid_numbers.append({"value": int(number), "positions": poses})
            else:
                if number:
                    valid_numbers.append({"value": int(number), "positions": poses})
                number = ""
                poses = []
    return valid_numbers


def is_number_neigh_with_symbol(data, dictt):
    sum_adj = 0
    for l in dictt:
        should_add = False
        for pos in l["positions"]:
            neigh = find_neighbours_one_pos(data, pos[0], pos[1])
            for i, n in enumerate(neigh["neighbors"]):
                if neigh["pos_neighbors"][i] in l["positions"]:
                    continue
                if not n == ".":  # and not n.isdigit():
                    should_add = True
        if should_add:
            sum_adj += l["value"]
    return sum_adj


def gear_ratio(data, dictt):
    gear_ratio = 0
    for i, l in enumerate(data):
        for j, c in enumerate(l):
            if c == "*":
                n_gears = 0
                gears = []
                neigh = find_neighbours_one_pos(data, i, j)
                print(neigh)
                # print(dictt)
                for pos in neigh["pos_neighbors"]:
                    # print("POS: ", pos)
                    for dic in dictt:
                        # print("N: ", dic)
                        if pos in dic["positions"]:
                            if dic not in gears:
                                n_gears += 1
                                gears.append(dic)
                            break
                if n_gears == 2:
                    gear_ratio += gears[0]["value"] * gears[1]["value"]
                print(n_gears)
    return gear_ratio


with open("input") as f:
    lines = f.readlines()
data = []
for e in lines:
    e = e.strip()
    data.append(e)
dictt = get_valid_numbers(data)
print(dictt)
# print(is_number_neigh_with_symbol(data, dictt))
print(gear_ratio(data, dictt))
# gear_ratio(data, dictt)
