def read_input(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines



def decode(instructions: list, start_point: int = 50):
    zero_counter = 0
    current_pos = start_point

    for instruction in instructions:
        instruction = instruction.strip()
        direction = instruction[0]
        try:
            amount = int(instruction[1:])
        except ValueError:
            continue

        if direction == "R":

            target_pos = current_pos + amount

            zeros = (target_pos // 100) - (current_pos // 100)
            zero_counter += zeros

            current_pos = target_pos % 100

        elif direction == "L":
            target_pos = current_pos - amount

            zeros = ((current_pos - 1) // 100) - ((target_pos - 1) // 100)
            zero_counter += zeros

            current_pos = target_pos % 100

    return zero_counter

if __name__ == '__main__':
    lines = read_input("input/day1.txt")
    decoded_lines = decode(lines, 50)
    print(decoded_lines)