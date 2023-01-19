# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.


class Solution:
    def subarraySum(self, nums, k) :
        if len(nums) == 0:
            return 0

        prefixSum = 0
        checkMap = {}
        checkMap[0] = 1
        count = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            count += checkMap.get(prefixSum - k, 0)
            if prefixSum in checkMap:
                checkMap[prefixSum] += 1
            else:
                checkMap[prefixSum] = 1
        return count

if __name__ == "__main__":
    test = Solution()
    print(test.subarraySum([1,1,1], 2))

        