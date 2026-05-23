import math
from board_measurements import BoardMeasurements


class DartBoard:


    def __init__(self):
        pass

    @staticmethod
    def compute_polar_coordinates(x, y):
        # prevent division by 0
        if x == 0 and y == 0:
            return 0, 0
        
        r = math.hypot(x, y)
        theta = math.acos(x / r)

        # acos only returns values from 0 to pi, fixing here
        if y < 0:
            theta = 2 * math.pi - theta

        return r, theta

    def get_score(self, hit_loc: list[float]) -> tuple[int, str]:
        # convert dart position to polar coordinates 
        r, theta = self.compute_polar_coordinates(x=hit_loc[0], y=hit_loc[1])

        # from a class variable determine which section of the dartboard the dart landed in
        
        for key, value in BoardMeasurements.segment_radii.items():
            if value[0] < r <= value[1]:
                segment_type = key
            elif r > 170: 
                return 0, "out"
            elif r == 0:
                return 50, "bull"

        for key, value in BoardMeasurements.segment_angles.items():
            if value[0] < theta <= value[1]:
                if segment_type == "bull":
                    return 50, "bull"
                elif segment_type == "outer_bull":
                    return 25, "outer_bull"
                else:
                    segment_number = key
            elif theta == 0:
                if segment_type == "bull":
                    return 50, "bull"
                elif segment_type == "outer_bull":
                    return 25, "outer_bull"
                segment_number = 6
        
        # return the number and "double"/"triple" segment
        return segment_number, segment_type
    

    