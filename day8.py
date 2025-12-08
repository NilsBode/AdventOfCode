import math

import numpy as np
from itertools import combinations

def read_data(input):
    file = open(input, 'r')
    data = file.readlines()
    file.close()
    return data


def calc_distances(data):
    combs = list(combinations(data, 2))
    circuits = []
    for i in range(len(combs)):
        value1 = combs[i][0].split(",")
        value2 = combs[i][1].split(",")

        x1 = int(value1[0])
        y1 = int(value1[1])
        z1 = int(value1[2])

        x2 = int(value2[0])
        y2 = int(value2[1])
        z2 = int(value2[2])

        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
        combs[i] = (combs[i][0], combs[i][1], distance)

    combs.sort(key=lambda x: x[2])
    sorted_combs = combs

    for i in range(10):
        if len(circuits) == 0:
            circuits.append([sorted_combs[i][0], sorted_combs[i][1]])
            continue


        index_first_val = None
        index_second_val = None
        for j in range(len(circuits)):
            if sorted_combs[i][0] in circuits[j]:
                index_first_val = j

            if sorted_combs[i][1] in circuits[j]:
                index_second_val = j

            if index_first_val == index_second_val:
                index_first_val = None
                index_second_val = None

        if index_first_val is not None and index_second_val is not None:
            if index_first_val > index_second_val:
                first_part = circuits.pop(index_first_val)
                second_part = circuits.pop(index_second_val)
            else:
                second_part = circuits.pop(index_second_val)
                first_part = circuits.pop(index_first_val)
            together = first_part + second_part
            circuits.append(together)

        elif index_first_val is None and index_second_val is None:
            circuits.append([sorted_combs[i][0], sorted_combs[i][1]])

        elif index_first_val is not None and index_second_val is None:
            circuits[index_first_val].append(sorted_combs[i][1])

        elif index_second_val is not None and index_first_val is None:
            circuits[index_second_val].append(sorted_combs[i][0])


    circuits.sort(key=lambda x: len(x), reverse=True)
    product = 1
    for i in range(3):
        product *= len(circuits[i])

    return product


if __name__ == '__main__':
    data = read_data('input/day8_test.txt')
    print(calc_distances(data))