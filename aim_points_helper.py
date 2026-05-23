import math


segment_angle = math.pi / 10

# singles
angles_for_all = [segment_angle * i for i in range(20)]
radius_for_singles = 133.5


# doubles
radius_for_doubles = 165


# trebles
radius_for_trebles = 102


# D25
radius_for_d25 = 0


# S25
radius_for_s25 = 11.175


def polar_to_cartesian(theta, r):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return round(x, 3), round(y, 3)

singles = [
    "S6",
    "S13",
    "S4",
    "S18",
    "S1",
    "S20",
    "S5",
    "S12",
    "S9",
    "S14",
    "S11",
    "S8",
    "S16",
    "S7",
    "S19",
    "S3",
    "S17",
    "S2",
    "S15",
    "S10",
]

doubles = [
    "D6",
    "D13",
    "D4",
    "D18",
    "D1",
    "D20",
    "D5",
    "D12",
    "D9",
    "D14",
    "D11",
    "D8",
    "D16",
    "D7",
    "D19",
    "D3",
    "D17",
    "D2",
    "D15",
    "D10",
]

trebles = [
    "T6",
    "T13",
    "T4",
    "T18",
    "T1",
    "T20",
    "T5",
    "T12",
    "T9",
    "T14",
    "T11",
    "T8",
    "T16",
    "T7",
    "T19",
    "T3",
    "T17",
    "T2",
    "T15",
    "T10",
]

singles_dict = {singles[i]: polar_to_cartesian(angles_for_all[i], radius_for_singles) for i in range(len(singles))}
print(singles_dict)
print("")

doubles_dict = {doubles[i]: polar_to_cartesian(angles_for_all[i], radius_for_doubles) for i in range(len(doubles))}
print(doubles_dict)
print("")

trebles_dict = {trebles[i]: polar_to_cartesian(angles_for_all[i], radius_for_trebles) for i in range(len(trebles))}
print(trebles_dict)
print("")

d25_dict = {"D25": (0, 0)}
print(d25_dict)
print("")  

s25_dict = {"S25": polar_to_cartesian(math.pi / 2, radius_for_s25)}
print(s25_dict) 
print("")

all_segments_dict = {**singles_dict, **doubles_dict, **trebles_dict, **d25_dict, **s25_dict}
print(all_segments_dict)

