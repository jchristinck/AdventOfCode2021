import copy


def readfile(filename="input.txt"):
    """ reads file, appends line to list [rows] of lists [elements in row]"""
    with open(filename, "r") as f:
        temp_array = list(f.read().splitlines())  # list of lines containing a string
    cmd_array = []
    polymer_array = [char for char in temp_array[0]]  # first line is polymer
    for row_id in range(len(temp_array)):
        if row_id > 1:
            cmd_array.append(temp_array[row_id].split(' -> '))
            cmd_array[-1] = [char for char in cmd_array[-1][0]] + list(cmd_array[-1][1])  # make cmds to list of 3 chars
    return polymer_array, cmd_array


def explicit_method(steps):
    """ explicit method that saves the polymer as list """
    for step in range(steps):
        print(step)
        insertions = []
        for cmd in cmds:
            for first_letter_appearance, first_letter in \
                    [(i, x) for i, x in enumerate(polymer[:-1]) if (x == cmd[0]) and (polymer[i + 1] == cmd[1])]:
                insertions.append([cmd[2], first_letter_appearance + 1])  # make list of insertions in this step
        insertions.sort(key=lambda x: x[1], reverse=True)
        for insertion in insertions:
            polymer.insert(insertion[1], insertion[0])
    appearances = [sum(map(lambda x: x == char, polymer)) for char in set(polymer)]
    print('explicit method with ', steps, ' steps: ', max(appearances) - min(appearances))


def calc_matrix():
    """ converts polymer to matrix of element after element counters"""
    list_of_elements = set()
    for e in polymer:  # find all possible letters
        list_of_elements.add(e)
    for cmd in cmds:  # find all possible letters
        for e in cmd:
            list_of_elements.add(e)
    list_of_elements = list(list_of_elements)  # convert to list because indexing is needed
    matrix = [[0] * len(list_of_elements) for _ in range(len(list_of_elements))]
    for idx in range(len(polymer) - 1):  # search in polymer
        first_idx = list_of_elements.index(polymer[idx])  # first letter
        second_idx = list_of_elements.index(polymer[idx + 1])  # second letter
        matrix[first_idx][second_idx] += 1  # raise matrix element of first letter - second letter combination by one
    return matrix, list_of_elements


def matrix_method(steps):
    matrix, elements = calc_matrix()  # calculate matrix and list of elements for identification in matrix
    for step in range(steps):
        new_matrix = copy.deepcopy(matrix)
        for cmd in cmds:  # go command-wise
            first_idx = elements.index(cmd[0])  # index in matrix of first letter of command
            second_idx = elements.index(cmd[1])  # index in matrix of second letter of command
            insert_idx = elements.index(cmd[2])  # index in matrix of letter to be inserted
            occ = matrix[first_idx][second_idx]  # number of times the command-combination is in polymer
            new_matrix[first_idx][second_idx] -= occ  # these combinations are deleted
            new_matrix[first_idx][insert_idx] += occ  # new combination raised
            new_matrix[insert_idx][second_idx] += occ  # new combination raised
        matrix = new_matrix
    occ = [sum(i) for i in matrix]  # count number of times letter appears in polymer
    idx = elements.index(polymer[-1])  # last letter of polymer
    occ[idx] += 1  # is raised by one because only elements to second last were counted in matrix
    print('matrix method with ', steps, ' steps: ', max(occ) - min(occ))


if __name__ == "__main__":
    polymer, cmds = readfile()
    # explicit_method(10)  # does not work for part 2
    matrix_method(40)
