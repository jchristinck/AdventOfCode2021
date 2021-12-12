def readfile(filename="input.txt"):
    """ reads file, appends line to list [rows] of lists [elements in row]"""
    with open(filename, "r") as f:
        temp_array = list(f.read().splitlines())  # list of lines containing a string
    for row_id in range(len(temp_array)):
        temp_array[row_id] = temp_array[row_id].split('-')
    return temp_array


def calc_caves():
    """ calculates list of cave positions and list of lists of connections, where 1 is possible and 0 is not """
    f_caves = []
    for f_connection in array:
        for point in f_connection:
            if point not in f_caves:
                f_caves.append(point)
    f_connections = [[0] * len(f_caves) for _ in range(len(f_caves))]
    for f_connection in array:
        idx = f_caves.index(f_connection[0])
        idy = f_caves.index(f_connection[1])
        f_connections[idx][idy] = 1
        f_connections[idy][idx] = 1
    return f_caves, f_connections


def is_path_gone(new_path):
    """ checks if path is already in path_list"""
    abbreviated_path_list = []
    for f_path in path_list:
        abbreviated_path_list.append(f_path[:len(new_path) + 1])
    return new_path in path_list


if __name__ == "__main__":
    array = readfile()
    caves, connections = calc_caves()
    path_list = []
    while True:
        this_path = ['start']
        path_list_length = len(path_list)
        small_once = False
        critical_point = False
        while True:
            length = len(this_path)
            for new_pos, connection in enumerate(connections[caves.index(this_path[-1])]):
                if connection:
                    if (caves[new_pos].isupper() or not (caves[new_pos] in this_path)) and caves[new_pos] != 'start':
                        path_gone = is_path_gone(this_path + [caves[new_pos]])
                        if not path_gone:
                            this_path.append(caves[new_pos])
                            break
            if (length == len(this_path)) or (this_path[-1] == 'end'):
                break
        is_new_path = this_path not in path_list
        if is_new_path:
            path_list.append(this_path)
        else:
            break
    valid_path_list = []
    for path in path_list:
        if path[-1] == 'end':
            valid_path_list.append(path)
    print(len(valid_path_list))
