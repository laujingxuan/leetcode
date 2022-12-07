# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #time complexity of O(N^2) because we are revisiting the list for every node and space complexity of O(N)
    def pathSumNonIdeal(self, root, targetSum):
        return self.pathSumHelper(root, targetSum, [], 0)
        
    def pathSumHelper(self, root, targetSum, pathList, currentSum):
        if root == None:
            return 0
        currentSum += root.val
        pathList.append(root.val)
        foundTotal = 0
        checkSum = currentSum
        for i in range(len(pathList)):
            if checkSum ==targetSum:
                foundTotal += 1
            checkSum -= pathList[i]
        leftTotal = self.pathSumHelper(root.left, targetSum, pathList[:], currentSum)
        rightTotal = self.pathSumHelper(root.right, targetSum, pathList[:], currentSum)
        return foundTotal + leftTotal + rightTotal

    #better way with O(N) time and space complexity
    #explanation: https://leetcode.com/problems/path-sum-iii/solutions/141424/python-step-by-step-walk-through-easy-to-understand-two-solutions-comparison/?envType=study-plan&id=level-2&orderBy=most_votes
    def pathSum(self, root, targetSum):
        memo = {0:1}
        self.total = 0
        self.pathSumIdealHelper(root, targetSum, memo, 0)
        return self.total
        
    def pathSumIdealHelper(self, root, targetSum, memo, currentSum):
        if root == None:
            return 0
        currentSum += root.val
        previousFound = currentSum - targetSum
        self.total += memo.get(previousFound, 0)
        memo[currentSum] = memo.get(currentSum, 0) + 1
        leftTotal = self.pathSumIdealHelper(root.left, targetSum, memo, currentSum)
        rightTotal = self.pathSumIdealHelper(root.right, targetSum, memo, currentSum)
        memo[currentSum] -= 1
        return leftTotal + rightTotal
