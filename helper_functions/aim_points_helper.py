import math


def polar_to_cartesian(theta, r):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return round(x, 3), round(y, 3)

# define angle to aim at for each segment
segment_angle = math.pi / 10
segment_angles = [segment_angle * i for i in range(20)]

# define how far from the center to aim for each segment type
radius_for_singles = 133.5
radius_for_doubles = 165
radius_for_trebles = 102
radius_for_single_bull = 11.175

# create clockwise order of segments on the dartboard
segment_ordering = [
    "6",
    "13",
    "4",
    "18",
    "1",
    "20",
    "5",
    "12",
    "9",
    "14",
    "11",
    "8",
    "16",
    "7",
    "19",
    "3",
    "17",
    "2",
    "15",
    "10",
]

singles = [f"S{segment}" for segment in segment_ordering]
doubles = [f"D{segment}" for segment in segment_ordering]
trebles = [f"T{segment}" for segment in segment_ordering]

singles_dict = {
    singles[i]: polar_to_cartesian(segment_angles[i], radius_for_singles) 
    for i in range(len(singles))
}
print(singles_dict)
print("")

doubles_dict = {
    doubles[i]: polar_to_cartesian(segment_angles[i], radius_for_doubles) 
    for i in range(len(doubles))
}
print(doubles_dict)
print("")

trebles_dict = {
    trebles[i]: polar_to_cartesian(segment_angles[i], radius_for_trebles) 
    for i in range(len(trebles))
}
print(trebles_dict)
print("")

bull_dict = {
    "S25": polar_to_cartesian(math.pi / 2, radius_for_single_bull),
    "D25": (0, 0)
}
print(bull_dict)
print("")  

# create a complete dictionary for all aim points
all_segments_dict = singles_dict | doubles_dict | trebles_dict | bull_dict
print(all_segments_dict)
