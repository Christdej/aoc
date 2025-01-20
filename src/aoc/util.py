def find_neighbours(arr):
    neighbors = []

    for i in range(len(arr)):
        for j, value in enumerate(arr[i]):
            ns = get_neighbors_indexes(arr, i, j)
            new_neighbors = []
            for t in ns:
                new_neighbors.append(arr[t[0]][t[1]])
            neighbors.append(
                {
                    "value": value,
                    "pos": [i, j],
                    "neighbors": new_neighbors,
                    "pos_neighbors": ns,
                }
            )
    return neighbors


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


def get_lines_through_pos(arr, i, j):
    lines = []
    if i == 0 or j == 0:
        return lines
    if i == len(arr) - 1 or j == len(arr[0]) - 1:
        return lines
    lines.append([arr[i + 1][j], arr[i - 1][j]])
    lines.append([arr[i][j + 1], arr[i][j - 1]])
    lines.append([arr[i + 1][j + 1], arr[i - 1][j - 1]])
    lines.append([arr[i + 1][j - 1], arr[i - 1][j + 1]])
    return lines


# Values of neightbors that form line
def get_lines_through_pos_up_down_left_right(arr, i, j):
    lines = []
    if i == 0 or j == 0:
        return lines
    if i == len(arr) - 1 or j == len(arr[0]) - 1:
        return lines
    lines.append([arr[i + 1][j], arr[i - 1][j]])
    lines.append([arr[i][j + 1], arr[i][j - 1]])
    return lines


def get_lines_through_pos_diagonal(arr, i, j):
    lines = []
    if i == 0 or j == 0:
        return lines
    if i == len(arr) - 1 or j == len(arr[0]) - 1:
        return lines
    lines.append([arr[i + 1][j + 1], arr[i - 1][j - 1]])
    lines.append([arr[i + 1][j - 1], arr[i - 1][j + 1]])
    return lines


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def depth_first_search(arr, start_x, start_y, target, prev=-1):
    neighbours = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    if (
        start_x < 0
        or start_x >= len(arr)
        or start_y < 0
        or start_y >= len(arr[start_x])
    ):
        return set()
    v = arr[start_x][start_y]
    if v != prev + 1:
        return set()
    if v == target:
        return {(start_x, start_y)}
    r = set()
    for a in neighbours:
        r = r.union(depth_first_search(arr, start_x + a[0], start_y + a[1], target, v))
    return r


def create_graph(arr):
    G = {}
    for i, row in enumerate(arr):
        for j, e in enumerate(row):
            G[(i, j)] = e
    return G


# G = {(i)+(j)*1j: e for i, row in enumerate(data) for j, e   in enumerate(row)}

# visited = set()


def dfs_graph(G, p, t, prev=-1):
    print("P: ", p)
    print("T: ", t)
    if p in visited and G.get(p) == t:
        return {p}
    if G.get(p) != t:
        return set()
    visited.add(p)
    r = set()
    neighbours = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    for a in neighbours:
        print("A: ", a)
        temp = dfs_graph(G, (p[0] + a[0], p[1] + a[1]), t, prev=p)
        print("Temp: ", temp)
        visited = visited.union(temp)
    # neighbors = {(p + dr * 1j, dr) for p, dr in fence}
    return r
