import csv


def readfile(filename="input.txt"):
    """ reads csv delimited file using comma as delimiter, returns list (rows) of lists (columns)"""
    f = open(filename, "r")
    r = csv.reader(f, delimiter=',')  # comma-separated
    temp_array = []
    for i in r:
        temp_array.append(list(map(int, i)))  # append row as list of integer
    return temp_array


if __name__ == "__main__":
    array = readfile()[0]
    position_array = range(min(array), max(array) + 1)  # all positions of crab submarines
    fuel_array_lin = []
    fuel_array_fac = []
    for possible_position in position_array:
        fuel_array_lin.append(sum([abs(crab_position - possible_position) for crab_position in array]))
        fuel_array_fac.append(sum([sum(range(abs(crab_position - possible_position) + 1)) for crab_position in array]))
    print('linear', min((val, idx) for idx, val in enumerate(fuel_array_lin)))
    print('factorial', min((val, idx) for idx, val in enumerate(fuel_array_fac)))
