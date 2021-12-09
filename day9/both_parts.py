def readfile(filename="input.txt"):
    """ reads file and replaces ' | ' with ' ' in each line, than appends line to list of lists"""
    with open(filename, "r") as f:
        temp_array = f.read().splitlines()  # list of lines containing a string
    for idx in range(len(temp_array)):
        temp_array[idx] = [i for i in temp_array[idx]]
    return temp_array


if __name__ == "__main__":
    # array = readfile("test_input.txt")
    array = readfile()
    rows = len(array)
    cols = len(array[0])
    winner_array = []
    for idx, row in enumerate(array):
        for idy, col in enumerate(row):
            left_n = False
            right_n = False
            upper_n = False
            lower_n = False
            if idy > 0:
                if array[idx][idy] < array[idx][idy - 1]:
                    left_n = True
            else:
                left_n = True
            if idy < cols - 1:
                if array[idx][idy] < array[idx][idy + 1]:
                    right_n = True
            else:
                right_n = True
            if idx > 0:
                if array[idx][idy] < array[idx - 1][idy]:
                    upper_n = True
            else:
                upper_n = True
            if idx < rows - 1:
                if array[idx][idy] < array[idx + 1][idy]:
                    lower_n = True
            else:
                lower_n = True
            if left_n and right_n and upper_n and lower_n:
                winner_array.append((idx, idy))
    # print(winner_array)
    sum_lowpoints = 0
    for i in range(len(winner_array)):
        sum_lowpoints += int(array[winner_array[i][0]][winner_array[i][1]]) + 1
    print(sum_lowpoints)
