
import numpy as np

def load_file(fname):
    with open(fname) as fid:
        data = fid.readlines()
    return data

class BingoCard:

    def __init__(self, numbers):
        self.card = np.array(numbers)
        self.marked = np.zeros_like(self.card) 
        self.bingo = False

    def _check_lines(self, axis):
        indx = None
        sum_along_axis = self.marked.sum(axis=axis)
        n = self.card.shape[axis]
        if any( sum_along_axis == n):
            indx = list(sum_along_axis).index(n)
            if axis == 0:
                indx = (indx, 0)
            elif axis == 1:
                indx = (0, indx)
        return indx

    def check_for_bingo(self):
        if self._check_lines(0):
            self.bingo = self._check_lines(0)
        if self._check_lines(1):
            self.bingo = self._check_lines(1)

    def check_number(self, num):
        self.marked[np.where(self.card == num)] = 1       
        self.check_for_bingo()

def get_bingo_cards(data):
    cards = []
    for i in range(2, len(data), 6):
        card_data = data[i:i+5]
        out = [x.strip().split() for x in card_data]
        for i in range(5):
             out[i] = [int(x) for x in out[i]]

        cards.append(BingoCard(out))

    return cards

def play_bingo(bingo_numbers, cards):
    for num in bingo_numbers:
        for card in cards:
            card.check_number(num)
            if card.bingo:
                #print('Bingo!')
                return num, card

def play_to_loose(bingo_numbers, cards):

    winning_cards = []
    while len(cards) > 0:
        last_called_num, winning_card = play_bingo(bingo_numbers, cards)
        winning_cards.append((last_called_num, winning_card))
        cards.remove(winning_card)
    
    return winning_cards

#data = load_file('test_input.txt')
data = load_file('input.txt')

bingo_numbers = [int(x) for x in data[0].strip().split(',')]

cards = get_bingo_cards(data)

last_called_num, winning_card = play_bingo(bingo_numbers, cards)

sum_unmarked = winning_card.card[winning_card.marked == 0].sum()

print('Solution to day 4, part 1 = {}'.format(last_called_num * sum_unmarked))

cards = get_bingo_cards(data)

winning_cards = play_to_loose(bingo_numbers, cards)

last_called_num, last_winning_card = winning_cards[-1]

sum_unmarked = last_winning_card.card[last_winning_card.marked == 0].sum()

print('Solution to day 4, part 2 = {}'.format(last_called_num * sum_unmarked))
