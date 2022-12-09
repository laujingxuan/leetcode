# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

class Solution:
    def orangesRotting(self, grid):
        queue = []
        numberOfFreshOranges = 0
        listArray = [[0,1], [0,-1], [1,0], [-1, 0]]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    for z in range(len(listArray)):
                        queue.append([i + listArray[z][0], j + listArray[z][1]])
                elif grid[i][j] == 1:
                    numberOfFreshOranges += 1
        minsNeeded = 0
        if numberOfFreshOranges == 0:
            return 0
        while len(queue) != 0:
            for i in range(len(queue)):
                current = queue.pop(0)
                if current[0] < 0 or current[0] >= len(grid) or current[1] < 0 or current[1] >= len(grid[0]) or grid[current[0]][current[1]] != 1:
                    continue
                grid[current[0]][current[1]] = 2
                numberOfFreshOranges -= 1
                for z in range(len(listArray)):
                    queue.append([current[0] + listArray[z][0], current[1] + listArray[z][1]])
            minsNeeded += 1
        if numberOfFreshOranges != 0:
            return -1
        return minsNeeded - 1

class Alternate:
    def orangesRottinAlternateMoreDirty(self, grid):
        queue = []
        listArray = [[0,1], [0,-1], [1,0], [-1, 0]]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    for z in range(len(listArray)):
                        if i + listArray[z][0] >= 0 and i + listArray[z][0] < len(grid) and j + listArray[z][1] >= 0 and j + listArray[z][1] < len(grid[i]) and grid[i + listArray[z][0]][j + listArray[z][1]] == 1:
                            queue.append([i + listArray[z][0], j + listArray[z][1]])
        minsNeeded = 0

        while len(queue) > 0:
            isAdded = False
            for i in range(len(queue)):
                current = queue.pop(0)
                if grid[current[0]][current[1]] == 1:
                    grid[current[0]][current[1]] = 2
                    if not isAdded:
                        minsNeeded += 1
                        isAdded= True
                for z in range(len(listArray)):
                        if current[0] + listArray[z][0] >= 0 and current[0] + listArray[z][0] < len(grid) and current[1] + listArray[z][1] >= 0 and current[1] + listArray[z][1] < len(grid[0]) and grid[current[0] + listArray[z][0]][current[1] + listArray[z][1]] == 1:
                            queue.append([current[0] + listArray[z][0], current[1] + listArray[z][1]])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        return minsNeeded

if __name__ == "__main__":
    test = Solution()
    test1 = Alternate()
    print(test.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
    print(test1.orangesRottinAlternateMoreDirty([[2,1,1],[1,1,0],[0,1,1]]))
    # print(test.orangesRotting([[1],[2]]))