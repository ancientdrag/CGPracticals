# mid point circle drawing algorithm
from graphics import GraphWin, Point
import time

def midPointCircleDraw(x_centre, y_centre, r):
    win = GraphWin("Mid Point Circle Generation Program Output", 600, 480)
    x = r
    y = 0
    P = 1 - r
    while x > y:
        x1 = x + x_centre     
        y1 = y + y_centre     
        x2 = -x + x_centre    
        y2 = y + y_centre     
        x3 = x + x_centre      
        y3 = -y + y_centre
        x4 = -x + x_centre
        y4 = -y + y_centre

        PutPixel(win, x1, y1)
        PutPixel(win, x2, y2)
        PutPixel(win, x3, y3)
        PutPixel(win, x4, y4)

        x1 = y + x_centre
        y1 = x + y_centre
        x2 = -y + x_centre
        y2 = x + y_centre
        x3 = y + x_centre
        y3 = -x + y_centre
        x4 = -y + x_centre
        y4 = -x + y_centre

        PutPixel(win, x1, y1)
        PutPixel(win, x2, y2)
        PutPixel(win, x3, y3)
        PutPixel(win, x4, y4)

        y += 1
        if P <= 0:
            P = P + 2 * y + 1
        else:
            x -= 1
            P = P + 2 * y -2 *x + 1
    win.getMouse()
    win.close()

def PutPixel(win, x, y):
    pt = Point(x,y)
    pt.draw(win)

if __name__ == '__main__':
    x,y = map(int, input("Enter center co-ordinates: ").split())
    r = int(input("Enter radius: "))
    midPointCircleDraw(x,y,r)