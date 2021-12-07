
import numpy as np
        
def load_file(fname):
    with open(fname) as fid:
        lines = fid.readlines()
        data = [line.strip() for line in lines]
    return data

def get_lines(data):
    lines = []
    for d in data:
        d = d.split(' -> ')
        start = tuple(int(x) for x in d[0].split(','))
        end = tuple(int(x) for x in d[1].split(','))
        lines.append((start, end))
    return lines

def get_max_xy(lines):
    max_x = 0
    max_y = 0 
    for line in lines:
        p1, p2 = line
        mx = max(p1[0], p1[0])
        if mx > max_x:
            max_x = mx

        my = max(p1[1], p1[1])
        if my > max_y:
            max_y = mx

    return max_x, max_y

def part1(lines, max_x, max_y):
    
    grid = np.zeros((max_x+1, max_y+1))

    for line in lines:
        p1, p2 = line
        if (p1[0] == p2[0]):
            a, b = sorted((p1[1],p2[1]))
            grid[p1[0], a:b+1] += 1

        if (p1[1] == p2[1]):
            a, b = sorted((p1[0],p2[0]))
            grid[a:b+1, p1[1]] += 1

    c = np.count_nonzero(grid >= 2)

    return c

def get_range(start, stop):
        if start > stop:
            i_range = range(start, stop-1, -1)
        else:
            i_range = range(start, stop+1)

        return i_range

def part2(lines, max_x, max_y):
    """There is neater way to do this!
    """
    grid = np.zeros((max_x+1, max_y+1))

    for line in lines:

        p1, p2 = line
        if (p1[0] == p2[0]):
            a, b = sorted((p1[1],p2[1]))
            grid[p1[0], a:b+1] += 1

        elif (p1[1] == p2[1]):
            a, b = sorted((p1[0],p2[0]))
            grid[a:b+1, p1[1]] += 1
        else:
            i_range = get_range(p1[0], p2[0])
            j_range = get_range(p1[1], p2[1])

            for i, j in zip(i_range,j_range):
                    grid[i,j] += 1

    c = np.count_nonzero(grid >= 2)

    return c


#data = load_file('test_input.txt')
data = load_file('input.txt')

lines = get_lines(data)
max_x, max_y = get_max_xy(lines)

c = part1(lines, max_x, max_y)

print('Solution to Day 5, part 1 = {}'.format(c))

c = part2(lines, max_x, max_y)

print('Solution to Day 5, part 2 = {}'.format(c))