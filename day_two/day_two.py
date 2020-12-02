f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()


def part1(file):
    valid = 0
    for line in file:
        x = line.split(': ')
        policy = x[0]
        password = x[1]
        y = policy.split(' ')
        letter = y[1]
        z = y[0].split('-')
        least = int(z[0])
        most = int(z[1])
        if least <= password.count(letter) <= most:
            valid += 1

    return valid


def part2(file):
    valid = 0
    for line in file:
        x = line.split(': ')
        policy = x[0]
        password = x[1]
        y = policy.split(' ')
        letter = y[1]
        z = y[0].split('-')
        pos1 = int(z[0]) - 1
        pos2 = int(z[1]) - 1
        if (password[pos1] == letter and password[pos2] != letter)\
                or (password[pos1] != letter and password[pos2] == letter):
            valid += 1

    return valid


print(part1(lines))
print(part2(lines))
