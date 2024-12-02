import os
print(os.getcwd())



with open("input") as f:

    reports = f.readlines()

    safe_reports = 0
    for i in range(len(reports)):
        levels = reports[i].split()
        levels = [int(level) for level in levels]

        safe = True
        defined_direction = None
        for j in range(len(levels) - 1):
            if defined_direction is None:
                if levels[j+1] - levels[j] > 0:
                    defined_direction = "i"
                elif levels[j+1] - levels[j] < 0:
                    defined_direction = "d"
                else:
                    safe = False
                    break

            if defined_direction == "i":
                if levels[j+1] - levels[j] <= 0 or levels[j+1] - levels[j] > 3:
                    safe = False
                    break
            elif defined_direction == "d":
                if levels[j+1] - levels[j] >= 0 or levels[j+1] - levels[j] < -3:
                    safe = False
                    break

        if safe:
            safe_reports += 1

    print(safe_reports)
