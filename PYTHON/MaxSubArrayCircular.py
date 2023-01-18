class Solution:
    def maxSubarraySumCircular(self, nums):
        maxOverall = nums[0]
        maxSoFar = 0
        total = 0
        minOverall = nums[0]
        minSoFar = 0
        #find maximum subarray, min subarray and total
        for i in range(len(nums)):
            minSoFar += nums[i]
            maxSoFar += nums[i]
            total += nums[i]
            if maxSoFar > maxOverall:
                maxOverall = maxSoFar
            if maxSoFar < 0:
                maxSoFar = 0
            if minSoFar < minOverall:
                minOverall = minSoFar
            if minSoFar > 0:
                minSoFar = 0
        #For the case where all the values is negative, then total-minOverall will be 0 which stands for empty array being selected. Hence invalid
        if maxOverall > 0:
            return max(total-minOverall, maxOverall)
        return maxOverall