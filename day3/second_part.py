def readfile(filename="input.txt"):
    f = open(filename, "r")
    temp_array = f.read().splitlines()
    return temp_array


def count_in_array_at_string_pos(arr, idx, cmp_val):
    c = 0
    for string in arr:
        c += 1 if string[idx] == cmp_val else -1
    return c


def filter_from_array(arr, cmp_val):
    for counter_idx in range(len(arr[0])):
        counter = count_in_array_at_string_pos(arr, counter_idx, '1')
        arr_new = []
        if counter >= 0:
            for list_element_idx, list_element in enumerate(arr):
                if list_element[counter_idx] == cmp_val:
                    arr_new.append(arr[list_element_idx])
        else:
            for list_element_idx, list_element in enumerate(arr):
                if list_element[counter_idx] != cmp_val:
                    arr_new.append(arr[list_element_idx])
        arr = arr_new
        if len(arr) < 2:
            return arr[0]


array = readfile()
o2 = filter_from_array(array, '1')
co2 = filter_from_array(array, '0')
o2 = int(o2, 2)
co2 = int(co2, 2)
print(o2, co2, o2 * co2)
