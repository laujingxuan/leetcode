# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.

import random


class Solution:
    #time complexity O(NlogN) since we sort the whole array
    def findKthLargestSelect(self, nums, k):
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)

    def quickSelect(self, nums, low, high, desiredIndex):
        if high > low:
            pivot = self.partition(nums, low, high)
            if pivot == desiredIndex:
                return nums[pivot]
            if pivot > desiredIndex:
                return self.quickSelect(nums, low, pivot - 1, desiredIndex)
            else:
                return self.quickSelect(nums, pivot + 1, high, desiredIndex)
        return nums[high]


    def findKthLargestSortAll(self, nums, k):
        self.quickSort(nums, 0, len(nums) - 1)
        return nums[len(nums) - k]

    def partition(self, nums, low, high):
        pivot = random.randrange(low, high+1)
        nums[pivot], nums[high] = nums[high], nums[pivot]
        pivotNumber = nums[high]
        index = low
        for i in range(low, high):
            if nums[i] <= pivotNumber:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        nums[index], nums[high] = nums[high], nums[index]
        return index

    def quickSort(self, nums, low, high):
        if high > low:
            pivot = self.partition(nums, low, high)
            self.quickSort(nums, low, pivot - 1)
            self.quickSort(nums, pivot + 1, high)
        return


if __name__ == "__main__":
    test = Solution()
    print(test.findKthLargestSelect([3,2,1,5,6,4], 2))
    # print(test.findKthLargestSortAll([3,2,1,5,6,4], 2))