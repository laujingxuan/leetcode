class Solution:
    # Actually, this is a 0/1 knapsack problem, for each number, we can pick it or not. Let us assume dp[i][j] means whether the specific sum j can be gotten from the first i numbers. If we can pick such a series of numbers from 0-i whose sum is j, dp[i][j] is true, otherwise it is false.
    def canPartitionKnapSack(self, nums):
        total = 0
        for num in nums:
            total += num
        if total%2 == 1:
            return False
        halfTotal = total//2
        
        memo = [[False for i in range(halfTotal + 1)] for j in range(len(nums) + 1)]
        memo[0][0] = True
        for i in range(1, len(memo)):
            for j in range(1, len(memo[i])):
                if j < nums[i - 1]:
                    memo[i][j] = memo[i - 1][j]
                else:
                    memo[i][j] = memo[i-1][j-nums[i - 1]] or memo[i-1][j]
        return memo[len(nums)][halfTotal]


    #2^n time complexity since possible to include and not include for every elements, hence non ideal
    def canPartitionDFS(self, nums):
        total = 0
        for num in nums:
            total += num
        if total%2 == 1:
            return False
        halfTotal = total//2
        return self.backTrackFindSum(nums, halfTotal, 0)

    def backTrackFindSum(self, nums, total, startIndex):
        if total == 0:
            return True
        if total < 0 or startIndex >= len(nums):
            return False
        return self.backTrackFindSum(nums, total - nums[startIndex], startIndex + 1) or self.backTrackFindSum(nums, total, startIndex + 1)
        #for i in range(startIndex, len(nums) - 1):
        #    isFound = self.backTrackFindSum(nums, total-nums[i], i + 1)
        #    if isFound:
        #        return True
        # return False