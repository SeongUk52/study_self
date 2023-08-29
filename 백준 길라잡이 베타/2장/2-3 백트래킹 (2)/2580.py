def isValid(row,col,board,num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    srow,scol = 3*(row//3),3*(col//3)
    for i in range(3):
        for j in range(3):
            if board[srow+i][scol+j] == num:
                return False
    return True


def bt(board):
    empty = findempty(board)
    if not empty:
        return True
    row,col = empty
    for i in range(1,10):
        if isValid(row,col,board,i):
            board[row][col] = i
            if bt(board):
                return True
            board[row][col] = 0
    return False




def findempty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i,j
    return None
sudoku = [list(map(int,input().split())) for _ in range(9)]

bt(sudoku)
for i in sudoku:
    print(*i)
