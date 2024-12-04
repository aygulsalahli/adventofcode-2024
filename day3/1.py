import re

with open("input") as f:
    # Regular expression pattern
    pattern = r'mul\((\d{1,3}),\s*(\d{1,3})\)'
    reports = f.read()
    # Find all matches
    matches = re.findall(pattern, reports)

    sum = 0
    for match in matches:
        sum += int(match[0]) * int(match[1])

    print(sum)

