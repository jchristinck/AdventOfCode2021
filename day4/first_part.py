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


def check_for_winner(boards, board_size=5):
    for idx in range(len(boards)):
        for idy in range(board_size):
            row_chosen = 0
            col_chosen = [0 for i in range(board_size)]
            for idz in range(len(boards[0][0])):
                if boards[idx][idy][idz] == 1:
                    col_chosen[idy] += 1
                    row_chosen += 1
            if row_chosen == board_size:
                return idx
        for idy in range(board_size):
            if col_chosen[idy] == board_size:
                return idx
    return -1


def calc_sum_of_unmarked(array, chosen_numbers):
    sum = 0
    for i in range(len(array)):
        for j in range(len(array[0])):
            sum += (1 - chosen_numbers[i][j]) * array[i][j]
    return sum


array = readfile()
numbers_drawn = list(map(int, array.pop(0)))
board_array, chosen_numbers_array = prepare_arrays(array)
winner_board = -1
while winner_board == -1:
    if not numbers_drawn:
        print('failed to determine winner, no numbers left to draw')
        break
    last_number = numbers_drawn.pop(0)
    chosen_numbers_array = set_new_number(board_array, chosen_numbers_array, last_number)
    winner_board = check_for_winner(chosen_numbers_array)
sum_of_unmarked = calc_sum_of_unmarked(board_array[winner_board], chosen_numbers_array[winner_board])
print(last_number, sum_of_unmarked, last_number * sum_of_unmarked)
