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

    def get_score(self, hit_loc: list[float]) -> tuple[int, str, int]:
        # convert dart position to polar coordinates 
        r, theta = self.compute_polar_coordinates(x=hit_loc[0], y=hit_loc[1])
        
        for key, value in BoardMeasurements.segment_radii.items():
            if value[0] < r <= value[1]:
                segment_type = key
            elif r > 170: 
                return 0, "out", 0
            elif r == 0:
                return 50, "bull", 50

        for key, value in BoardMeasurements.segment_angles.items():
            if value[0] < theta <= value[1]:
                if segment_type == "bull":
                    return 50, "bull", 50
                elif segment_type == "outer_bull":
                    return 25, "outer_bull", 25
                else:
                    if key == "6+" or key == "6-":
                        segment_number = 6
                    else:
                        segment_number = key
            elif theta == 0:
                if segment_type == "bull":
                    return 50, "bull", 50
                elif segment_type == "outer_bull":
                    return 25, "outer_bull", 25
                else:
                    segment_number = 6

        # compute scored value of the dart
        if segment_type == "treble":
            score = 3 * segment_number
        elif segment_type == "double":
            score = 2 * segment_number
        else:
            score = segment_number # bull already has 50 as the number        
        
        # return the number and "double"/"triple" segment
        return score, segment_type, segment_number
    

    