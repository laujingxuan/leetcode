#Work for both unique and non-unique candidates input
def combinationSum(candidates, target):
    candidates.sort()
    foundList = []
    combinationSumHelper(candidates, target, foundList, [], 0)
    return foundList

def combinationSumHelper(candidates, target, foundList, currentList, startingIndex):
    if target == 0:
        foundList.append(currentList)
        return
    if target < 0:
        return

    for index in range(startingIndex, len(candidates)):
        if index != startingIndex and candidates[index] == candidates[index-1]:
            continue
        combinationSumHelper(candidates, target-candidates[index], foundList, currentList + [candidates[index]], index)
    return

#Only works for unique candidates input
def combinationSumAlternate(candidates, target):
    ret = []
    dfs(candidates, target, [], ret)
    return ret

def dfs(nums, target, path, ret):
    if target < 0:
        return 
    if target == 0:
        ret.append(path)
        return 
    for i in range(len(nums)):
        dfs(nums[i:], target-nums[i], path+[nums[i]], ret)

if __name__ == "__main__":
    print(combinationSum([2,3,2], 5))
    print(combinationSumAlternate([2,3,2], 5))