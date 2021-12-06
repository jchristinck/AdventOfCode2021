import csv
import copy


def readfile(filename="input.txt"):
    """ reads csv delimited file using comma as delimiter, returns list (rows) of lists (columns)"""
    f = open(filename, "r")
    r = csv.reader(f, delimiter=',')  # comma-separated
    temp_array = []
    for i in r:
        temp_array.append(list(map(int, i)))  # append row as list of integer
    return temp_array[0]


def counting(num_of_days=80):
    """ calculates the number of lanternfish after num_of_days days"""
    lantern_counter = [0] * 9
    for fish in lantern_array:
        lantern_counter[fish] += 1  # array of number of fish per timer value
    for day in range(num_of_days):  # go day-wise
        copy_counter = copy.copy(lantern_counter)  # copy array to modify its values
        for idx in range(8):
            lantern_counter[idx] = copy_counter[idx + 1]  # non-reproducing
        lantern_counter[6] += copy_counter[0]  # reset because of reproducing
        lantern_counter[8] = copy_counter[0]  # offspring
    return sum(lantern_counter)


if __name__ == "__main__":
    lantern_array = readfile()
    print(counting(256))
