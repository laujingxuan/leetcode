# Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.
# Implement the Solution class:
# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.
import random


class Solution:
    # def __init__(self, nums):
    #     memo = []
    #     self.generateHelper(nums, [], memo)
    #     self.memo = memo

    # correct way of generating permutation but the time complexity is O(N!). 
    # since we dont need to really generate every possible permutation out. there is a more efficient way
    # def generateHelper(self, nums, currentCombi, memo):
    #     if len(nums) == 0:
    #         memo.append(currentCombi[:])
    #         return
    #     for i in range(len(nums)):
    #         currentCombi.append(nums[i])
    #         self.generateHelper(nums[:i] + nums[i+1:], currentCombi, memo)
    #         currentCombi.remove(nums[i])
    #     return

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums
        
    def shuffle(self):
        output = self.nums[:]
        for i in range(len(self.nums)):
            iVal = random.randrange(i, len(self.nums))
            output[i], output[iVal] = output[iVal], output[i]
        return output


if __name__ == "__main__":
    test = Solution([1,2,3,4,5,6,7,8,9,10,11,12])
    print(test.reset())
    for i in range(5):
        print(test.shuffle())