from math import hypot

def distance_between_points(a, b):
    return hypot(a.x - b.x, a.y - b.y)