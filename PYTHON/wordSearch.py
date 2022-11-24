#Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
def exist(board, word):
    for i in range (len(board)):
        for j in range(len(board[i])):
            if existHelper(board, word, i, j, 0):
                return True
    return False

# add a hash with row and column string as key?
def existHelper(board, word, row, column, wordIndex):
    if wordIndex == len(word):
        return True
    if row<0 or column<0 or row>=len(board) or column>=len(board[row]) or board[row][column] != word[wordIndex]:
        return False
    temp = board[row][column]
    board[row][column] = "*"
    checkHelper = [[0,-1], [0,1], [1,0], [-1,0]]
    for check in checkHelper:
        found = existHelper(board, word, row + check[0], column + check[1], wordIndex + 1)
        if found:
            return True
    board[row][column] = temp
    return False

if __name__ == "__main__":
    print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCG"))
    print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
    print(exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))
