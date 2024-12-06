with open("input") as f:

    matrix = []
    obstacles = []
    row = 0
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"
    DIRECTIONS = [UP, DOWN, LEFT, RIGHT]
    position = None

    for line in f:
        chars = line.strip()
        matrix.append(chars)
        for i in range(len(chars)):
            if chars[i] == "#":
                obstacles.append((row, i))
            elif chars[i] in DIRECTIONS:
                position = (row, i)
        row += 1


def get_next_position(pos, direction):
    row, col = pos

    while True:
        if direction == UP:
            next_pos = row - 1, col
            if not is_obstacle(next_pos):
                return next_pos, direction
            else:
                direction = RIGHT
        elif direction == DOWN:
            next_pos = row + 1, col
            if not is_obstacle(next_pos):
                return next_pos, direction
            else:
                direction = LEFT
        elif direction == LEFT:
            next_pos = row, col - 1
            if not is_obstacle(next_pos):
                return next_pos, direction
            else:
                direction = UP
        elif direction == RIGHT:
            next_pos = row, col + 1
            if not is_obstacle(next_pos):
                return next_pos, direction
            else:
                direction = DOWN


def is_at_exit(pos, direction):
    row, col = pos
    if direction == UP:
        return row == 0
    elif direction == DOWN:
        return row == len(matrix) - 1
    elif direction == LEFT:
        return col == 0
    elif direction == RIGHT:
        return col == len(matrix[0]) - 1


def is_obstacle(pos):
    return pos in obstacles


all_visited_positions = set()
current_direction = matrix[position[0]][position[1]]
if current_direction not in DIRECTIONS:
    raise Exception("Invalid direction")

while True:
    all_visited_positions.add(position)
    position, current_direction = get_next_position(position, current_direction)
    if is_at_exit(position, current_direction):
        all_visited_positions.add(position)
        break


print(len(all_visited_positions))
