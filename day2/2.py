with open("input") as f:

    reports = f.readlines()

    safe_reports = 0
    for i in range(len(reports)):
        levels = reports[i].split()
        levels = [int(level) for level in levels]

        safe = True
        defined_direction = None

        def is_safe(levels):
            defined_direction = None
            for j in range(len(levels) - 1):
                if defined_direction is None:
                    if levels[j+1] - levels[j] > 0:
                        defined_direction = "i"
                    elif levels[j+1] - levels[j] < 0:
                        defined_direction = "d"
                    else:
                        return False

                if defined_direction == "i":
                    if levels[j+1] - levels[j] <= 0 or levels[j+1] - levels[j] > 3:
                        return False
                elif defined_direction == "d":
                    if levels[j+1] - levels[j] >= 0 or levels[j+1] - levels[j] < -3:
                        return False

            return True


        safe = is_safe(levels)

        if not safe:
            for j in range(len(levels)):
                levels_copy = levels.copy()
                levels.pop(j)
                safe = is_safe(levels)
                if safe:
                    break
                levels = levels_copy

        if safe:
            safe_reports += 1

    print(safe_reports)
