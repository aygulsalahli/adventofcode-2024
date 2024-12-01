with open("input") as f:

    left_list = []
    right_list = []
    lines = f.readlines()

    for line in lines:
        left_list.append(int(line.split()[0]))
        right_list.append(int(line.split()[1]))

    left_list.sort()

    map_of_right_list = {}
    for i in range(len(right_list)):
        if right_list[i] in map_of_right_list:
            map_of_right_list[right_list[i]] += 1
        else:
            map_of_right_list[right_list[i]] = 1

    similarity_score = 0
    for i in range(len(left_list)):
        if left_list[i] in map_of_right_list:
            similarity_score += left_list[i] * map_of_right_list[left_list[i]]

    print(similarity_score)

