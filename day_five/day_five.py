f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()


def find_row(instructions):
    min_int = 0
    max_int = 127
    for i in instructions:
        if i == 'F':
            max_int = int((min_int + max_int) / 2)
        elif i == 'B':
            min_int = int((min_int + max_int) / 2) + 1
    if min_int == max_int:
        return max_int


def find_column(instructions):
    min_int = 0
    max_int = 7
    for i in instructions:
        if i == 'L':
            max_int = int((min_int + max_int) / 2)
        elif i == 'R':
            min_int = int((min_int + max_int) / 2) + 1
    if min_int == max_int:
        return max_int


def generate_seat_ids(file):
    seat_ids = []
    for line in file:
        row_instructions = line[:7]
        column_instructions = line[7:]
        row = find_row(row_instructions)
        column = find_column(column_instructions)
        seat_ids.append(row * 8 + column)
    return seat_ids


def part1(file):
    seat_ids = generate_seat_ids(file)
    return max(seat_ids)


def part2(file):
    seat_ids = generate_seat_ids(file)
    seat_ids.sort()
    return [x for x in range(seat_ids[0], seat_ids[-1] + 1)
            if x not in seat_ids]


print(part1(lines))
print(part2(lines))
