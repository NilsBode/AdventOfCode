import numpy as np

def read_data(input):
    file = open(input, 'r')
    lines = file.readlines()
    file.close()
    new_lines = []
    for line in lines:
        small_list = []
        for el in list(line):
            if el != "\n":
                small_list.append(int(el))
        new_lines.append(small_list)

    return new_lines


def calc_data(lines: list[list[int]]):
    sum = 0

    for line in lines:
        remaining_digits = 11
        tmp_line = line[:-12]
        index_first_digit = np.argmax(tmp_line)
        line_number  = f"{tmp_line[index_first_digit]}"

        index_last_digit = index_first_digit
        for i in range(remaining_digits, 0 , -1):
            tmp_line2 = line[index_last_digit + 1:]
            possible_digit = np.argmax(tmp_line2)
            while possible_digit > len(tmp_line2) - remaining_digits:
                tmp_line2 = line[index_last_digit + 1:possible_digit]
                possible_digit = np.argmax(tmp_line2)

            else:
                index_last_digit = possible_digit + 1 + remaining_digits - i
                number = str(tmp_line2[possible_digit])
                line_number = f"{line_number}{number}"

        print(line_number)
        sum += int(line_number)


    return sum





if __name__ == '__main__':
    data = read_data('input/day3_test.txt')
    print(calc_data(data))