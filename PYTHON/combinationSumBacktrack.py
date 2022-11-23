# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.
def combinationSum2(candidates, target):
    currentCombi = []
    foundCombi = []
    candidates.sort()
    combinationHelper(candidates, target, currentCombi, foundCombi)
    return foundCombi

def combinationHelper(candidates, target, currentCombi, foundCombi):
    if target == 0:
        foundCombi.append(currentCombi)
        return
    if target < 0 or not candidates:
        return
    newCandidates = candidates[:]
    for index, candidate in enumerate(candidates):
        # Very important here! We don't use `i > 0` because we always want 
        # to count the first element in this recursive step even if it is the same 
        # as one before. To avoid overcounting, we just ignore the duplicates
        # after the first element.
        if index!=0 and candidate == candidates[index-1]:
            newCandidates.remove(candidate)
            continue
        newCandidates.remove(candidate)
        combinationHelper(newCandidates, target-candidate, currentCombi + [candidate], foundCombi)
    return

def main():
    print("This is the main function.")
    input = [10,1,2,7,6,1,5]
    outputs = combinationSum2(input, 8)
    for output in outputs:
        print(output)

# We use the if-statement to run blocks of code only if our program is the main program executed. This allows our program to be executable by itself, but friendly to other Python modules who may want to import some functionality without having to run the code.
if __name__ == '__main__':
    main()