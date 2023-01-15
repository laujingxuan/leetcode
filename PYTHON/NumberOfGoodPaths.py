# A good path is a simple path that satisfies the following conditions:
# The starting node and the ending node have the same value.
# All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's value should be the maximum value along the path).
class Solution:
    #non ideal as time limit exceeded for certain test cases. Time complexity potential of O(N!)
    def numberOfGoodPathsNonIdeal(self, val, edges):
        edgesMap = {}
        for i in range(len(edges)):
            list1 = edgesMap.get(edges[i][0], [])
            list2 = edgesMap.get(edges[i][1], [])
            list1.append(edges[i][1])
            list2.append(edges[i][0])
            edgesMap[edges[i][0]] = list1
            edgesMap[edges[i][1]] = list2
        numberOfGoodPaths = 0
        for i in range(len(vals)):
            hasVisited = set()
            numberOfGoodPaths += self.dfsHelper(vals, hasVisited, edgesMap, i, vals[i])
        return numberOfGoodPaths - ((numberOfGoodPaths - len(vals))//2)

    def dfsHelper(self, vals, hasVisited, edgesMap, currentInd, target):
        if currentInd not in hasVisited:
            hasVisited.add(currentInd)
            connectedNodes = edgesMap.get(currentInd, [])
            goodPaths = 0
            if vals[currentInd] == target:
                goodPaths += 1
            elif vals[currentInd] > target:
                return 0
            for i in range(len(connectedNodes)):
                goodPaths += self.dfsHelper(vals, hasVisited, edgesMap, connectedNodes[i], target)
            return goodPaths
        return 0

if __name__ == "__main__":
    test = Solution()
    vals = [1,3,2,1,3]
    edges = [[0,1],[0,2],[2,3],[2,4]]
    print(test.numberOfGoodPaths(vals, edges))
    