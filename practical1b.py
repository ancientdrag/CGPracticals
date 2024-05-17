# Bresengham's line drawing algorithm
from matplotlib import pyplot as plt

x1 = int(input("Enter x0 value: "))
y1 = int(input("Enter y0 value: "))
x2 = int(input("Enter x1 value: "))
y2 = int(input("Enter y1 value: "))
dx = abs(x2-x1)
dy = abs(y2-y1)

def plotPixel(x1,y1,x2,y2, dx, dy):
    pk = 2*dy-dx
    x_cordinates = []
    y_cordinates = []
    
    for i in range(0,dx+1):
        x_cordinates.append(x1)
        y_cordinates.append(y1)
        print(x1, ",", y1)
        x1 = x1 + 1
        if (pk < 0):
            pk = pk +2 * dy
        else:
            pk = pk + 2 * dy
            y1 = y1 + 1
        # plot the line with cordinates list
            plt.plot(x_cordinates, y_cordinates, marker = "o", markersize = 1, markerfacecolor = "green")
    plt.show()

plotPixel(x1,y1,x2,y2,dx,dy)