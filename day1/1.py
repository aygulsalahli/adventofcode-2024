with open("input") as f:

    left_list = []
    right_list = []
    lines = f.readlines()

    for line in lines:
        left_list.append(int(line.split()[0]))
        right_list.append(int(line.split()[1]))

    left_list.sort()
    right_list.sort()

    sum_of_distances = 0

    for i in range(len(left_list)):
        sum_of_distances += abs(left_list[i] - right_list[i])

    print(sum_of_distances)

