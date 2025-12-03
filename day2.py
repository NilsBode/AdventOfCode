
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

        count = True
        for length in range(1, len(tested_id) // 2 + 1):
            print("\n")
            for k in range(1, len(tested_id) // max(length, 1)):
                tester = tested_id[:length]
                toTest = tested_id[k * length:k * length + length]
                print(f"{tested_id[:length]} = {tested_id[k * length:k * length + length]}")
                if tested_id[:length] != tested_id[k*length:k*length+length]:

                    count = False
                    break
                c
            if count:
                break

        if count:
            counter += i


    return counter


if __name__ == '__main__':
    data = read_data("input/day2_test.txt")
    total_counter = 0
    for pair in data:
        sum = check_range(int(pair[0]), int(pair[1]))
        total_counter += sum

    print(total_counter)
