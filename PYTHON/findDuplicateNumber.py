# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

class Solution:
    #idea same as searching for cyclic linked list
    def findDuplicate(self, nums):
        if len(nums) > 1:
            slow = nums[0]
            fast = nums[nums[0]]
            print(str(slow) + ":" + str(fast))
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]
                print(str(slow) + ":" + str(fast))
            slow = 0
            print(str(slow) + "::" + str(fast))
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]
                print(str(slow) + "::" + str(fast))
            return slow
        return -1

if __name__ == "__main__":
    test= Solution()
    print(test.findDuplicate([1,3,4,2,2]))