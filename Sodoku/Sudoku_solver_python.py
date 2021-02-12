"""
Date:2/01/2021
The following program solves sudoku using Backtracking .
"""

grid=[ [ 3, 0, 6, 5, 0, 8, 4, 0, 0 ],
                       [ 5, 2, 0, 0, 0, 0, 0, 0, 0 ],
                       [ 0, 8, 7, 0, 0, 0, 0, 3, 1 ],
                       [ 0, 0, 3, 0, 1, 0, 0, 8, 0 ],
                       [ 9, 0, 0, 8, 6, 3, 0, 0, 5 ],
                       [ 0, 5, 0, 0, 9, 0, 6, 0, 0 ],
                       [ 1, 3, 0, 0, 0, 0, 2, 5, 0 ],
                       [ 0, 0, 0, 0, 0, 0, 0, 7, 4 ],
                       [ 0, 0, 5, 2, 0, 6, 3, 0, 0 ] ]
def check(x,y,n):
    #rowcheck
    for i in range(9):
        if grid[x][i]==n:
            return False
    for i in range(9):
        if grid[i][y]==n:
            return False
    for i in range((x//3)*3,(x//3)*3+3):
        for j in range((y//3)*3,(y//3)*3+3):
            if grid[i][j]==n:
                return False
    return True

def solve():
    global grid
    import numpy as np

    for x in range(9):
        for y in range(9):
            if grid[x][y]==0:
                for n in range(1,10):
                    if check(x,y,n):
                        grid[x][y]=n
                        solve()
                        grid[x][y]=0
                return
    print("Solved grid:{}".format(np.matrix(grid)))
solve()