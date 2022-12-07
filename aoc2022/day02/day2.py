def what_to_choose(my, opp):
    if my == 1:
        if opp == 1:
            return 3
        if opp == 2:
            return 1
        if opp == 3:
            return 2
    if my == 2:
        if opp == 1:
            return 1
        if opp == 2:
            return 2
        if opp == 3:
            return 3
    if my == 3:
        if opp == 1:
            return 2
        if opp == 2:
            return 3
        if opp == 3:
            return 1


def winner_points(num):
    if num == 1:
        return 0
    if num == 2:
        return 3
    if num == 3:
        return 6


# A Rock
# B Paper
# C Scissors

# X Loose
# Y Draw
# Z Win
# assert sonar_sweep(data, window_size=3) == 5


with open("input") as f:
    lines = f.readlines()
opponentdata = []
mydata = []
for e in lines:
    e = e.strip()
    d = e.split(" ")
    if d[0] == "A":
        opponentdata.append(1)
    if d[0] == "B":
        opponentdata.append(2)
    if d[0] == "C":
        opponentdata.append(3)
    if d[1] == "X":
        mydata.append(1)
    if d[1] == "Y":
        mydata.append(2)
    if d[1] == "Z":
        mydata.append(3)


points = 0
for i in range(len(mydata)):
    x = what_to_choose(mydata[i], opponentdata[i])
    points += winner_points(mydata[i])
    points += x

print(points)


# print(opponentdata)
# print(mydata)
