
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from login import get_input

input = get_input(4)
next_chars = {"X": "M", "M": "A", "A": "S"}

def add_border(matrix, border_value=" "):
    if not matrix or not matrix[0]:
        return [[border_value, border_value],
                [border_value, border_value]]
    row_length_with_border = len(matrix[0]) + 2
    border_row = [border_value] * row_length_with_border
    bordered_matrix = [[border_value] + row + [border_value] for row in matrix]
    bordered_matrix = [border_row] + bordered_matrix + [border_row]
    return bordered_matrix


matrix = [[chr for chr in line] for line in input.splitlines()]

def get_sub_matrix(matrix, x, y):
    sub_matrix = []
    for dy in range(-2, 3):
        row = []
        for dx in range(-2, 3):
            if 0 <= y + dy < len(matrix) and 0 <= x + dx < len(matrix[0]):
                row.append(matrix[y + dy][x + dx])
            else:
                row.append(" ")
        sub_matrix.append(row)
    return sub_matrix

def find_xmas(matrix, x, y, next_chars):
    word = "X"
    while word[-1] in next_chars:
        word += next_chars[word[-1]]
    if matrix[y][x] != "X":
        return 0
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1), 
        (-1, 1),
        (1, -1), 
        (1, 1)
    ]

    count = 0
    for dy, dx in directions:
        cx, cy = x, y
        found = True
        for i in range(1, len(word)):
            cx += dx
            cy += dy
            if 0 <= cy < len(matrix) and 0 <= cx < len(matrix[0]):
                if matrix[cy][cx] == word[i]:
                    continue
                else:
                    found = False
                    break
            else:
                found = False
                break
        if found:
            count += 1

    return count

xmas_count = 0
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        xmas_count += find_xmas(matrix, x, y, next_chars)

print("(PART 1) XMAS Occurrences:", xmas_count)



def is_x_mas(matrix, x, y):
    if y-1 < 0 or y+1 >= len(matrix) or x-1 < 0 or x+1 >= len(matrix[0]):
        return 0
    if matrix[y][x] != 'A':
        return 0
    top_left = matrix[y-1][x-1]
    top_right = matrix[y-1][x+1]
    bottom_left = matrix[y+1][x-1]
    bottom_right = matrix[y+1][x+1]
    combo1 = (top_left == 'M' and bottom_right == 'S' and
               top_right == 'M' and bottom_left == 'S')
    combo2 = (top_left == 'M' and bottom_right == 'S' and
               top_right == 'S' and bottom_left == 'M')
    combo3 = (top_left == 'S' and bottom_right == 'M' and
               top_right == 'M' and bottom_left == 'S')
    combo4 = (top_left == 'S' and bottom_right == 'M' and
               top_right == 'S' and bottom_left == 'M')
    count = 0
    for combo in [combo1, combo2, combo3, combo4]:
        if combo:
            count += 1

    return count

xmas_count = 0
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        xmas_count += is_x_mas(matrix, x, y)

print("(PART 2) X-MAS Occurrences:", xmas_count)