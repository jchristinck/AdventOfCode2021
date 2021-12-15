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


if __name__ == "__main__":
    polymer, cmds = readfile()
    for step in range(10):
        insertions = []
        for cmd in cmds:
            for first_letter_appearance, first_letter in \
                    [(i, x) for i, x in enumerate(polymer[:-1]) if (x == cmd[0]) and (polymer[i + 1] == cmd[1])]:
                insertions.append([cmd[2], first_letter_appearance + 1])
        insertions.sort(key=lambda x: x[1], reverse=True)
        for insertion in insertions:
            polymer.insert(insertion[1], insertion[0])
    appearances = [sum(map(lambda x: x == char, polymer)) for char in set(polymer)]
    print(max(appearances) - min(appearances))
