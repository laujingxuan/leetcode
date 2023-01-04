class Solution:
    def generate(self, numRows):
        output = [[1]]
        for i in range(1, numRows):
            upperRow = output[-1]
            currentRow = [1]
            for j in range(1,i):
                currentRow.append(upperRow[j-1] + upperRow[j])
            currentRow.append(1)
            output.append(currentRow)
        return output