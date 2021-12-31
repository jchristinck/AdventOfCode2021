import timeit as t
import pygame


def readfile(filename="input.txt"):
    """ reads file, appends line to list [rows] of lists [elements in row]"""
    with open(filename, "r") as f:
        temp_array = list(f.read().splitlines())  # list of lines containing a string
    for row_id in range(len(temp_array)):
        temp_array[row_id] = [int(i) for i in temp_array[row_id]]
    return temp_array


def calc_maze_el(maze_val, repeat_val):
    """ calculates new value of maze element by subtracting 9 from old value until new value is between 0 and 9 """
    while maze_val + repeat_val > 9:
        maze_val -= 9
    return maze_val + repeat_val


def generate_large_maze(f_maze, multiplier):
    """ copies maze five times in each dimension to generate the maze for part 2 """
    large_maze = [[0 for _ in range(multiplier * len(f_maze))] for _ in range(multiplier * len(maze[0]))]
    for i in range(multiplier):  # copy multiplier times in y
        for j in range(multiplier):  # copy multiplier times in x
            for row_id, row in enumerate(f_maze):  # rows in maze
                for col_id, val in enumerate(row):  # cols in maze
                    large_maze[i * len(f_maze) + row_id][j * len(f_maze[0]) + col_id] = calc_maze_el(val, i + j)
    return large_maze


def solve_maze(display):
    """ solves maze using a* algorithm """
    queue = [(0, 0, 0)]  # queue for elements to look at
    went = [[0] * len(maze[0]) for _ in range(len(maze))]  # matrix that signals if element is already visited
    pixel_array = pygame.PixelArray(ui_screen)
    pixel_array[:][:] = (0, 0, 0)
    last_weight = 0
    while queue:
        current_node = queue.pop(queue.index(min(queue)))  # set lowest value element in queue as current node
        if not went[current_node[1]][current_node[2]]:
            went[current_node[1]][current_node[2]] = 1  # mark element as visited
            new_val = 0.08 * current_node[0]
            pixel_array[current_node[1]][current_node[2]] = (new_val, new_val, new_val)
        if current_node[0] > last_weight and display:
            last_weight = current_node[0]
            pygame.display.flip()
        children = []
        if (current_node[1] == len(maze) - 1) and (current_node[2] == len(maze[0]) - 1):  # at finish?
            break
        if current_node[1] > 0:  # left neighbour exists?
            children.append((maze[current_node[1] - 1][current_node[2]], current_node[1] - 1, current_node[2]))
        if current_node[2] > 0:  # top neighbour exists?
            children.append((maze[current_node[1]][current_node[2] - 1], current_node[1], current_node[2] - 1))
        if current_node[1] < len(maze) - 1:  # right neighbour exists?
            children.append((maze[current_node[1] + 1][current_node[2]], current_node[1] + 1, current_node[2]))
        if current_node[2] < len(maze[0]) - 1:  # bottom neighbour exists?
            children.append((maze[current_node[1]][current_node[2] + 1], current_node[1], current_node[2] + 1))
        for child in children:
            if went[child[1]][child[2]]:  # element is already visited?
                continue
            f = current_node[0] + child[0]  # calculate weight of element
            if queue:  # prevent error if queue is empty
                if (f > min(queue)[0]) and ([x[0] for x in queue if (x[1] == child[1]) and (x[2] == child[2])]):
                    # weight must be lower than any value for this element in queue
                    continue
            queue.append((f, child[1], child[2]))  # add element to queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                queue = []
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    queue = []
    t2 = t.default_timer()
    print('size of maze:', len(maze), 'x', len(maze[0]))
    print('result:', current_node[0])
    print('time to run:', t2 - t1, 's')


if __name__ == "__main__":
    mazeMultiplier = 5
    pygame.init()
    ui_screen = pygame.display.set_mode((100 * mazeMultiplier, 100 * mazeMultiplier))

    t1 = t.default_timer()
    maze = readfile()  # read input.txt
    solve_maze(False)  # solve first part
    maze = generate_large_maze(maze, mazeMultiplier)  # prepare maze for second part
    solve_maze(True)  # solve second part

    pygame.quit()
