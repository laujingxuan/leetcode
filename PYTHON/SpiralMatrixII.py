# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
class Solution:
    def generateMatrix(self, n):
        matrix = [[0 for i in range(n)] for j in range(n)]
        paths = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.helper(matrix, 0, 0, paths, 1)
        return matrix

    def helper(self, matrix, row, column, paths, currentVal):
        if row < 0 or column < 0 or row >= len(matrix) or column >= len(matrix[row]) or matrix[row][column] != 0:
            return
        matrix[row][column] = currentVal
        for i in range(len(paths)):
            self.helper(matrix, row + paths[i][0], column + paths[i][1], paths[i:] + paths[:i], currentVal + 1)
        return
    
    def generateMatrixAlternateSolution(self, n):
        matrix = [[0] * n for _ in range(n)]
        x, y, dx, dy = 0, 0, 1, 0
        for i in range(n*n):
            matrix[y][x] = i + 1
            if not 0 <= x + dx < n or not 0 <= y + dy < n or matrix[y+dy][x+dx] != 0:
                dx, dy = -dy, dx
            x, y = x + dx, y + dy
        return matrix