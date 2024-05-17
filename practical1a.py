# WAP to implement DDA line drawing algorithm
from PIL import Image

# creating an image object
width = 500
height = 500
image = Image.new("RGB", (width, height), "white")

# Digital Differential Analyzer line algorithm (DDA)
def draw_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    m = dy / dx

    while x0 <= x1:
        image.putpixel((round(x0), height - round(y0)), (0, 0, 0))
        x0 += 1
        y0 += m

# Example
draw_line(100, 100, 400, 400)

# Save and show the image
image.save("C:\\Users\\Hemant\\Desktop\\SEMESTER 6\\COMPUTER GRAPHICS 📊\\img1.png")
image.show()