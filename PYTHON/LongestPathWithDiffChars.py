class Solution:
# You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.
# You are also given a string s of length n, where s[i] is the character assigned to node i.
# Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.
    def longestPath(self, parent, s):
        trackMap = {}
        for i in range(0, len(parent)):
            list1 = trackMap.get(parent[i], [])
            list1.append(i)
            trackMap[parent[i]] = list1
        self.ans = 0
        self.dfsHelper(trackMap, s, 0)
        return self.ans


    def dfsHelper(self, trackMap, s, currentNode):
        subNodes = trackMap.get(currentNode, [])
        foundLength = [0] * len(subNodes)
        for i in range(len(subNodes)):
            subStringLength = self.dfsHelper(trackMap, s, subNodes[i])
            if s[subNodes[i]] != s[currentNode]:
                foundLength[i] = subStringLength
        foundLength.sort(reverse=True)
        longestSubstring = 0
        secondLongestSubstring = 0
        if len(subNodes) > 0:
            longestSubstring = foundLength[0]
        if len(subNodes) > 1:
            secondLongestSubstring = foundLength[1]
        self.ans = max(self.ans, longestSubstring + secondLongestSubstring + 1)
        return max(longestSubstring, secondLongestSubstring) + 1 
 
if __name__ == "__main__":
    test = Solution()
    print(test.longestPath([-1,0,1], "aab"))

    def longestPathBruteForce(self, parent, s):
        trackMap = {}
        for i in range(1, len(parent)):
            list1 = trackMap.get(parent[i], [])
            list2 = trackMap.get(i, [])
            list1.append(i)
            list2.append(parent[i])
            trackMap[parent[i]] = list1
            trackMap[i] = list2
        maxCount = 1
        for startNode in trackMap:
            maxCount = max(maxCount, self.dfsHelperBruteForce(trackMap, startNode, s, 0, -1))
        return maxCount


    def dfsHelperBruteForce(self, trackMap, startNode, s, currentCount, parentNode):
        if parentNode == -1 or s[startNode] != s[parentNode]:
            currentCount += 1
            possibleRoutes = trackMap[startNode]
            for route in possibleRoutes:
                if route == parentNode:
                    continue
                currentCount = max(currentCount, self.dfsHelperBruteForce(trackMap, route, s, currentCount, startNode))
        return currentCount

