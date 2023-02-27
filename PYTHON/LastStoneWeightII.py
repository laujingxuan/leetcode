# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the smallest possible weight of the left stone. If there are no stones left, return 0.
from __future__ import nested_scopes


class Solution:
    def lastStoneWeightII(self, stones):
        total = sum(stones)
        half = total//2
        nearestToHalf = 0
        #knapsack problem
        memo = [[False for i in range(len(stones) + 1)] for j in range(half + 1)]
        for value in range(len(memo[0])):
            memo[0][value] = True
        for capacity in range(1, half + 1):
            for value in range(1, len(stones) + 1):
            # for capacity in range(1, half + 1):
                # print(capacity - stones[value - 1])
                # print(memo)
                if memo[capacity][value - 1] or (capacity >= stones[value - 1] and memo[capacity - stones[value - 1]][value-1]):
                    nearestToHalf = capacity
                    memo[capacity][value] = True
        # print(total)
        # print(nearestToHalf)
        return abs(total - 2*nearestToHalf)

if __name__ == "__main__":
    test = Solution()
    print(test.lastStoneWeightII([2,7,4,1,8,1]))
    print(test.lastStoneWeightII([31,26,33,21,40]))
    print(test.lastStoneWeightII([1,2]))
