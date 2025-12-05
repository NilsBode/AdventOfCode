from os.path import split


def read_data(input):
    file = open(input, 'r')
    data = file.read()
    file.close()
    data = data.split("\n\n")
    fresh = data[0].split("\n")
    test = data[1].split("\n")

    ranges = []
    for rnge in fresh:
        start_val = int(rnge.split("-")[0])
        stop_val = int(rnge.split("-")[1])

        ranges.append([start_val, stop_val])


    return ranges, test


def check_data(fresh, test):
    counter = 0
    for tester in test:
        for possible_range in fresh:

            if possible_range[0] <= int(tester) <= possible_range[1]:
                counter += 1
                break

    return counter

def count_fresh(fresh):
    fresh.sort()
    new_fresh = []
    counter = 0
    while counter < len(fresh)-1:
        i=counter+1
        while fresh[counter][1] >= fresh[i][1]:
            fresh.pop(i)

        counter += 1


    changed = True
    while changed:
        changed = False
        i = 0
        while i < len(fresh):
            if i == len(fresh)-1:
                new_fresh.append(fresh[i])
            elif fresh[i][1] >= fresh[i+1][0]:
                new_fresh.append([fresh[i][0], fresh[i+1][1]])
                i += 1
                changed = True
            else:
                new_fresh.append(fresh[i])
            i += 1

        fresh = new_fresh
        new_fresh = []

    counter = 0
    for pair in fresh:
        counter += pair[1] - pair[0] +1

    print(fresh)
    return counter

if __name__ == '__main__':
    a = [[5, 6], [0, 2], [9, 11], [-1, 5]]
    fresh, id = read_data('input/day5.txt')
    print(len(fresh))
    print(count_fresh(fresh))