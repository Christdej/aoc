import re
from functools import lru_cache

data = []
for line in open("input_ex"):
    row, group = line.strip().split()
    # row = [1 if e == "#" else 0 for e in row]
    group = [int(number) for number in re.findall(r"\d+", group)]
    data.append((row, group))
print(data)


def find_arrangement(row, group):
    return


print("PART 2: ", sum(find_arrangement(row, group) for row, group))

# @lru_cache(maxsize=400)
# def matches2(record, damages):
#     def more_damaged_springs():
#         return len(damages) > 1

#     def found_damaged_springs():
#         return re.findall(r"^[\#\?]{%i}" % next_grp, record)

#     def valid_next_spring():
#         return not ((len(record) < next_grp + 1) or record[next_grp] == "#")

#     if not damages:
#         return 0 if "#" in record else 1

#     if not record:
#         return 0

#     result = 0
#     next_ch = record[0]
#     next_grp = damages[0]

#     if next_ch == "#":
#         if found_damaged_springs():
#             if more_damaged_springs():
#                 if valid_next_spring():
#                     result += matches2(record[next_grp + 1 :], damages[1:])
#                 else:
#                     return 0
#             else:
#                 result += matches2(record[next_grp:], damages[1:])

#     elif next_ch == ".":
#         result += matches2(record[1:], damages)

#     elif next_ch == "?":
#         result += matches2(record.replace("?", "#", 1), damages) + matches2(
#             record.replace("?", ".", 1), damages
#         )

#     return result


# def unfold(input):
#     return (("?".join([record] * 5), damages * 5) for record, damages in input)


# def part1(input):
#     # part 1 slow method
#     #  return sum(matches1(record, damages) for record, damages in input)

#     return sum(matches2(record, damages) for record, damages in input)


# def part2(input):
#     return part1(unfold(input))
