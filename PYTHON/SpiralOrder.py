class Solution:
    def spiralOrder(self, matrix):
        output = []
        output.append(matrix[0][0])
        hasVisited = set()
        hasVisited.add(str(0) + ":" + str(0))
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        currentDirectionIndex = 0
        row = 0
        column = 0
        while True:
            currentDirection = directions[currentDirectionIndex]
            row, column = self.spiralOrderHelper(matrix, hasVisited, row + currentDirection[0], column + currentDirection[1], output, currentDirection)
            if len(hasVisited) == len(matrix)*len(matrix[0]):
                break
            if currentDirectionIndex == 3:
                currentDirectionIndex = 0
            else:
                currentDirectionIndex += 1
        return output

    def spiralOrderHelper(self, matrix, hasVisited, row, column, output, currentDirection):
        while row >= 0 and column >= 0 and row < len(matrix) and column < len(matrix[0]):
            key = str(row) + ":" + str(column)
            if key in hasVisited:
                break
            hasVisited.add(key)
            output.append(matrix[row][column])
            row = row + currentDirection[0]
            column = column + currentDirection[1]
        return row - currentDirection[0], column - currentDirection[1]

    def spiralOrderAlternateSolution(self, matrix):
        res = []
        if len(matrix) == 0:
            return res
        row_begin = 0
        col_begin = 0
        row_end = len(matrix)-1 
        col_end = len(matrix[0])-1
        while (row_begin <= row_end and col_begin <= col_end):
            for i in range(col_begin,col_end+1):
                res.append(matrix[row_begin][i])
            row_begin += 1
            for i in range(row_begin,row_end+1):
                res.append(matrix[i][col_end])
            col_end -= 1
            if (row_begin <= row_end):
                for i in range(col_end,col_begin-1,-1):
                    res.append(matrix[row_end][i])
                row_end -= 1
            if (col_begin <= col_end):
                for i in range(row_end,row_begin-1,-1):
                    res.append(matrix[i][col_begin])
                col_begin += 1
        return res

if __name__ == "__main__":
    test = Solution()
    # print(test.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(test.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))