def readfile(filename="input.txt"):
    """ reads file and replaces ' -> ' with ',' in each line, than appends line to list of lists"""
    with open(filename, "r") as f:
        temp_array = f.read().splitlines()  # list of lines containing a string
    for idx in range(len(temp_array)):
        temp_array[idx] = list(map(int, temp_array[idx].replace(' -> ', ',').split(',')))  # list of [x1, y1, x2, y2]'s
    return temp_array


def calc_indices_between_points(f_line):
    """ returns list of 3-tuple of indices of the line """
    f_indices_list = []
    direction_x = 1 if f_line[3] > f_line[1] else (0 if f_line[3] == f_line[1] else -1)
    direction_y = 1 if f_line[2] > f_line[0] else (0 if f_line[2] == f_line[0] else -1)
    idx = f_line[0]
    idy = f_line[1]
    while (idx != f_line[2]) or (idy != f_line[3]):
        f_indices_list.append([idx, idy])
        idy += direction_x
        idx += direction_y
    else:
        f_indices_list.append([f_line[2], f_line[3]])
    return f_indices_list


if __name__ == "__main__":
    # list_of_lines = readfile("test_input.txt")
    list_of_lines = readfile()  # list, each containing a line x1, y1, x2, y2 as a list
    size_needed = max(list(map(max, *list_of_lines))) + 1  # determine size of diagram
    array_of_points = [[0 for _ in range(size_needed)] for _ in range(size_needed)]  # zeros everywhere

    for line in list_of_lines:  # go line-wise
        indices_list = calc_indices_between_points(line)  # get list of points of line
        for x, y in indices_list:  # go point-wise
            array_of_points[y][x] += 1  # increase number of point

    number_of_danger_points = 0
    for y in range(len(array_of_points)):  # go row-wise
        for x in range(len(array_of_points[y])):  # go column-wise
            if array_of_points[y][x] > 1:  # is danger point?
                number_of_danger_points += 1
    print(number_of_danger_points)
