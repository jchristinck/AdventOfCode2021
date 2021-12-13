def readfile(filename="input.txt"):
    """ reads file, appends line to list [rows] of lists [elements in row]"""
    with open(filename, "r") as f:
        temp_array = list(f.read().splitlines())  # list of lines containing a string
    for row_id in range(len(temp_array)):
        if not temp_array[row_id]:
            cmds_array = [[j[0][-1], int(j[1])] for j in [i.split('=') for i in temp_array[row_id + 1:]]]
            temp_array = temp_array[:row_id]
            break
        temp_array[row_id] = list(map(int, temp_array[row_id].split(',')))
    return cmds_array, temp_array


if __name__ == "__main__":
    cmds, array = readfile()
    for idx, cmd in enumerate(cmds):  # go though folding commands
        if cmd[0] == 'x':
            for dot in array:
                if dot[0] > cmd[1]:
                    dot[0] = 2 * cmd[1] - dot[0]  # mirror dots at x-folding line
        else:
            for dot in array:
                if dot[1] > cmd[1]:
                    dot[1] = 2 * cmd[1] - dot[1]  # mirror dots at y-folding line
        if not idx:
            print(len(set([tuple(k) for k in array])))  # part 1 solution
    sizes = [max(array, key=lambda x: x[0])[0], max(array, key=lambda x: x[1])[1]]  # x-y-size of show array
    show_array = [['.'] * (sizes[0] + 1) for _ in range(sizes[1] + 1)]
    for dot in array:
        show_array[dot[1]][dot[0]] = 'x'
    for row in show_array:
        print(''.join(row))
