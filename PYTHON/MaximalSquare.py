class Solution:
    def maximalSquare(self, matrix):
        memo = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
        maxSquareLen = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    memo[i + 1][j + 1] = min(memo[i][j], memo[i+1][j], memo[i][j+1]) + 1
                    maxSquareLen = max(maxSquareLen, memo[i+1][j+1])
        return maxSquareLen*maxSquareLen