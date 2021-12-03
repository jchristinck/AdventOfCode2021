import csv
import timeit as t


def prepare_array():
    f = open("input.txt", "r")
    r = csv.reader(f)
    array = []
    for row in r:
        array.append(int(row[0]))
    group_array = []
    for idx in range(len(array) - 2):
        group_array.append(sum(array[idx:idx + 3]))
    return group_array


def efficient_counting(array):
    cmp_val = array[0]
    i = 0
    for new_val in array:
        if new_val > cmp_val:
            i += 1
        cmp_val = new_val
    print(i)


t1 = t.default_timer()
temp_array = prepare_array()
t2 = t.default_timer()
efficient_counting(temp_array)
t3 = t.default_timer()
print(t2 - t1)
print(t3 - t2)
print(t3 - t1)
