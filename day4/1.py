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

            if schema[row][col] != 'X':
                continue

            # Check onward line for XMAS >>
            if col + 3 < columns:
                if schema[row][col + 1] == 'M' and schema[row][col + 2] == 'A' and schema[row][col + 3] == 'S':
                    sum += 1

            #  Check backward line for XMAS <<
            if col - 3 >= 0:
                if schema[row][col - 1] == 'M' and schema[row][col - 2] == 'A' and schema[row][col - 3] == 'S':
                    sum += 1

            # Check downward line for XMAS V
            if row + 3 < rows:
                if schema[row + 1][col] == 'M' and schema[row + 2][col] == 'A' and schema[row + 3][col] == 'S':
                    sum += 1

            # Check upward line for XMAS ^
            if row - 3 >= 0:
                if schema[row - 1][col] == 'M' and schema[row - 2][col] == 'A' and schema[row - 3][col] == 'S':
                    sum += 1

            # Check diagonal line for XMAS \
            if row + 3 < rows and col + 3 < columns:
                if schema[row + 1][col + 1] == 'M' and schema[row + 2][col + 2] == 'A' and schema[row + 3][col + 3] == 'S':
                    sum += 1

            # Check diagonal line for XMAS /
            if row + 3 < rows and col - 3 >= 0:
                if schema[row + 1][col - 1] == 'M' and schema[row + 2][col - 2] == 'A' and schema[row + 3][col - 3] == 'S':
                    sum += 1

            # Check diagonal line for XMAS /
            if row - 3 >= 0 and col + 3 < columns:
                if schema[row - 1][col + 1] == 'M' and schema[row - 2][col + 2] == 'A' and schema[row - 3][col + 3] == 'S':
                    sum += 1

            # Check diagonal line for
            if row - 3 >= 0 and col - 3 >= 0:
                if schema[row - 1][col - 1] == 'M' and schema[row - 2][col - 2] == 'A' and schema[row - 3][col - 3] == 'S':
                    sum += 1

    print(sum)
