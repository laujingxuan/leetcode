class Solution:

    # only O(m+n) time complexity
    # idea: We start search the matrix from top right corner, initialize the current position to top right corner, if the target is greater than the value in current position, then the target can not be in entire row of current position because the row is sorted, if the target is less than the value in current position, then the target can not in the entire column because the column is sorted too. 
    def searchMatrix(self, matrix, target):
        row = 0
        column = len(matrix[0]) - 1
        while row < len(matrix) and column >= 0:
            if matrix[row][column] == target:
                return True
            if matrix[row][column] > target:
                column -= 1
            else:
                row += 1
        return False

    def searchMatrixNotIdealWithBinary(self, matrix, target):
        for i in range(len(matrix)):
            if matrix[i][0] == target:
                return True
            if matrix[i][0]>target:
                break
            if self.binarySearchRow(matrix, i, target):
                return True
        return False
        
    def binarySearchRow(self, matrix, row, target):
        startIndex = 0
        lastIndex = len(matrix[row]) - 1
        while lastIndex >= startIndex:
            midIndex = (startIndex + lastIndex)//2
            if matrix[row][midIndex] == target:
                return True
            if matrix[row][midIndex] > target:
                lastIndex = midIndex - 1
            else:
                startIndex = midIndex + 1
        return False
