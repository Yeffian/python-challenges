import math

def calculate_escape_velocity(m, r):
    # assuming that Earth's g = 9.8
    return math.sqrt(2 * 9.8 * m * r)

