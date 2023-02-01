class Solution:
# Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
# You may assume the input array always has a valid answer.
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if i%2==1 and nums[i]<nums[i-1] or i%2==0 and nums[i]>nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]


# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
# You may assume the input array always has a valid answer.
# Non ideal as ideal solution is with average O(N) time and O(1) space
    def wiggleSortII(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        newList = nums[:]
        currentIndex = 0
        for i in range(1, len(newList), 2):
            nums[i] = newList[currentIndex]
            currentIndex += 1

        for i in range(0, len(newList), 2):
            nums[i] = newList[currentIndex]
            currentIndex += 1
        return