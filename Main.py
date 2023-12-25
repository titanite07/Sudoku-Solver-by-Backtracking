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
    board = []
    print("Enter 9x9 Sudoku (separated by commas):")
for _ in range(9):
    row = [int(x) for x in input().strip().replace(',', ' ').split()]
    matrix.append(row)

    print(solves(board))
    pprint(board)
