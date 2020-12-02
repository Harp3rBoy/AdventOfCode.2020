f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()


def part1(file):
    for i in file:
        i = int(i)
        for j in file:
            j = int(j)
            if i + j == 2020:
                return i * j


def part2(file):
    for i in file:
        i = int(i)
        for j in file:
            j = int(j)
            for k in file:
                k = int(k)
                if i + j + k == 2020:
                    return i * j * k


print(part1(lines))
print(part2(lines))
