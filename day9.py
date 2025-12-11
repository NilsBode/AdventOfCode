from itertools import combinations

def read_file(filename):
    file = open(filename, 'r')
    data = file.readlines()
    file.close()

    new_data = []
    for line in data:
        x = int(line.split(",")[0])
        y = int(line.split(",")[1])
        new_data.append((x, y))

    return new_data


def get_max_square(data):
    combs = list(combinations(data, 2))
    max_area = 0

    for pos1, pos2 in combs:
       area = (abs( pos1[0] - pos2[0])+1) * (abs(pos1[1] - pos2[1])+1)
       if area > max_area:
           max_area = area

    return max_area


if __name__ == '__main__':
    data = read_file("input/day9.txt")
    print(get_max_square(data))