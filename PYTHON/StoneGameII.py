import math


class Solution:
    def stoneGameII(self, piles):
        sumList = self._suffix_sum(piles)
        dp = [[0 for i in range(len(piles))] for j in range(len(piles))]
        return self.dfs(piles, sumList, 0, 1, dp)

    def dfs(self, piles, suffixSum, index, m, dp):
        if index >= len(piles):
            return 0
        if m < len(piles) and dp[index][m] != 0:
            return dp[index][m]
        mRange = 2 * m
        nextPlayerSum = suffixSum[index]
        #calculate the sum for next player
        #when current pile is 0, the pile that can be taken by the next player is 1 and 2 (since m = 1 and 2m = 2)
        # for nextPile in range(index + 1, min(len(piles) - 1, index + mRange + 1)):
        for nextPile in range(index + 1, index + mRange + 1):
            newM = max(m, nextPile - index)
            nextPlayerSum = min(nextPlayerSum, self.dfs(piles, suffixSum, nextPile, newM, dp))
        currentPlayerSum = suffixSum[index] - nextPlayerSum
        if m < len(piles):
            dp[index][m] = currentPlayerSum
        return currentPlayerSum

    def _suffix_sum(self, piles):
        reverse = [0] * (len(piles) + 1)
        for i in range(len(piles) - 1, -1, -1):
            reverse[i] = piles[i] + reverse[i + 1]
        return reverse

if __name__ == "__main__":
    test = Solution()
    # input = [2,7,9,4,4]
    input = [1]
    print(test.stoneGameII(input))