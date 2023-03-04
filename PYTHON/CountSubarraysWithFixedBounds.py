# You are given an integer array nums and two integers minK and maxK.

# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.

# A subarray is a contiguous part of an array.

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        index = 0
        badIndex = -1
        minKIndex = -1
        maxKIndex = -1
        output = 0
        while index < len(nums):
            if nums[index] == minK:
                minKIndex = index
            if nums[index] == maxK:
                maxKIndex = index
            if nums[index] < minK or nums[index] > maxK:
                badIndex = index
            # This statement computes the number of valid subarrays that end at the current index i and adds it to the total count. The number of valid subarrays is equal to the number of subarrays whose minimum and maximum elements are both in the range [minK, maxK].
            output += max(0, min(minKIndex, maxKIndex) - badIndex)
            index += 1
        return output

    def countSubarraysTimeLimitExceeded(self, nums: List[int], minK: int, maxK: int) -> int:
        totalCount = 0
        trackSet = set()
        for i in range(len(nums)):
            totalCount += self.helper(nums, minK, maxK, i, trackSet)
        return totalCount

    def helper(self, nums, minK, maxK, currentIndex, currentSet):
        if currentIndex == len(nums) or nums[currentIndex] < minK or nums[currentIndex] > maxK:
            return 0
        currentSet.add(nums[currentIndex])
        count = 0
        if minK in currentSet and maxK in currentSet:
            count += 1
        count += self.helper(nums, minK, maxK, currentIndex + 1, currentSet)
        currentSet.discard(nums[currentIndex])
        return count