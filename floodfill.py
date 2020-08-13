image = [
    list("...#######........"),
    list("...#.....#........"),
    list("...#.....#........"),
    list("...#..######......"),
    list("...#..#....#......"),
    list("...####....######."),
    list("....#...........#."),
    list("....#############."),
    list(".................."),
]


def print_image():
    for line in image:
        print("".join(line))


def floodfill(canvas, row, col, char):
    # BASE CASES
    if row < 0 or row > len(canvas) - 1 or col < 0 or col > len(canvas[0]) - 1:
        return
    if canvas[row][col] != ".":
        return

    canvas[row][col] = char

    floodfill(canvas, row - 1, col, char)
    floodfill(canvas, row + 1, col, char)
    floodfill(canvas, row, col + 1, char)
    floodfill(canvas, row, col - 1, char)


floodfill(image, 2, 5, "+")
floodfill(image, 5, 9, "^")
floodfill(image, 1, 1, "0")
print_image()
