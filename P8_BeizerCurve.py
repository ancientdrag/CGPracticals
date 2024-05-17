import matplotlib.pyplot as plt
import numpy as np
import math

def bezier_curve(control_points):
    control_points=np.array(control_points)
    
    def B(t):
        n = len(control_points)-1
        return np.sum([control_points[i] * math.comb(n,i) * (t**i) *(1-t)**(n-i) 
                       for i in range(n+1)], axis=0)
     
    # Create a range of values for t
    t_values = np.linspace(0.0, 1.0, 100)

    # Evaluate the Bezier curve function for each value of t
    curve_points = np.array([B(t) for t in t_values])

    # Plot the Bezier curve
    plt.plot(curve_points[:,0], curve_points[:,1], 'b-', label='Bezier Curve')
    # plot the control points
    plt.plot(control_points[:,0], control_points[:,1], 'ro-', label='Control Points')
    plt.legend()
    plt.show()

# Example usage:
control_points = [(1,1), (2,3), (4,4), (6,1)]
bezier_curve(control_points)