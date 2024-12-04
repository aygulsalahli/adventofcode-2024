def makes_an_MS(p1, p2):
    if p1 == "M" and p2 == "S":
        return True
    if p1 == "S" and p2 == "M":
        return True

    return False

with open("input") as f:
    schema = []
    lines = f.readlines()
    sum = 0
    for index, line in enumerate(lines):
        line = line.rstrip()
        schema.append([x for x in line])

    rows = len(schema)
    columns = len(schema[0])

    for row in range(rows):
        for col in range(columns):

            if schema[row][col] != 'A':
                continue

            if row - 1 >= 0 and col + 1 < columns and row + 1 < rows and col - 1 >= 0:
                if makes_an_MS(schema[row-1][col-1], schema[row+1][col+1]) and makes_an_MS(schema[row+1][col-1], schema[row-1][col+1]):
                        sum += 1

    print(sum)
