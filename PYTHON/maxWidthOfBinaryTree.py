# Given the root of a binary tree, return the maximum width of the given tree.

# The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

# It is guaranteed that the answer will in the range of a 32-bit signed integer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #bfs solution
    def widthOfBinaryTree(self, root):
        if root is None:
            return 0
        queue = [(root, 0)]
        startIndex = -1
        maxLen = 0
        while len(queue) > 0:
            queueLen = len(queue)
            for i in range(queueLen):
                (node, order) = queue.pop(0)
                if startIndex == -1:
                    startIndex = order
                currLen = order - startIndex + 1
                if node.left is not None:
                    queue.append((node.left, order * 2))
                if node.right is not None:
                    queue.append((node.right, order * 2 + 1))
                maxLen = max(maxLen, currLen)
            startIndex = -1
        return maxLen
    
    #dfs solution
    def widthOfBinaryTree(self, root):
        return self.dfsHelper(root, 0, 0, [], [])

    def dfsHelper(self, root, order, level, startList, endList):
        if root is None:
            return 0
        if level == len(startList):
            startList.append(order)
            endList.append(order)
        else:
            endList[level] = order
        currLen = endList[level] - startList[level] + 1
        # print(str(root.val) + ":" + str(currLen) + ":" + str(startList) + ":" + str(endList))
        left = self.dfsHelper(root.left, order * 2, level + 1, startList, endList)
        right = self.dfsHelper(root.right,  order * 2 + 1, level + 1, startList, endList)
        return max(currLen, left, right)


    #non ideal
    def widthOfBinaryTreeTimeLimitExceeded(self, root):
        if root is None:
            return 0
        queue = [root]
        hasNextLevel = True
        maxLen = 0
        while len(queue) > 0 and hasNextLevel:
            queueLen = len(queue)
            hasNextLevel = not hasNextLevel
            starting = -1
            ending = -1
            for i in range(queueLen):
                node = queue.pop(0)
                if node is None:
                    if hasNextLevel:
                        queue.append(None)
                        queue.append(None)
                    continue
                if starting == -1:
                    starting = i
                ending = i
                queue.append(node.left)
                queue.append(node.right)
                if node.left is not None or node.right is not None:
                    hasNextLevel = True
                maxLen = max(maxLen, ending - starting + 1)
        return maxLen