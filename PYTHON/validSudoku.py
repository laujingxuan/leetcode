def isValidSudoku(board) -> bool:
    for i in range(len(board)):
        rowCheckSet = set()
        columnCheckSet = set()
        blockSet = set()
        for j in range(len(board[i])):
            if board[i][j] != "." and board[i][j] in rowCheckSet:
                return False
            if board[j][i] != "." and board[j][i] in columnCheckSet:
                return False
            row = 3*(i//3)
            column = 3*(i%3)
            if board[row + j//3][column + j%3] != "." and board[row + j//3][column + j%3] in blockSet:
                return False
            rowCheckSet.add(board[i][j])
            columnCheckSet.add(board[j][i])
            blockSet.add(board[row + j//3][column + j%3])
    return True

if __name__ == '__main__':
    print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))