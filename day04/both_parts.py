import csv


def readfile(filename="input.txt"):
    """ reads csv delimited file using comma as delimiter, returns list (rows) of lists (columns)"""
    f = open(filename, "r")
    r = csv.reader(f, delimiter=',')
    temp_array = []
    for i in r:
        temp_array.append(i)
    return temp_array


def prepare_arrays(f_array, board_size=5):
    """ returns two lists of lists of lists of size num_boards * board_size (rows) * boards_size (columns)
        num_boards implicit from data input f_array
        f_board_array contains contents of array
        f_marked_boards_array contains zeros """
    f_board_array = []  # set up boards_array
    for idx in range(int(len(f_array) / (board_size + 1))):  # go board-wise
        board = f_array[(board_size + 1) * idx + 1:(board_size + 1) * idx + board_size + 1]  # get data of one board
        f_board_array.append([list(map(int, board[idy][0].split())) for idy in range(len(board))])  # append board

    f_marked_boards_array = []  # set up marked_boards_array
    for i in range(len(f_board_array)):  # go board-wise
        f_marked_boards_array.append([[0 for _ in range(board_size)] for _ in range(board_size)])  # zero everywhere
    return f_board_array, f_marked_boards_array


def set_new_number(boards, marked_boards, number_drawn):
    """ mark marked_boards with number_drawn """
    indices = [(idx, idy, idz)
               for idx, board in enumerate(boards)
               for idy, row in enumerate(board)
               for idz, col in enumerate(row)
               if boards[idx][idy][idz] == number_drawn]  # list of 3-tuple indices of cells that contain number_drawn
    for idx, idy, idz in indices:
        marked_boards[idx][idy][idz] = 1  # mark cells that contain number_drawn in all boards with 1
    return marked_boards


def mark_finished_boards(boards, winner_boards, board_size=5):
    """ checks for finished boards and marks the element at its index in winner_boards list with place of the board"""
    for idx in range(len(boards)):  # go board-wise
        col_chosen = [0 for _ in range(board_size)]
        for idy in range(board_size):  # go row-wise
            row_chosen = 0
            for idz in range(len(boards[0][0])):  # go column-wise
                if boards[idx][idy][idz] == 1:  # if cell is marked
                    col_chosen[idz] += 1
                    row_chosen += 1
            if (row_chosen == board_size) and not winner_boards[idx]:  # row marked and board not yet won?
                winner_boards[idx] = max(winner_boards) + 1  # mark board with place
        for idz in range(board_size):  # go column-wise
            if (col_chosen[idz] == board_size) and not winner_boards[idx]:  # column marked and board not yet won?
                winner_boards[idx] = max(winner_boards) + 1  # mark board with place
    return winner_boards


def calc_winning_board_value(winner_searched=1):
    """ calculates the winning board at place winner_searched and returns parameters """
    array = readfile()
    numbers_to_draw = list(map(int, array.pop(0)))  # list of numbers to be still drawn, list will be emptied
    board_array, marked_boards_array = prepare_arrays(array)  # lists of bingo boards & of marked numbers in boards
    """  board_array[board][row][column] to reach a bingo boards' cell and likewise in marked_numbers_array """
    winner_board_array = [0] * len(board_array)  # list of all boards, number will be place of board to finish

    while numbers_to_draw:
        last_number = numbers_to_draw.pop(0)
        marked_boards_array = set_new_number(board_array, marked_boards_array, last_number)  # mark arrays
        winner_board_array = mark_finished_boards(marked_boards_array, winner_board_array)  # check for finished boards

        if max(winner_board_array) == winner_searched:  # place of wanted board reached?
            winner_board = winner_board_array.index(max(winner_board_array))  # determine searched winner
            sum_of_unmarked = sum([a * (1 - b)
                                   for x, y in zip(board_array[winner_board], marked_boards_array[winner_board])
                                   for a, b in zip(x, y)])  # calculate sum of unmarked cells of winner board
            print('',
                  'place:', winner_searched, '\n',
                  'board number:', winner_board, '\n',
                  'lost number drawn:', last_number, '\n',
                  'winning boards final score:', sum_of_unmarked, '\n',
                  'product of last number drawn and winning boards final score:', last_number * sum_of_unmarked, '\n')
            return

    print('failed to determine winner number', winner_searched, ', no numbers left to draw')


if __name__ == "__main__":
    calc_winning_board_value(1)
    calc_winning_board_value(100)
