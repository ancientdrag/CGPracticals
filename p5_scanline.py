import numpy as np
import matplotlib.pyplot as plt

def scanline_fill(points):
    
    # Find the min and max y-coordinates
    ymin = int(min(points[:,1]))
    ymax = int(max(points[:,1]))

    # Initialize an array to store the x-coordinates of the intersections
    # between the scanline and the polygon edges
    x_intersections = np.zeros((len(points),))

    # Iterate over each scanline
    for y in range(ymin, ymax+1):
        # Find the edges that intersect the scanline
        j = 0
        for i in range(len(points)):
            if i == len(points) - 1:
                k = 0
            else:
                k = i + 1

            if (points[i][1] <= y and points[k][1] > y) or (points[k][1] <= y and points[i][1] > y):
                x_intersections[j] = int(points[i][0] + (y - points[i][1]) / (points[k][1] - points[i][1]) * (points[k][0] - points[i][0]))
                j += 1

        # Sort the intersections by x-coordinate
        x_intersections = np.sort(x_intersections[:j])

        # Fill the scanline between pairs of intersections
        for i in range(0, len(x_intersections), 2):
            plt.plot([x_intersections[i], x_intersections[i+1]], [y, y], color='black')

    plt.show()

#example usage
points = np.array([(100, 100), (200, 200), (300, 150), (200, 100)])
scanline_fill(points)
