# Given an integer array nums, find a  subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
class Solution:
    def maxProduct(self, nums):
        overallMax = nums[0]
        tempMin = nums[0]
        tempMax = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                # multiplied by a negative makes big number smaller, small number bigger
                # so we redefine the extremums by swapping them
                tempMin, tempMax = tempMax, tempMin
            tempMax = max(nums[i], tempMax * nums[i])
            tempMin = min(nums[i], tempMin * nums[i])
            # multiplied by a negative makes big number smaller, small number bigger
            # so we redefine the extremums by swapping them
            overallMax = max(overallMax, tempMax)
        return overallMax

    def alternateMaxProduct(self, nums):
        B = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            B[i] *= B[i - 1] or 1
        print(nums)
        print(B)
        return max(nums + B)


if __name__ == "__main__":
    test = Solution()
    # print(test.maxProduct([2,3,-2,4]))
    print(test.alternateMaxProduct([2,3,-2, 0, 4]))
    # print(test.alternateMaxProduct([0,0,0,0]))