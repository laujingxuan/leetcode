#dynamic programming solution but has max stack error
def canJump(nums):
    memo=[True] * (len(nums) + 1)
    return canJumpHelper(nums, 0, memo)

def canJumpHelper(nums, currentIndex, memo):
    if currentIndex == len(nums)-1:
        return True
    if currentIndex >= len(nums) or memo[currentIndex] != True:
        return False
    for i in range(1, nums[currentIndex] + 1):
        found = canJumpHelper(nums, currentIndex+i, memo)
        if found:
            return True
    memo[currentIndex] = False
    return memo[currentIndex]


#better solution with time complexity of O(N) only
#this method only suitable for this case where we can jump further than the last index
#if we want to jump exactly to the last index, below method will fail
def canJumpBest(nums):
    last = len(nums) -1
    for index in range(len(nums)-2, -1, -1):
        if index + nums[index] >= last:
            last = index
    return last == 0

if __name__ == "__main__":
    print(canJump([2,3,1,1,4]))
    print(canJump([3,2,1,0,4]))
    print(canJumpBest([2,3,1,1,4]))
    print(canJumpBest([3,2,1,0,4]))