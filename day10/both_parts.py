def readfile(filename="input.txt"):
    """ reads file and replaces  in each line, than appends line to list of lists"""
    with open(filename, "r") as f:
        temp_array = f.read().splitlines()  # list of lines containing a string
    for idx in range(len(temp_array)):
        temp_array[idx] = [i for i in temp_array[idx]]
    return temp_array


def discard_corrupt_lines():
    """ goes through array row by row and element by element. builds up an identifier string with opening elements
     and deletes elements if closed. adds up score of corrupted lines and returns non corrupted line identifiers."""
    corrupt_sum = 0
    non_corrupt_lines = []
    for line in array:  # go row-wise
        line_id = ""
        for el in line:  # go element-wise
            if el == "(":  # build line identifier
                line_id += "1"
            elif el == "[":
                line_id += "2"
            elif el == "{":
                line_id += "3"
            elif el == "<":
                line_id += "4"
            elif el == ")":  # check for correct closing character
                if line_id[-1] == "1":
                    line_id = line_id[:-1]  # deletes closed character from line identifier
                else:
                    corrupt_sum += 3  # add up corrupted line score
                    line_id = "c"  # line is corrupted
                    break
            elif el == "]":
                if line_id[-1] == "2":
                    line_id = line_id[:-1]
                else:
                    corrupt_sum += 1197
                    line_id = "c"
                    break
            elif el == "}":
                if line_id[-1] == "3":
                    line_id = line_id[:-1]
                else:
                    corrupt_sum += 57
                    line_id = "c"
                    break
            elif el == ">":
                if line_id[-1] == "4":
                    line_id = line_id[:-1]
                else:
                    corrupt_sum += 25137
                    line_id = "c"
                    break
        if line_id != "c":  # line not corrupted ? (why is this necessary? loop was broken for corrupt lines...)
            non_corrupt_lines.append(line_id)
    print(corrupt_sum)
    return non_corrupt_lines


def autocomplete_scoring():
    """ calculates the autocomplete score of each unfinished line """
    auto_scores = []
    for line in line_ids:  # go line-wise
        auto_score = 0
        line = line[::-1]  # reverse string
        for el in line:  # go element-wise
            if el == "1":  # calculate new auto_score
                auto_score *= 5
                auto_score += 1
            if el == "2":
                auto_score *= 5
                auto_score += 2
            if el == "3":
                auto_score *= 5
                auto_score += 3
            if el == "4":
                auto_score *= 5
                auto_score += 4
        auto_scores.append(auto_score)
    auto_scores.sort()
    print(auto_scores[int((len(auto_scores) - 1) / 2)])  # look for middle element


if __name__ == "__main__":
    array = readfile()
    line_ids = discard_corrupt_lines()
    autocomplete_scoring()

