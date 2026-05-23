import math
import random
from dartboard import DartBoard
from board_measurements import BoardMeasurements


class DartBot:

    def __init__(self, aim_skill: list):
        self.sigma_x = aim_skill[0]
        self.sigma_y = aim_skill[1]

    def throw_dart(self, aim_point):
        # generate randomly how far away you are from aiming point
        x_dist_from_aimpoint = random.normalvariate(mu=0, sigma=self.sigma_x)
        y_dist_from_aimpoint = random.normalvariate(mu=0, sigma=self.sigma_y)

        # compute position of thrown dart
        x = aim_point[0] + x_dist_from_aimpoint
        y = aim_point[1] + y_dist_from_aimpoint

        return x, y
    
    # bot needs to know where to aim
    # bot needs the centers of all triple and double zones
    # bot needs the checkout routes

