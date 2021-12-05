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
    for idx in range(int(len(array) / 6)):
        board = f_array[(board_size + 1) * idx + 1:(board_size + 1) * idx + board_size + 1]
        for idy in range(len(board)):
            board[idy] = list(map(int, board[idy][0].split()))
        f_board_array.append(board)
    f_chosen_numbers_array = []
    for i in range(num_boards):
        f_chosen_numbers_array.append([[0 for j in range(board_size)] for k in range(board_size)])
    return f_board_array, f_chosen_numbers_array


def set_new_number(boards, chosen_numbers, number_drawn):
    for idx in range(len(boards)):
        for idy in range(len(boards[0])):
            for idz in range(len(boards[0][0])):
                if boards[idx][idy][idz] == number_drawn:
                    chosen_numbers[idx][idy][idz] = 1
    return chosen_numbers


def mark_finished_boards(boards, winner_boards, board_size=5):
    for idx in range(len(boards)):
        col_chosen = [0 for i in range(board_size)]
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


def calc_sum_of_unmarked(array, chosen_numbers):
    sum = 0
    for i in range(len(array)):
        for j in range(len(array[0])):
            sum += (1 - chosen_numbers[i][j]) * array[i][j]
    return sum


def check_for_last_board(winner_boards):
    if max(winner_boards) == len(winner_boards):
        for idx in range(len(winner_boards)):
            if winner_boards[idx] == len(winner_boards):
                return idx, True
    return -1, False


array = readfile()
numbers_drawn = list(map(int, array.pop(0)))
board_array, chosen_numbers_array = prepare_arrays(array)
winner_board_array = [0] * len(board_array)
one_board_left = False
while not one_board_left:
    if not numbers_drawn:
        print('failed to determine winner, no numbers left to draw')
        quit()
    last_number = numbers_drawn.pop(0)
    chosen_numbers_array = set_new_number(board_array, chosen_numbers_array, last_number)
    winner_board_array = mark_finished_boards(chosen_numbers_array, winner_board_array)
    winner_board, one_board_left = check_for_last_board(winner_board_array)
    print(winner_board_array)
sum_of_unmarked = calc_sum_of_unmarked(board_array[winner_board], chosen_numbers_array[winner_board])
print(last_number, sum_of_unmarked, last_number * sum_of_unmarked)
