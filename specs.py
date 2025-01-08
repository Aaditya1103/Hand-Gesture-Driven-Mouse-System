import numpy as np

def calculate_angle(point1, point2, point3):
#Calculate the angle between three points with point2 as the vertex.
    radians = np.arctan2(point3[1] - point2[1], point3[0] - point2[0]) - np.arctan2(point1[1] - point2[1], point1[0] - point2[0])
    angle = np.abs(np.degrees(radians))
    return angle

def calculate_distance(points):
#Calculate the distance between two points given as a list.
    if len(points) < 2:
        return 0
    (x1, y1), (x2, y2) = points[0], points[1]
    distance = np.hypot(x2 - x1, y2 - y1)
    return np.interp(distance, [0, 1], [0, 1000])