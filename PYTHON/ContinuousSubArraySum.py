class Solution:
    #time limit exceeded
    def checkSubarraySumBruteForce(self, nums, k):
        for i in range(len(nums)):
            tempSum = nums[i]
            for j in range(i+1, len(nums)):
                tempSum += nums[j]
                if tempSum%k == 0:
                    return True
        return False

    def checkSubarraySum(self, nums, k):
        #Basically is if we find a duplicate remainder in the accumulated sum array, it means that there's a part of subarray with sum%k==0
        #Two remainders the same means the sum of difference in between the two indexes are a multiple of k
        checkRemainder = {}
        checkRemainder[0] = -1
        currentSum = 0
        for i in range(len(nums)):
            currentSum += nums[i]
            remainder = currentSum%k
            if remainder in checkRemainder:
                if i - checkRemainder[remainder] > 1:
                    return True
            else:
                checkRemainder[remainder] = i
        return False

    #FInd the maximum subarray
    def findMaximumSubArray(self, nums):
        maxOverall = nums[0]
        maxSoFar = 0
        for i in range(len(nums)):
            maxSoFar += nums[i]
            if maxSoFar > maxOverall:
                maxOverall = maxSoFar
            if maxSoFar < 0:
                maxSoFar = 0
        return maxOverall