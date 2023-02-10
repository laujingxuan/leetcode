from dis import dis


class Solution:
# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.
# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

    def maxDistanceIdealBFS(self, grid):
        rowLen, colLen = len(grid), len(grid[0])
        paths = [[0,1], [0,-1], [1,0], [-1,0]]
        queue = []
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 1:
                    queue.append([i, j])
        if len(queue) == 0 or len(queue) == rowLen * colLen:
            return -1
        level = 0
        while len(queue) > 0:
            queueLen = len(queue)
            for z in range(queueLen):
                coord = queue.pop(0)
                for path in paths:
                    newRow = coord[0] + path[0]
                    newCol = coord[1] + path[1]
                    if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0]) or grid[newRow][newCol] == 1:
                        continue
                    queue.append([newRow,newCol])
                    grid[newRow][newCol] = 1
            level += 1
        return level-1
    
    #improvements can be made as we dont need to do BFS for each cell actually
    def maxDistanceNonIdealBFS(self, grid):
        paths = [[0,1], [0,-1], [1,0], [-1,0]]
        longestDist = -1
        allLand = True
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    allLand = False
                queue = []
                queue.append([i, j])
                distance = 0
                isFound = False
                hasVisited = set()
                while len(queue) > 0:
                    queueLen = len(queue)
                    for z in range(queueLen):
                        coord = queue.pop(0)
                        row = coord[0]
                        col = coord[1]
                        key = str(row) + ":" + str(col)
                        hasVisited.add(key)
                        if grid[row][col] == 1:
                            isFound = True
                            break
                        for path in paths:
                            key =  str(row + path[0]) + ":" + str(col + path[1])
                            if row + path[0] < 0 or row + path[0] >= len(grid) or col + path[1] < 0 or col + path[1] >= len(grid[row]) or key in hasVisited:
                                continue
                            queue.append([row+path[0], col+path[1]])
                    if isFound:
                        break
                    distance += 1
                if isFound:
                    longestDist = max(longestDist, distance)
        if allLand:
            return -1
        return longestDist


    #DFS is not suitable for this case. Should use BFS. Time complexity is O(row*colum*(row+column))? Since you might need to traverse the whole matrix for each cell
    def maxDistanceWithDFS(self, grid):
        maxShortestDist = -1
        memo = [[-1 for j in range(len(grid[0]))] for i in range(len(grid))]
        allLand = True
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 0:
                    allLand = False
                memo[row][column] = self.maxDistanceHelper(grid, row, column, memo)
                maxShortestDist = max(maxShortestDist, memo[row][column])
        if allLand:
            return -1
        return maxShortestDist
    
    def maxDistanceHelper(self, grid, row, column, memo):
        if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[row]) or grid[row][column] == 2:
            return -1
        if grid[row][column] == 1:
            memo[row][column] = 0
            return 0
        if memo[row][column] != -1:
            return memo[row][column]

        paths = [[1,0], [-1,0], [0,1], [0,-1]]
        minDistance = -1
        grid[row][column] = 2
        for path in paths:      
            distance = self.maxDistanceHelper(grid, row + path[0], column + path[1], memo)
            if distance != -1:
                if minDistance == -1:
                    minDistance = distance + 1
                    continue
                minDistance = min(minDistance, distance + 1)
        grid[row][column] = 0
        return minDistance

if __name__ == "__main__":
    grid = [[1,0,0],[0,0,0],[0,0,0]]
    test = Solution()
    print(test.maxDistanceIdealBFS(grid))