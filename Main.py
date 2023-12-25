from pprint import pprint

def fempty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c

    return None, None  

def valid(puzzle, guess, row, col):
    rowval = puzzle[row]
    if guess in rowval:
        return False 
    colval = [puzzle[i][col] for i in range(9)]
    if guess in colval:
        return False
    rowstart = (row // 3) * 3 
    colstart = (col // 3) * 3

    for r in range(rowstart, rowstart + 3):
        for c in range(colstart, colstart + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solves(puzzle):
    row, col = fempty(puzzle)

    if row is None:  
        return True 
    
    
    for guess in range(1, 10):       
        if valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solves(puzzle):
                return True
        
    
        puzzle[row][col] = 0

    
    return False

if __name__ == '__main__':
    board = [
        [ 0, 0, 0,   2, 6, 0,   7, 0, 1],
        [ 6,  8, 0,   0, 7, 0,   0, 9, 0,],
        [ 1,  9, 0,   0, 0, 4,   5, 0, 0],

        [ 8,  2, 0,   1, 0, 0,   0, 4, 0],
        [ 0,  0, 4,   6, 0, 2,    9, 0, 0],
        [ 0, 5, 0,   0, 0, 3,    0, 2, 8,],

        [0, 0, 9,    3, 0, 0,   0, 7, 4],
        [0, 4, 0,   0, 5, 0,   0, 3, 6],
        [ 7, 0, 3,   0,  1,  8,   0, 0, 0]
    ]
    

    print(solves(board))
    pprint(board)
