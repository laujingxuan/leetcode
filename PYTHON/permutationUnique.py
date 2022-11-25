def permuteUnique(nums):
    nums.sort()
    foundList = []
    permutationHelper(nums, foundList, [])
    return foundList
    
        
def permutationHelper(nums, foundList, currentList):
    if len(nums) == 0:
        foundList.append(currentList)
        return
    for index, num in enumerate(nums):
        if index != 0 and nums[index] == nums[index-1]:
            continue
        nums.remove(num)
        permutationHelper(nums, foundList, currentList + [num])
        nums.insert(index, num)
    return

def permuteUniqueAlternate(nums):
    ans = [[]]
    for n in nums:
        new_ans = []
        for l in ans:
            print("test")
            print(l)
            for i in range(len(l)+1):
                new_ans.append(l[:i]+[n]+l[i:])
                if i<len(l) and l[i]==n: break              #handles duplication
        ans = new_ans
    return ans

if __name__ == "__main__":
    print(permuteUnique([1,1,2]))
    print(permuteUniqueAlternate([1,1,2]))