import math


class Solution:
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False
        small = math.inf
        big = math.inf
        for i in range(len(nums)):
            if nums[i] <= small:
                small = nums[i]
            elif nums[i] <= big:
                big = nums[i]
            else:
                return True
        return False
        