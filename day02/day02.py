def load_file(fname):
    with open(fname) as fid:
        data = fid.readlines()
    return data

def part1(data):
    x_position = 0
    z_position = 0

    for d in data:
        instruction, value = d[0], int(d[1])
        if instruction == 'forward':
            x_position += value
        elif instruction == 'up':
            z_position -= value
        elif instruction == 'down':
            z_position += value
        else:
            raise ValueError('Expected forward, up, down... got {}'.format(instruction))
    return x_position, z_position

def part2(data):
    x_position = 0
    z_position = 0
    aim = 0

    for d in data:
        instruction, value = d[0], int(d[1])
        if instruction == 'forward':
            x_position += value
            z_position += (aim * value)
        elif instruction == 'up':
            aim -= value
        elif instruction == 'down':
            aim += value
        else:
            raise ValueError('Expected forward, up, down... got {}'.format(instruction))
    return x_position, z_position, aim


fname = 'input.txt'
data = load_file(fname)

data = [x.split() for x in data]

x_position, z_position = part1(data)    
pt1_solution = x_position * z_position
print('Solution to Day 2, part 1 = {}'.format(pt1_solution))

x_position, z_position, aim = part2(data)    
pt2_solution = x_position * z_position
print('Solution to Day 2, part 2 = {}'.format(pt2_solution))