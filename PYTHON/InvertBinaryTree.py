# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTreeDFS(self, root):
        if root == None or (root.left == None and root.right == None):
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def invertTreeBFS(self, root):
        if root == None:
            return root
        queue = []
        queue.append(root)
        while len(queue) > 0:
            current = queue.pop()
            current.left, current.right = current.right, current.left
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
        return root