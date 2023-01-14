class Solution:
    def spiralOrder(self, matrix):
        hasVisited = set()
        output = []
        checkList = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.spiralOrderHelper(matrix, hasVisited, 0, 0, output, checkList, 0)
        return output


    def spiralOrderHelper(self, matrix, hasVisited, row, column, output, checkList, checkListStartInd):
        key = str(row) + ":" + str(column)
        if row < 0 or column < 0 or row >= len(matrix) or column >= len(matrix[0]) or key in hasVisited:
            return
        output.append(matrix[row][column])
        hasVisited.add(key)
        for i in range(checkListStartInd, len(checkList)):
            self.spiralOrderHelper(matrix, hasVisited, row+checkList[i][0], column+checkList[i][1], output, checkList, i)

        for i in range(0,checkListStartInd):
            self.spiralOrderHelper(matrix, hasVisited, row+checkList[i][0], column+checkList[i][1], output, checkList, i)
        return

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