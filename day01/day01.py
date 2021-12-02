def load_file(fname):
    with open(fname) as fid:
        data = fid.readlines()
    return data

def count_increases(data):
    n_increases = 0
    for i in range(len(data) - 1):
        if data[i+1] - data[i] > 0:
            n_increases += 1
    return n_increases

def sum_window(data, winlen=3):
    out = []
    for i in range(len(data) - winlen + 1):
        out.append(sum(data[i:i+winlen]))
    return out


fname = 'input01.txt'
data = load_file(fname)
data = [int(x.strip()) for x in data]

n_increases = count_increases(data)
print('Part 1 Number of increases = {}'.format(n_increases))

summed_data = sum_window(data, 3)
n_summed_increases = count_increases(summed_data)
print('Part 2 Number of increases = {}'.format(n_summed_increases))

