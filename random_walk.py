'''
random walk
'''
from random import choice


class RandomWalk():
    '''create a class of randomwalk'''

    def __init__(self, num_points=5000):
        '''init class'''
        self.num_points = num_points

        # start from (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''calculate all points'''
        while len(self.x_values) < self.num_points:

            # decide walk direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # refuse staying
            if x_step == 0 and y_step == 0:
                continue

            # calculate next point
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
