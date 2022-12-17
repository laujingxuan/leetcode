# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.isSymmetricHelper(root.left, root.right)
        
    def isSymmetricHelper(self, left, right):
        if left == None and right == None :
            return True
        if left == None or right == None:
            return False
        return left.val == right.val and self.isSymmetricHelper(left.right, right.left) and self.isSymmetricHelper(left.right, right.left)
    
    def isSymmetricIterativeMethod(self, root):
        if root == None:
            return True
        stack = []
        stack.append([root.left, root.right])
        while len(stack) > 0:
            current = stack.pop()
            if current[0] == None and current[1] == None:
                continue
            if current[0] == None or current[1] == None:
                return False
            if current[0].val != current[1].val:
                return False
            stack.append([current[0].left, current[1].right])
            stack.append([current[0].right, current[1].left])
        return True

if __name__ == "__main__":
    first = TreeNode(2)
    second = TreeNode(3)
    third = TreeNode(3)
    forth = TreeNode(4)
    fifth = TreeNode(5)
    sixth = TreeNode(5)
    first.left = second
    first.right = third
    second.left = forth
    second.right = sixth
    third.left = fifth
    test = Solution()
    print(test.isSymmetric(first))