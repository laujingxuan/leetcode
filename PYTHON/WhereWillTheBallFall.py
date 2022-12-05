#1706. Where Will the Ball Fall
class Solution:
    # idea: we can simulate the movement of each ball
    # if a ball is stuck at some point, then it would be -1
    # otherwise, get the final destination column
    def findBallBetterTidier(self, grid):
        m, n = len(grid), len(grid[0])
        ans = []
        # iterate each column
        for col in range(n):
            cur_col = col
            # iterate each row
            for cur_row in range(m):
                # the next column would be the current column + the value of the current cell
                # e.g. column 0 + 1 = column 1 (move to the right)
                # e.g. column 3 - 1 = column 2 (move to the left)
                next_col = cur_col + grid[cur_row][cur_col]
                # after that we need to check if the ball gets stuck at the same column
                # and there are three cases
                # 1. the ball on the leftmost column is moving to the left
                # hence, we check `next_col < 0`
                # 2. the ball on the rightmost column is moving to the right
                # hence, we check `next_col >= n`
                # 3. the ball is stuck at a V shape position
                # e.g. ball 2 and ball 3 in column 2 and column 3 in row 0
                # hence, we check if the if grid[cur_row][cur_col] is different than grid[cur_row][next_col]
                if next_col < 0 or next_col >= n or grid[cur_row][cur_col] ^ grid[cur_row][next_col]:
                    # the ball is stuck at some point, which means it couldn't reach to the end
                    # hence, we can set -1 and break here
                    cur_col = -1
                    break
                # continue the above process with the updated cur_col
                cur_col = next_col
            # the ball reaches to the end,
            # cur_col is the final destination
            ans.append(cur_col)
        return ans

    #own solution where i computer the whole reachable path first
    def findBall(self, grid):
        if len(grid[0]) == 1:
            return [-1]
        memo = [[1 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if j == 0:
                    if grid[i][j] == -1:
                        memo[i][j] = -1
                    continue
                if j == len(grid[i]) - 1 and grid[i][j] == 1:
                    memo[i][j] = -1
                    continue
                if grid[i][j] == -1 and grid[i][j-1] == 1:
                    memo[i][j] = -1
                    memo[i][j-1] = -1
        output = []
        print(memo)
        for i in range(len(grid[0])):
            row = 0
            column = i
            while row < len(grid) and column < len(grid[0]) and column >= 0:
                # if i == 4:
                #     print("row: " + str(row))
                #     print("column: " + str(column))
                if memo[row][column] == -1:
                    break
                column += grid[row][column]
                row += 1
                # if i == 4:
                #     print("row: " + str(row))
                #     print("column: " + str(column))
            if row == len(grid):
                output.append(column)
            else:
                output.append(-1)
        return output

if __name__ == "__main__":
    test = Solution()
    # print(test.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
    # print(test.findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))
    print(test.findBall([[1]]))