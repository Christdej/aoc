def power_of_game(game):
    lim = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for set in game:
        for hand in set:
            s = hand.strip()
            s = s.split(" ")
            n = int(s[0])
            c = s[1].strip()
            if n > lim[c]:
                lim[c] = n

    return lim["red"] * lim["green"] * lim["blue"]


def divide_game_to_sets(line):
    game = []
    print("LINE ", line)
    line = line.split(";")
    for l in line:
        game.append(l.split(","))

    return game


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


with open("input") as f:
    lines = f.readlines()
data = []
for e in lines:
    e = e.split(":")[1]
    e = e.strip()
    data.append(divide_game_to_sets(e))
print(data)

c = 0
for i, game in enumerate(data):
    c += power_of_game(game)
print(c)
