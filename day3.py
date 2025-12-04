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
        tmp_line = line[:-12]
        index_first_digit = np.argmax(tmp_line)
        tmp_line2 = line[index_first_digit+1:]
        index_second_digit = np.argmax(tmp_line2)

        number = int(f"{tmp_line[index_first_digit]}{tmp_line2[index_second_digit]}")
        print(number)
        sum += number


    return sum





if __name__ == '__main__':
    data = read_data('input/day3.txt')
    print(calc_data(data))