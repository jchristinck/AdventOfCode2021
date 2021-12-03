import csv
import timeit as t


def whack_counting():
    f = open("input.txt", "r")
    r = csv.reader(f)
    array = [int(r.__next__()[0])]
    i = 0
    for row in r:
        array.append(int(row[0]))
        if array[-1] > array[-2]:
            i += 1
    print(i)


def efficient_counting():
    f = open("input.txt", "r")
    r = csv.reader(f)
    cmp_val = int(r.__next__()[0])
    i = 0
    for row in r:
        new_val = int(row[0])
        if new_val > cmp_val:
            i += 1
        cmp_val = new_val
    print(i)


t1 = t.default_timer()
whack_counting()
t2 = t.default_timer()
efficient_counting()
t3 = t.default_timer()
print(t2 - t1)
print(t3 - t2)
print(t3 - t1)
