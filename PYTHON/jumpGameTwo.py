def jump(nums):
    memo = [0]*len(nums)
    return jumpHelper(nums, 0, memo)

def jumpHelper(nums, currentIndex, memo):
    if currentIndex == len(nums) - 1:
        return 0
    if currentIndex >= len(nums):
        return -1
    if memo[currentIndex] != 0:
        return memo[currentIndex]
    tempMin = -1
    for i in range(1, nums[currentIndex] + 1):
        stepNeeded = jumpHelper(nums, currentIndex + i, memo)
        if tempMin == -1:
            tempMin = stepNeeded
        elif stepNeeded != -1:
            tempMin = min(tempMin, stepNeeded)
    memo[currentIndex] = tempMin
    if memo[currentIndex] != -1:
        memo[currentIndex] += 1
    return memo[currentIndex]

def jumpAlternate(nums):
    tracking = [-1] * len(nums)
    tracking[len(nums) - 1] = 0
    for i in range(len(nums)-2, -1, -1):
        minTrack = -1
        for j in range(1, nums[i] + 1):
            if tracking[i + j] >= 0:
                if minTrack == -1:
                    minTrack = tracking[i + j] + 1
                elif tracking[i+j] != -1:
                    minTrack = min(minTrack, tracking[i + j] + 1)
        tracking[i] = minTrack
    return tracking[0]

if __name__ == "__main__":
    # print(jump([2,3,0,1,4]))
    # print(jump([2,3,1,1,4]))
    print(jumpAlternate([2,3,1,1,4]))