import numpy as np

def load_file(fname):
    with open(fname) as fid:
        lines = fid.readlines()
        data = [line.strip() for line in lines]
    data = [int(x) for x in data[0].split(',')]
    return data

def part1(data):
    return [np.abs(np.array(data) - i).sum() for i in range(max(data))]

def get_fuel2(data, i):
    a = np.abs(np.array(data) - i)
    return np.sum((a * (a + 1)) // 2)    

def part2(data):
    return [get_fuel2(data, i) for i in range(max(data))]

#data = load_file('test_input.txt')
data = load_file('input.txt')

fuel = part1(data)

print('Solution Day 6, part 1 = {}'.format(min(fuel)))

fuel2 = part2(data)
print('Solution Day 6, part 2 = {}'.format(min(fuel2)))
