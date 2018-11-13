'''

Copy the previous grid value, and write code that uses
it to print the image.

..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

Hint: You will need to use a loop in a loop in order
to print grid[0][0], then grid[1][0], then grid[2][0],
and so on, up to grid[8][0]. This will finish the first row,
so then print a newline. Then your program should print
grid[0][1], then grid[1][1], then grid[2][1], and so on.
The last thing your program will print is grid[8][5].


'''


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def graphics_printer(sample_grid):
    for i in range(0, 6):
        for j in range(0, 9):
            print(sample_grid[j][i], end='')
            if j == 8:
                print('\n')


graphics_printer(grid)
