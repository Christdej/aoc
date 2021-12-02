def parse_line(line):
    command, value = line.split()
    value = int(value)
    if command == "forward":
        return value, 0
    if command == "down":
        return 0, value
    if command == "up":
        return 0, -value


def dive(data):
    depth = 0
    forward = 0
    aim = 0
    for l in data:
        f, d = parse_line(l)
        aim += d
        forward += f
        depth += f * aim
    return depth * forward


data = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

assert dive(data) == 900


with open("input") as f:
    lines = f.readlines()

data = [e for e in lines]

print(dive(data))
