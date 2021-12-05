import csv


def readfile(filename="input.txt"):
    f = open(filename, "r")
    r = csv.reader(f, delimiter=',')
    temp_array = []
    for i in r:
        temp_array.append(i)
    return temp_array


def prepare_arrays(f_array, board_size=5, num_boards=100):
    f_board_array = []
    for idx in range(int(len(f_array) / (board_size + 1))):
        board = f_array[(board_size + 1) * idx + 1:(board_size + 1) * idx + board_size + 1]
        for idy in range(len(board)):
            board[idy] = list(map(int, board[idy][0].split()))
        f_board_array.append(board)
    f_chosen_numbers_array = []
    for i in range(num_boards):
        f_chosen_numbers_array.append([[0 for _ in range(board_size)] for _ in range(board_size)])
    return f_board_array, f_chosen_numbers_array


def set_new_number(boards, chosen_numbers, number_drawn):
    indices = [(idx, idy, idz)
               for idx, board in enumerate(boards)
               for idy, row in enumerate(board)
               for idz, col in enumerate(row)
               if boards[idx][idy][idz] == number_drawn]
    for idx, idy, idz in indices:
        chosen_numbers[idx][idy][idz] = 1
    return chosen_numbers


def mark_finished_boards(boards, winner_boards, board_size=5):
    for idx in range(len(boards)):
        col_chosen = [0 for _ in range(board_size)]
        for idy in range(board_size):
            row_chosen = 0
            for idz in range(len(boards[0][0])):
                if boards[idx][idy][idz] == 1:
                    col_chosen[idz] += 1
                    row_chosen += 1
            if (row_chosen == board_size) and (winner_boards[idx] == 0):
                winner_boards[idx] = max(winner_boards) + 1
        for idy in range(board_size):
            if (col_chosen[idy] == board_size) and (winner_boards[idx] == 0):
                winner_boards[idx] = max(winner_boards) + 1
    return winner_boards


def calc_winning_board_value(number_searched=1):
    array = readfile()
    numbers_drawn = list(map(int, array.pop(0)))
    board_array, chosen_numbers_array = prepare_arrays(array)
    winner_board_array = [0] * len(board_array)
    one_board_left = False
    while not one_board_left:
        last_number = numbers_drawn.pop(0)
        if not numbers_drawn:
            print('failed to determine winner number', number_searched, ', no numbers left to draw')
            quit()
        chosen_numbers_array = set_new_number(board_array, chosen_numbers_array, last_number)
        winner_board_array = mark_finished_boards(chosen_numbers_array, winner_board_array)
        if max(winner_board_array) == number_searched:
            winner_board = winner_board_array.index(max(winner_board_array))
            sum_of_unmarked = sum([a * (1 - b)
                                   for x, y in zip(board_array[winner_board], chosen_numbers_array[winner_board])
                                   for a, b in zip(x, y)])
            print(number_searched, last_number, sum_of_unmarked, last_number * sum_of_unmarked)
            break


if __name__ == "__main__":
    calc_winning_board_value(1)
    calc_winning_board_value(100)
