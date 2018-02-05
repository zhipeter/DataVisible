'''
Die
'''
from random import randint


class Die():
    '''class of die'''

    def __init__(self, num_sides=6):
        '''init die'''
        self.num_sides = num_sides

    def roll(self):
        '''return a value'''
        return randint(1, self.num_sides)
