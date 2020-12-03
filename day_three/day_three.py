f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()


def part1(file):
    trees = 0
    x = 3
    for y in range(1, len(lines) - 1):
        line = lines[y] * 100
        if line[x] == '#':
            trees += 1
        x += 3
    return trees


print(part1(lines))
