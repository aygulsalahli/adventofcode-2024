import re

with open("input") as f:

    pattern = r'mul\((\d{1,3}),\s*(\d{1,3})\)'
    # Split the file with 'do's
    f = f.read().split('do')

    sum = 0
    for i in range(len(f)):
        # Skip pieces that start with "n't", remember don't disables until the next do
        if f[i].startswith("n't"):
            continue

        matches = re.findall(pattern, f[i])
        for match in matches:
            sum += int(match[0]) * int(match[1])


    print(sum)

