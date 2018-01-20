#!/usr/bin/python
"""
Write a function that will solve a 9x9 Sudoku puzzle. The function will take 
one argument consisting of the 2D puzzle array, with the value 0 representing 
an unknown square.

The Sudokus tested against your function will be "easy" (i.e. determinable; 
there will be no need to assume and test possibilities on unknowns) and can be
solved with a brute-force approach.

For Sudoku rules, see the Wikipedia article.
https://en.wikipedia.org/wiki/Sudoku
"""
from __future__ import print_function

# Grids defined by their Top Left and Bottom Right Corner on the Sudoku matrix.
GRIDS = (((0, 0), (2, 2)), ((3, 0), (5, 2)), ((6, 0), (8, 2)),
         ((0, 3), (2, 5)), ((3, 3), (5, 5)), ((6, 3), (8, 5)),
         ((0, 6), (2, 8)), ((3, 6), (5, 8)), ((6, 6), (8, 8)))

def get_box_grid(x, y):
    """Determine the box grid, the row 'x' and column 'y' are in and return 
    the box grid boundaries (top left, bottom right).
    """
    for grid in GRIDS:
        if x >= grid[0][0] and y >= grid[0][1] and \
           x <= grid[1][0] and y <= grid[1][1]:
            return grid
    return None

def rm_pot(potential, puzzle, tl, br):
    """Check through the puzzle array in the range delimited by top left (tl) 
    and bottom right (br) for values in 'potential'. Any value found that is
    in 'potential' is removed so only missing values remain when it is 
    returned.
    """
    for y in range(tl[1], br[1]+1):
        for x in range(tl[0], br[0]+1):
            if puzzle[y][x] in potential:
                potential.remove(puzzle[y][x])
    return potential

def sudoku(puzzle):
    # Loop until there are no empty values (0) in the 2D Sudoku aray.
    count_zero = 81
    while (count_zero):
        count_zero = 0
        for y in range(9):
            for x in range(9):
                # If the current box is empty (is 0)
                if not puzzle[y][x]:

                    # Potentially, this box can be any value in the range 1..9
                    potential = list(range(1, 10))

                    # Remove  values in the same row
                    potential = rm_pot(potential, puzzle, (0, y), (8, y))

                    # Remove values in the same column
                    if len(potential) > 1:
                        potential = rm_pot(potential, puzzle, (x, 0), (x, 8))

                    # Remove values in the same box-grid
                    if len(potential) > 1:
                        box = get_box_grid(x, y)
                        potential = rm_pot(potential, puzzle, box[0], box[1])

                    # If there is only 1 value left in the list of potential
                    # values, then that must be the missing value!
                    if len(potential) == 1:
                        puzzle[y][x] = potential[0]
                    else:
                        count_zero += 1
    return puzzle

if __name__ == "__main__":

    puzzle = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]

    result = sudoku(puzzle)

    for y in range(9):
        for x in range(9):
            print("{} ".format(result[y][x]), end="")
        print("")

