# Cohen - Sutherland Clipping
from graphics import *

INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8

def computeCode(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE
    if x < xmin: code |= LEFT
    elif x > xmax: code |= RIGHT
    if y < ymin: code |= BOTTOM
    elif y > ymax: code |= TOP
    return code

def cohenSutherlandClip(x1, y1, x2, y2, xmin, ymin, xmax, ymax, win):
    code1, code2 = computeCode(x1, y1, xmin, ymin, xmax, ymax), computeCode(x2, y2, xmin, ymin, xmax, ymax)
    accept = False

    while True:
        if code1 == 0 and code2 == 0: accept = True; break
        elif (code1 & code2) != 0: break
        else:
            code_out = code1 if code1 != 0 else code2
            if code_out & TOP: x, y = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1), ymax
            elif code_out & BOTTOM: x, y = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1), ymin
            elif code_out & RIGHT: y, x = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1), xmax
            elif code_out & LEFT: y, x = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1), xmin
            x1, y1 = (x, y) if code_out == code1 else (x2, y2); code1, code2 = computeCode(x1, y1, xmin, ymin, xmax, ymax), computeCode(x2, y2, xmin, ymin, xmax, ymax)

    if accept:
        print(f"Line accepted from ({x1},{y1}) to ({x2},{y2})")
        Line(Point(x1, y1), Point(x2, y2)).draw(win)
        Line(Point(x1, y1), Point(x2, y2)).setOutline('black')
        Line(Point(x1, y1), Point(x2, y2)).setWidth(2)
    else:
        print("Line rejected")

x1, y1, x2, y2 = 10, 5, 3, 15
xmin, ymin, xmax, ymax = 0, 0, 15, 15

win = GraphWin("Cohen-Sutherland Clipping", 500, 500)
win.setCoords(-1, -1, 16, 16)

Rectangle(Point(xmin, ymin), Point(xmax, ymax)).draw(win)
original_line = Line(Point(x1, y1), Point(x2, y2))
original_line.setOutline('blue')
original_line.draw(win)

cohenSutherlandClip(x1, y1, x2, y2, xmin, ymin, xmax, ymax, win)

win.getMouse()
win.close()