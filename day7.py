from functools import cache

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

@cache
def simulate_part2(start_row, index):
    if start_row == len(data)-1:
        return 1

    total_ways = 0

    if data[start_row+1][index] == ".":
        total_ways += simulate_part2(start_row + 1, index)

    elif data[start_row+1][index] == "^":
        total_ways += simulate_part2(start_row + 1, index + 1)
        total_ways += simulate_part2(start_row + 1, index - 1)

    return total_ways

data = read_data("input/day7.txt")

if __name__ == '__main__':

    print(simulate_part2(0, 70))