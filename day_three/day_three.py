import math

f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()


def part1(file):
    trees = 0
    x = 3
    for y in range(1, len(file) - 1):
        line = file[y] * 100
        if line[x] == '#':
            trees += 1
        x += 3
    return trees


def part2(file):
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    trees_list = []
    for slope in slopes:
        trees = 0
        x = slope[0]
        for y in range(slope[1], len(file) - 1, slope[1]):
            line = file[y] * 100
            if line[x] == '#':
                trees += 1
            x += slope[0]
        trees_list.append(trees)
    return math.prod(trees_list)


print(part1(lines))
print(part2(lines))
