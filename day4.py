import numpy as np

def read_data(input):
    file = open(input, 'r')
    data = file.readlines()
    new_lines = []
    for line in data:
        new_lines.append(list(line.replace('\n', '')))
    return new_lines


def check_neighbours(pos:(int, int), grid):

    counter = 0

    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if pos[0] + i < 0 or pos[0] + i >= len(grid):
                break
            if pos[1] + j < 0 or pos[1] + j >= len(grid[0]):
                continue
            if grid[pos[0] +  i][pos[1] + j] == '@':
                counter += 1

    return counter - 1 < 4


def check_grid(grid):
    counter = 0

    changed = True
    while changed:
        changed = False
        for x1 in range(len(grid)):
            for x2 in range(len(grid[0])):
                if grid[x1][x2] == '@':
                    if check_neighbours((x1, x2), grid):
                        grid[x1][x2] = '.'
                        changed = True
                        counter += 1

    return counter


if __name__ == '__main__':
    data = read_data('input/day4.txt')
    print(check_grid(data))