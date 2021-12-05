import math
import numpy as np

def load_file(fname):
    with open(fname) as fid:
        data = fid.readlines()
    return data

def filter_on_bit(data, bit_pos, mode='least'):

    n_ratings = data.shape[0]
    summed_bits = data[:, bit_pos].sum() 


    threshold = math.ceil(n_ratings/2)
    if summed_bits >= threshold:
        bit_value = 0 
    else:
        bit_value = 1

    # swap bit value for 'most'
    if mode == 'most':
        if bit_value == 1:
            bit_value = 0
        else:
            bit_value = 1

    return data[data[:,bit_pos] == bit_value]

def get_rating(data, type='o2'):

    if type == 'o2':
        mode = 'most'
    elif type == 'co2':
        mode = 'least'

    nbits = data.shape[1]

    for i in range(nbits):
        data = filter_on_bit(data, i, mode)
        if data.shape[0] == 1:
            break
    return data[0,:]

#data = load_file('test_input.txt')
data = load_file('input.txt')

data = np.array([list(x.strip()) for x in data], dtype=int)

summed_bits = data.sum(axis=0) / data.shape[0]

most_common_bit = np.where( summed_bits < 0.5, 0, 1)
least_common_bit = np.where( summed_bits < 0.5, 1, 0)

gamma = int(''.join(most_common_bit.astype(str)), 2)
epsilon = int(''.join(least_common_bit.astype(str)), 2)

solution_pt1 = gamma * epsilon

print('Solution Day 03, part 1 = {}'.format(solution_pt1))

o2 = get_rating(data, 'o2')
co2 = get_rating(data, 'co2')

o2_gen_rating = int(''.join(o2.astype(str)), 2)
co2_scrubber_rating = int(''.join(co2.astype(str)), 2)
solution_pt2 = o2_gen_rating * co2_scrubber_rating

print('Solution Day 03, part 2 = {}'.format(solution_pt2))