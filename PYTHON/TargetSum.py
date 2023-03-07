# class Solution:
#     def findTargetSumWays(self, nums, target):
#         if len(nums) == 1:
#             if abs(nums[0]) == abs(target):
#                 return 1
#             return 0
#         #divide nums into two sets and the difference between the two sets should be target
#         total = sum(nums)
#         if (total - target)%2 != 0:
#             return 0
#         positiveSum = (total - target)//2 + target
#         memo = [[-1 for i in range(len(nums) + 1)] for j in range(positiveSum + 1)]
#         totalCount = 0
#         for capacity in range(len(memo)):
#             memo[capacity][0] = 0
#         for value in range(len(memo[0])):
#             memo[0][value] = 0
#         for capacity in range(len(memo)):
#             for value in range(1, len(memo[capacity])):
#                 # print(str(capacity) + ":" + str(value))
#                 if (capacity >= nums[value - 1] and memo[capacity - nums[value - 1]][value - 1] >= 0):
#                     memo[capacity][value] = memo[capacity - nums[value - 1]][value - 1] + 1
#                     if capacity == positiveSum:
#                         totalCount += memo[capacity][value]
#         # print(memo)
#         return totalCount

# if __name__ == "__main__":
#     test = Solution()
#     print(test.findTargetSumWays([1,0], 1))