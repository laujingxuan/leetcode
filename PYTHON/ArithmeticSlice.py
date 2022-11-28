# An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.
def numberOfArithmeticSlices(nums):
    if len(nums) < 3:
        return 0
    diff = nums[1] - nums[0]
    count = 1
    checkList = []
    for i in range(2, len(nums)):
        if diff != nums[i] - nums[i-1]:
            if count >= 2:
                checkList.append(count)
            count = 1
            diff = nums[i] - nums[i-1]
        else:
            count += 1
    if count >= 2:
        checkList.append(count)
    totalCount = 0
    for num in checkList:
        oneCount = 1
        for i in range(3, num+1):
            oneCount = oneCount + i - 1
        totalCount += oneCount
    return totalCount

def numberOfArithmeticSlicesBetter(nums):
    if len(nums) < 3:
        return 0
    sum = 0
    curr = 0
    for i in range(2,len(nums)):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            curr += 1
            sum += curr
        else:
            curr = 0
    return sum

if __name__ == "__main__":
    print(numberOfArithmeticSlices([1,2,3,8,9,10]))
    print(numberOfArithmeticSlicesBetter([1,2,3,8,9,10]))