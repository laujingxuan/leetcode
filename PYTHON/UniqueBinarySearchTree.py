# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
class Solution:
    def numTreesWithDP(self, n: int) -> int:
        memo = [-1 for i in range(n)]
        return self.helperWithDP(0, n - 1, memo)


    def helperWithDP(self, start, end, memo):
        if start >= end:
            return 1
        if memo[end - start] != -1:
            return memo[end-start]
        total = 0
        for i in range(start, end+1):
            left = self.helperWithDP(start, i - 1, memo)
            right = self.helperWithDP(i + 1, end, memo)
            total += left*right
        
        memo[end-start] = total
        return total


    def numTreesCleanerBestSolution(self, n: int) -> int:
        # https://leetcode.com/problems/unique-binary-search-trees/solutions/31666/dp-solution-in-6-lines-with-explanation-f-i-n-g-i-1-g-n-i/
        memo = [0 for i in range(n + 1)]
        memo[0] = 1
        memo[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                memo[i] += memo[j - 1] * memo[i - j]

        return memo[n]



    def numTreesTimeLimitExceeded(self, n: int) -> int:
        return self.helper(0, n - 1)


    def helper(self, start, end):
        if start >= end:
            return 1
        if end - start == 1:
            return 2
        total = 0
        for i in range(start, end+1):
            left = self.helper(start, i - 1)
            right = self.helper(i + 1, end)
            total += left*right
        
        return total