
def read_data(input):
    file = open(input, "r")
    data = file.readlines()
    file.close()
    return data

def simulate(data):
    beam_indices = [data[0].index("S")]
    splits = 0
    for i in range(1, len(data)):
        data[i] = data[i].replace("\n", "")
        new_beams = []
        for beam in beam_indices:
            if data[i][beam] == "." and beam not in new_beams:
                new_beams.append(beam)
            elif data[i][beam] == "^":
                if beam + 1 not in new_beams:
                    new_beams.append(beam + 1)

                if beam - 1 not in new_beams:
                    new_beams.append(beam - 1)
                splits += 1

        beam_indices = new_beams
    return splits

def simulate_part2(data, start_row, indice):
    print(start_row)
    if start_row == len(data)-1:
        return 1

    total_ways = 0

    if data[start_row+1][indice] == ".":
        total_ways += simulate_part2(data, start_row+1, indice)

    elif data[start_row+1][indice] == "^":
        total_ways += simulate_part2(data, start_row+1, indice+1)
        total_ways += simulate_part2(data, start_row+1, indice-1)

    return total_ways



if __name__ == '__main__':
    data = read_data("input/day7.txt")

    print(simulate_part2(data, 0, 70))