# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

class Solution:
    #Should be O(N) time complexity (possibly loop through the matrix twice and third time is looping through the keys) and O(N) space complexity
    def pacificAtlantic(self, heights):
        # Get all the higher sea level of top and left
        topLeftPath = {}
        for i in range(len(heights)):
            self.seaHelper(heights, i, 0, topLeftPath)
        for i in range(len(heights[i])):
            self.seaHelper(heights, 0, i, topLeftPath)
        # Get all the higher sea level of bottom and right
        bottomRightPath = {}
        for i in range(len(heights)):
            self.seaHelper(heights, i, len(heights[0]) - 1, bottomRightPath)
        for i in range(len(heights[0])):
            self.seaHelper(heights, len(heights) - 1, i, bottomRightPath)
        # Find the intersection of topleft and bottomright
        output = []
        for key in topLeftPath:
            if key in bottomRightPath:
                output.append(topLeftPath[key])
        return output

    def seaHelper(self, heights, initRow, initColumn, pathMap):
        if initRow < 0 or initColumn < 0 or initRow >= len(heights) or initColumn >= len(heights[initRow]):
            return False
        queue = []
        checkList = [[0,1], [0, -1], [1,0], [-1, 0]]
        queue.append([initRow,initColumn])
        while len(queue) > 0:
            point = queue.pop(0)
            row = point[0]
            column = point[1]
            key = str(row) + ":" + str(column)
            if key in pathMap:
                continue
            if row < 0 or column < 0 or row >= len(heights) or column >= len(heights[initRow]):
                continue
            pathMap[key] = [row, column]
            for current in checkList:
                print("row: " + str(row) + ":" + str(current[0]))
                print("column: " + str(column) + ":" + str(current[1]))
                if row + current[0] < 0 or column + current[1] < 0 or row + current[0] >= len(heights) or column + current[1] >= len(heights[0]) or heights[row + current[0]][column + current[1]] < heights[row][column]:
                    continue
                queue.append([row + current[0], column + current[1]])
        return pathMap

if __name__ == "__main__":
    test = Solution()
    # print(test.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
    # print(test.pacificAtlantic([[1]]))
    print(test.pacificAtlantic([[1,1],[1,1],[1,1]]))
                