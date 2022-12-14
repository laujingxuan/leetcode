# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #BFS method
    def rightSideView(self, root):
        if root == None:
            return []
        queue = []
        output = []
        queue.append(root)
        while len(queue) != 0:
            added = False
            queueLen = len(queue)
            for i in range(queueLen):
                current = queue.pop(0)
                if not added:
                    output.append(current.val)
                    added = True
                if current.right != None:
                    queue.append(current.right)
                if current.left != None:
                    queue.append(current.left)
        return output

    #DFS method
    def rightSideView(self, root):
        output = []
        self.rightSideViewHelper(root, output, 0)
        return output

    def rightSideViewHelper(self, root, output, depth):
        if root == None:
            return output
        if len(output) == depth:
            output.append(root.val)
        self.rightSideViewHelper(root.right, output, depth + 1)
        self.rightSideViewHelper(root.left, output, depth + 1)
        return output