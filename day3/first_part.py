def readfile(filename="input.txt"):
    f = open(filename, "r")
    temp_array = f.read().splitlines()
    return temp_array


def count_in_array_at_string_pos(arr, idx, cmp_val):
    c = 0
    for string in arr:
        c += 1 if string[idx] == cmp_val else -1
    return c


array = readfile()
counter_array = [0] * len(array[0])
for idx in range(len(counter_array)):
    counter_array[idx] = count_in_array_at_string_pos(array, idx, '1')
gamma = ''
epsilon = ''
for i in counter_array:
    if i > 0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma, epsilon, gamma * epsilon)
