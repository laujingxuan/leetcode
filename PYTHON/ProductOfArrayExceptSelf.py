# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

#Prefix, Suffix method
class Solution:
    def productExceptSelf(self, nums):
        output = [1 for i in range(len(nums))]
        pre = 1
        post = 1
        for i in range(len(nums)):
            output[i] *= pre
            pre *= nums[i]
            output[len(nums) - i - 1] *= post
            post *= nums[len(nums) - i - 1]
        return output
