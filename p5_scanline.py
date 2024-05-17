import matplotlib.pyplot as plt

def draw_pixel(canvas, x, y, color):
    canvas[y][x] = color

def get_pixel(canvas, x, y):
    return canvas[y][x]

def scanline_fill(canvas, seed_point, fill_color):
    stack = [seed_point]

    while stack:
        x, y = stack.pop()

        # Move to the left boundary
        while x >= 0 and get_pixel(canvas, x, y) != fill_color:
            x -= 1
        x += 1

        # Fill the scanline to the right
        while x < len(canvas[0]) and get_pixel(canvas, x, y) != fill_color:
            draw_pixel(canvas, x, y, fill_color)

            # Check and push neighboring pixels
            if y > 0 and get_pixel(canvas, x, y - 1) != fill_color:
                stack.append((x, y - 1))
            if y < len(canvas) - 1 and get_pixel(canvas, x, y + 1) != fill_color:
                stack.append((x, y + 1))

            x += 1

def main():
    width, height = 20, 20
    canvas = [[(255, 255, 255) for _ in range(width)] for _ in range(height)]

    seed_point = (10, 10)
    fill_color = (255, 0, 0)

    # Drawing a simple shape
    for y in range(5, 15):
        for x in range(5, 15):
            draw_pixel(canvas, x, y, (0, 0, 0))

    scanline_fill(canvas, seed_point, fill_color)

    # Visualize the canvas using Matplotlib
    plt.imshow(canvas)
    plt.title("Scanline Fill Algorithm")
    plt.show()

if __name__ == "__main__":
    main()