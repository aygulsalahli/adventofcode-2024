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


def get_next_position(pos, direction, artificial_obstacle_position = None):
    row, col = pos

    while True:
        if direction == UP:
            next_pos = row - 1, col
            if not is_obstacle(next_pos, artificial_obstacle_position):
                return next_pos, direction
            else:
                direction = RIGHT
        elif direction == DOWN:
            next_pos = row + 1, col
            if not is_obstacle(next_pos, artificial_obstacle_position):
                return next_pos, direction
            else:
                direction = LEFT
        elif direction == LEFT:
            next_pos = row, col - 1
            if not is_obstacle(next_pos, artificial_obstacle_position):
                return next_pos, direction
            else:
                direction = UP
        elif direction == RIGHT:
            next_pos = row, col + 1
            if not is_obstacle(next_pos, artificial_obstacle_position):
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


def is_obstacle(pos, artificial_obstacle_position = None):
    return pos in obstacles or pos == artificial_obstacle_position

all_visited_positions = set()
start_position = position
current_direction = matrix[position[0]][position[1]]
if current_direction not in DIRECTIONS:
    raise Exception("Invalid direction")

while True:
    all_visited_positions.add(position)
    position, current_direction = get_next_position(position, current_direction, None)
    if is_at_exit(position, current_direction):
        all_visited_positions.add(position)
        break


# Put an obstacle on guards' path and see if they're in the loop
# one obstacle at most at a time
#  if it makes a loop, count the number of all the different positions for an obstacle
def is_loop(obstacle_position):
    current_direction = matrix[start_position[0]][start_position[1]]
    position = start_position
    # includes the position and the direction at the position
    current_trajectory = set()
    current_direction = matrix[position[0]][position[1]]
    while True:
        current_trajectory.add((position[0], position[1], current_direction))
        position, current_direction = get_next_position(position, current_direction, obstacle_position)
        if is_at_exit(position, current_direction):
            break
        if (position[0], position[1], current_direction) in current_trajectory:
            return True
    return False

all_loop_positions = set()
for visited_position in all_visited_positions:
    if visited_position == start_position:
        continue

    artificial_obstacle_position = visited_position
    if is_loop(artificial_obstacle_position):
        all_loop_positions.add(visited_position)

print(len(all_loop_positions))



# WARNING: This is a brute force solution and it's not efficient :grimacing:
# Do not try this at home!
