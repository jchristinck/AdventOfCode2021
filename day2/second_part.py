import csv


def readfile(filename="input.txt"):
    f = open(filename, "r")
    r = csv.reader(f)
    temp_array = []
    for row in r:
        temp_array.append(row[0])
    return temp_array


array = readfile()

depth = 0
horizontal = 0
aim = 0
for string in array:
    [cmd, num] = string.split()
    if cmd == "up":
        aim -= int(num)
    elif cmd == "down":
        aim += int(num)
    elif cmd == "forward":
        horizontal += int(num)
        depth += aim * int(num)
    else:
        print("no command found")

print(depth)
print(horizontal)
print(depth * horizontal)
