# image = []
# for line in open("input"):
#     image.append(line.strip())
#     if "#" not in line:
#         image.append("." * len(image[0]))
# i = 0
# while i < len(image[0]):
#     if "#" not in [line[i] for line in image]:
#         for j in range(len(image)):
#             image[j] = image[j][:i] + "." + image[j][i:]
#         i += 1
#     i += 1
# galaxies = [
#     (x, y)
#     for x in range(len(image[0]))
#     for y in range(len(image))
#     if image[y][x] == "#"
# ]
# print(galaxies)
# lengths = 0
# for i, galaxy1 in enumerate(galaxies):
#     for galaxy2 in galaxies[i + 1 :]:
#         lengths += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
# print(lengths)

image = [
    [(x, y) if c == "#" else None for x, c in enumerate(line.strip())]
    for y, line in enumerate(open("input"))
]
empty_lines = 0
for y, line in enumerate(image):
    if len(set(line)) > 1:
        image[y] = [
            (n[0], n[1] + empty_lines * 999999) if n is not None else None for n in line
        ]
    else:
        empty_lines += 1
empty_lines = 0
for x in range(len(image[0])):
    line = [image[y][x] for y in range(len(image))]
    if len(set(line)) > 1:
        for y in range(len(image)):
            image[y][x] = (
                (image[y][x][0] + empty_lines * 999999, image[y][x][1])
                if image[y][x] is not None
                else None
            )
    else:
        empty_lines += 1
galaxies = [g for line in image for g in line if g is not None]
lengths = 0
for i, galaxy1 in enumerate(galaxies):
    for galaxy2 in galaxies[i + 1 :]:
        lengths += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
print(lengths)
