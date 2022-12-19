class Solution:
    #store states of each row in the first of that row, and store states of each column in the first of that column. 
    # ecause the state of row0 and the state of column0 occupy the same cell, so use another variable col0 to separate them
    def setZeroesTimeNSquare(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[0])-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0
        
        return matrix

    #Might not be too ideal as time complexity can be O(N^3) when all elements are 0
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    self.setZeroesHelpers(matrix, i, j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == None:
                    matrix[i][j] = 0

    def setZeroesHelpers(self, matrix, row, column):
        for i in range(len(matrix)):
            if matrix[i][column] != 0:
                matrix[i][column] = None
        for j in range(len(matrix[0])):
            if matrix[row][j] != 0:
                matrix[row][j] = None
        return

