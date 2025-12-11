from itertools import combinations
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def read_file(filename):
    file = open(filename, 'r')
    data = file.readlines()
    file.close()

    new_data = []
    for line in data:
        x = int(line.split(",")[0])
        y = int(line.split(",")[1])
        new_data.append(Point(x, y))

    return new_data


def get_max_square(data):
    combs = list(combinations(data, 2))
    max_area = 0

    for pos1, pos2 in combs:
       area = (abs(pos1.x - pos2.x)+1) * (abs(pos1.y - pos2.y)+1)
       if area > max_area:
           max_area = area

    return max_area

def get_max_square_part2(data):
    combs = list(combinations(data, 2))
    walls = []
    max_area = 0
    for i in range(len(data)):
        p1 = data[i]
        p2 = data[(i + 1) % len(data)]  # Verbindet auch letzten mit erstem Punkt
        walls.append((p1, p2))

    for comb in combs:

        A = comb[0]
        C = comb[1]

        area = (abs(A.x - C.x) + 1) * (abs(A.y - C.y) + 1)
        if area < max_area:
            continue

        x1, x2 = min(A.x, C.x), max(A.x, C.x)
        y1, y2 = min(A.y, C.y), max(A.y, C.y)

        P_TL = Point(x1, y1)
        P_TR = Point(x2, y1)
        P_BR = Point(x2, y2)
        P_BL = Point(x1, y2)

        rect = [
            (P_TL, P_TR),
            (P_TR, P_BR),
            (P_BR, P_BL),
            (P_BL, P_TL),
        ]

        invalid = False
        for edge in rect:
            for wall in walls:
                if check_intersection(edge[0], edge[1], wall[0], wall[1]):
                    invalid = True
                    break

            if invalid:
                break
        if not invalid:
            max_area = area

    return max_area



def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)


def check_intersection(point_a, point_b, point_c, point_d):
    """
    Überprüft, ob die Gerade ab sich mit der Gerade cd schneidet
    :param point_a: Punkt A
    :param point_b: Punkt B
    :param point_c: Punkt C
    :param point_d: Punkt D
    :return:
    """
    return ccw(point_a, point_c, point_d) != ccw(point_b, point_c, point_d) and ccw(point_a, point_b, point_c) != ccw(point_a, point_b, point_d)



if __name__ == '__main__':
    data = read_file("input/day9.txt")
    print(get_max_square_part2(data))