
def read_data(input):
    file = open(input, 'r')
    line = file.readline()
    file.close()
    line = line.split(",")
    ranges = []
    for r in line:
        ranges.append(r.split("-"))

    return ranges





def check_range(start, end):
    counter = 0


    for i in range(start, end+1):
        tested_id = str(i)
        is_repetition = False

        for length in range(1, len(tested_id) // 2 + 1):
            if len(tested_id) % length != 0:
                continue

            current_match = True

            pattern = tested_id[:length]

            for k in range(length, len(tested_id), length):
                chunk = tested_id[k: k + length]

                if pattern != chunk:
                    current_match = False
                    break

            if current_match:
                is_repetition = True
                break

        if is_repetition:
            counter += i


    return counter


if __name__ == '__main__':
    data = read_data("input/day2.txt")
    total_counter = 0
    for pair in data:
        sum = check_range(int(pair[0]), int(pair[1]))
        total_counter += sum

    print(total_counter)
