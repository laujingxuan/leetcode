#time complexity O(N^2)
def lengthOfLIS(nums):
    overallMax = 1
    memo = [1] * len(nums)
    for i in range(len(nums)-1, -1, -1):
        for j in range(i, len(nums)):
            if nums[i] < nums[j] and memo[i] < memo[j] + 1:
                memo[i] = memo[j] + 1
        overallMax = max(overallMax, memo[i])
    return overallMax

#same idea but from the front
def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)

#O(N * logN) time complexity
# def lengthOfLISGreedyBest(self, nums: List[int]) -> int:
#     sub = []
#     for x in nums:
#         if len(sub) == 0 or sub[-1] < x:
#             sub.append(x)
#         else:
#             idx = bisect_left(sub, x)  # Find the index of the first element >= x (Need to code the binary search out)
#             sub[idx] = x  # Replace that number with x
#     return len(sub)

if __name__ == "__main__":
    print(lengthOfLIS([0,1,0,3,2,3]))