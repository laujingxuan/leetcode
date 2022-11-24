def subsetsWithDup(nums):
    nums.sort()
    foundList = []
    subSetsWithDupHelper(nums, [], foundList, 0)
    return foundList

# def subSetsWithDupHelper(nums, currentList, foundList):
#     foundList.append(currentList[:])
#     if len(nums)==0:
#         return
    
#     for index, num in enumerate(nums):
#         if index != 0 and num == nums[index - 1]:
#             continue
#         currentList.append(num)
#         subSetsWithDupHelper(nums[index+1:], currentList, foundList)
#         del currentList[len(currentList) - 1]

def subSetsWithDupHelper(nums, currentList, foundList, currentIndex):
    foundList.append(currentList[:])
    if currentIndex == len(nums):
        return
    
    for index in range(currentIndex, len(nums)):
        if index > currentIndex and nums[index] == nums[index - 1]:
            continue
        currentList.append(nums[index])
        subSetsWithDupHelper(nums, currentList, foundList, index+1)
        del currentList[len(currentList) - 1]


if __name__=='__main__':
    foundList = subsetsWithDup([1,2,2])
    for output in foundList:
        print(output)