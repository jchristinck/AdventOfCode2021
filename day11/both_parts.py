import copy


def readfile(filename="input.txt"):
    """ reads file, appends line to list [rows] of lists [elements in row]"""
    with open(filename, "r") as f:
        temp_array = list(f.read().splitlines())  # list of lines containing a string
    for row_id in range(len(temp_array)):
        temp_array[row_id] = [int(i) for i in temp_array[row_id]]
    return temp_array


def raise_neighbours(idyn, idxn):
    """ check all available neighbours in array and adds one to them, checks if they blink
    and then recursively call this function at their the blinking neighbour's position """
    ly = len(array)
    lx = len(array[0])
    if (idyn > 0) and (idxn > 0) and (blink_array[idyn - 1][idxn - 1] >= 0):  # neighbour top left
        array[idyn - 1][idxn - 1] += 1
        if array[idyn - 1][idxn - 1] > 9:
            blink_array[idyn - 1][idxn - 1] = -1
            raise_neighbours(idyn - 1, idxn - 1)
    if (idyn > 0) and (blink_array[idyn - 1][idxn] >= 0):  # neighbour top
        array[idyn - 1][idxn] += 1
        if array[idyn - 1][idxn] > 9:
            blink_array[idyn - 1][idxn] = -1
            raise_neighbours(idyn - 1, idxn)
    if (idyn > 0) and (idxn < lx - 1) and (blink_array[idyn - 1][idxn + 1] >= 0):  # neighbour top right
        array[idyn - 1][idxn + 1] += 1
        if array[idyn - 1][idxn + 1] > 9:
            blink_array[idyn - 1][idxn + 1] = -1
            raise_neighbours(idyn - 1, idxn + 1)
    if (idxn > 0) and (blink_array[idyn][idxn - 1] >= 0):  # neighbour left
        array[idyn][idxn - 1] += 1
        if array[idyn][idxn - 1] > 9:
            blink_array[idyn][idxn - 1] = -1
            raise_neighbours(idyn, idxn - 1)
    if (idxn < lx - 1) and (blink_array[idyn][idxn + 1] >= 0):  # neighbour right
        array[idyn][idxn + 1] += 1
        if array[idyn][idxn + 1] > 9:
            blink_array[idyn][idxn + 1] = -1
            raise_neighbours(idyn, idxn + 1)
    if (idyn < ly - 1) and (idxn > 0) and (blink_array[idyn + 1][idxn - 1] >= 0):  # neighbour bottom left
        array[idyn + 1][idxn - 1] += 1
        if array[idyn + 1][idxn - 1] > 9:
            blink_array[idyn + 1][idxn - 1] = -1
            raise_neighbours(idyn + 1, idxn - 1)
    if (idyn < ly - 1) and (blink_array[idyn + 1][idxn] >= 0):  # neighbour right
        array[idyn + 1][idxn] += 1
        if array[idyn + 1][idxn] > 9:
            blink_array[idyn + 1][idxn] = -1
            raise_neighbours(idyn + 1, idxn)
    if (idyn < ly - 1) and (idxn < lx - 1) and (blink_array[idyn + 1][idxn + 1] >= 0):  # neighbour left
        array[idyn + 1][idxn + 1] += 1
        if array[idyn + 1][idxn + 1] > 9:
            blink_array[idyn + 1][idxn + 1] = -1
            raise_neighbours(idyn + 1, idxn + 1)


if __name__ == "__main__":

    BLINKS_AFTER_STEP = 100  # decide after what amount of steps the total blinks shall be counted
    ABORT_WHEN_SYNC = True  # decide whether program shall abort after first synced step

    array = readfile()
    num_blinks = 0
    first_sync = 'no sync yet'
    for step in range(100000):
        num_blinks_step = 0
        blink_array = copy.deepcopy(array)
        for idy, row in enumerate(array):  # go row-wise
            for idx, col in enumerate(row):  # go col-wise
                if blink_array[idy][idx] >= 0:  # not blinked yet?
                    array[idy][idx] += 1
                    if array[idy][idx] > 9:  # shall it blink?
                        blink_array[idy][idx] = -1  # set as blinked
                        raise_neighbours(idy, idx)
        for idy, row in enumerate(array):  # go row-wise
            for idx, col in enumerate(row):  # go col-wise
                if blink_array[idy][idx] == -1:  # blinked this step?
                    array[idy][idx] = 0  # reset to zero
                    num_blinks_step += 1  # blinks of this step raised
                    if step < BLINKS_AFTER_STEP:  # blinks still counted in this step?
                        num_blinks += 1  # total blinks raised
        if num_blinks_step == len(array) * len(array[0]):  # all blinked ?
            first_sync = step + 1  # set first synchronized step
            if ABORT_WHEN_SYNC:
                break
    print('total number of blinks after', BLINKS_AFTER_STEP, 'steps:', num_blinks)
    print('first synchronized step:', first_sync)
