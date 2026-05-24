import math
import random

from aim_points import aim_points
from board_measurements import BoardMeasurements
from checkout_routes import checkout_routes
from dartboard import DartBoard


class DartBot:

    def __init__(self, aim_skill: list):
        self.dartboard = DartBoard()
        self.sigma_x = aim_skill[0]
        self.sigma_y = aim_skill[1]

    def think(self, remaining_score: int) -> tuple[str, tuple]:
        try:
            aim_at = checkout_routes[remaining_score][0]
        except KeyError as e:
            aim_at = "T20"

        aim_coordinates = aim_points[aim_at]

        return aim_at, aim_coordinates

    def throw_dart(self, aim_point: tuple) -> tuple[int, str, int]:
        # generate randomly how far away you are from aiming point
        x_dist_from_aimpoint = random.normalvariate(mu=0, sigma=self.sigma_x)
        y_dist_from_aimpoint = random.normalvariate(mu=0, sigma=self.sigma_y)

        # unpack aim point
        aim_x, aim_y = aim_point

        # compute position of thrown dart
        x = aim_x + x_dist_from_aimpoint
        y = aim_y + y_dist_from_aimpoint

        # find which segment was hit, and if it was a treble, double, or single
        score, segment_type, segment_number = self.dartboard.get_score(hit_loc=[x, y])

        return score, segment_type, segment_number
    
    def turn(self, remaining_score: int) -> tuple[int, str, int]:
        aim_at, aim_coordinates = self.think(remaining_score)
        score, segment_type, segment_number = self.throw_dart(aim_coordinates)
        return aim_at, score, segment_type, segment_number




