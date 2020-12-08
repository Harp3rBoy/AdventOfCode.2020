import re

f = open("input.txt", "r")
lines = f.read().split("\n")[:-1]
passports = []
passport = ''
for line in lines:
    if line != '':
        passport += ' ' + line
    else:
        passports += [passport[1:]]
        passport = ''

f.close()

fields = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: (x.endswith("cm") and 150 <= int(x[:-2]) <= 193) or
                     (x.endswith("in") and 59 <= int(x[:-2]) <= 76),
    "hcl": lambda x: re.match("^#([0-9a-f]){6}$", x),
    "ecl": lambda x: x in ['amb', "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: re.match("^[0-9]{9}$", x),
}


def field_checker(entry):
    for field in fields:
        if field not in entry:
            return False
    return True


def part1(file):
    valid = 0
    for entry in file:
        if field_checker(entry):
            valid += 1
    return valid


def part2(file):
    valid = 0
    for entry in file:
        if field_checker(entry):
            p = dict(x.split(":") for x in entry.split())
            valid += all(data(p[field]) for field, data in fields.items())
    return valid


print(part1(passports))
print(part2(passports))
