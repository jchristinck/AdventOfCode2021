def readfile(filename="input.txt"):
    """ reads file and replaces ' | ' with ' ' in each line, than appends line to list of lists"""
    with open(filename, "r") as f:
        temp_array = f.read().splitlines()  # list of lines containing a string
    for idx in range(len(temp_array)):
        temp_array[idx] = temp_array[idx].replace(' | ', ' ').split(' ')
    return temp_array


def unique_counting():
    unique_count = 0
    for row in array:
        for idx in range(len(row[10:])):
            entry = row[10 + idx]
            if len(entry) == 2:
                unique_count += 1
            elif len(entry) == 3:
                unique_count += 1
            elif len(entry) == 4:
                unique_count += 1
            elif len(entry) == 7:
                unique_count += 1
    print(unique_count)


if __name__ == "__main__":
    array = readfile("test_input.txt")
    # array = readfile()
    unique_counting()
    print(array)
