from collections import Counter
import numpy as np
        
def load_file(fname):
    with open(fname) as fid:
        lines = fid.readlines()
        data = [line.strip() for line in lines]
    return data

# Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, 
# while each other number decreases by 1 if it was present at the start of the day.
def part1(data):
    days = [data]
    days.append([x - 1 for x in days[-1]])
    for i in range(1,80):

        today = days[i].copy()
        n_zeros = today.count(0)
        
        tomorrow = [x-1 if x !=0 else 6 for x in today]
        
        tomorrow.extend([8] * n_zeros)    
        days.append(tomorrow)

    return len(days[-1])

def part2(data, n_iter=256):
 
    c = Counter({i:data.count(i) for i in range(9)})
    for day in range(n_iter):
        c[(day + 7) % 9] += c[day % 9]
    return c.total()

#data = load_file('test_input.txt')
data = load_file('input.txt')

data = [int(x) for x in data[0].split(',')]

n_fish = part1(data)    
print('Solution Day 6, part 1 = {}'.format(n_fish))

n_fish = part2(data, 256)    
print('Solution Day 6, part 2 = {}'.format(n_fish))