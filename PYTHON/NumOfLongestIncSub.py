# Given an integer array nums, return the number of longest increasing subsequences.
# Notice that the sequence has to be strictly increasing.
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
def findNumberOfLIS(nums):
    memoLen = [1] * len(nums)
    memoCount = [1] * len(nums)
    maxLen = 0
    res = 0
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                if memoLen[i] == memoLen[j] + 1:
                    memoCount[i] += memoCount[j]
                if memoLen[j] + 1 > memoLen[i]:
                    memoLen[i] = memoLen[j] + 1
                    memoCount[i] = memoCount[j]
        if maxLen ==memoLen[i]:
            res += memoCount[i]
        if maxLen < memoLen[i]:
            maxLen = memoLen[i]
            res = memoCount[i]
    print(memoLen)
    print(memoCount)
    return res




if __name__ == "__main__":
    print(findNumberOfLIS([1,3,5,4,7]))
    print(findNumberOfLIS([1,1,1,2,2,2,3,3,3]))