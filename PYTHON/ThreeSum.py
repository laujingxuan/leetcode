class Solution:
    def threeSumClosest(self, nums, target):
        if len(nums) <3:
            return -1
        nums.sort()
        closestSum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            firstIndex = i + 1
            secondIndex = len(nums) - 1
            while secondIndex > firstIndex:
                print(str(nums[i]) + ":" + str(nums[firstIndex]) + ":" + str(nums[secondIndex]))
                currentSum = nums[firstIndex] + nums[secondIndex] + nums[i]
                if abs(currentSum - target) - abs(closestSum - target) < 0:
                    closestSum = currentSum
                if currentSum > target:
                    secondIndex -= 1
                else:
                    firstIndex += 1
        return closestSum

if __name__ == "__main__":
    test = Solution()
    print(test.threeSumClosest([-1,2,1,-4], 1))