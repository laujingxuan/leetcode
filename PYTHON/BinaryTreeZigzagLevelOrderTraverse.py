# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        output = []
        queue = []
        queue.append(root)
        fromLeft = True
        while len(queue) > 0:
            queueLen = len(queue)
            levelList = []
            for i in range(queueLen):
                current = queue.pop(0)
                if fromLeft:
                    levelList.append(current.val)
                else:
                    levelList.insert(0, current.val)
                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
            fromLeft = not fromLeft
            output.append(levelList)
        return output

    def zigzagLevelOrderAlternateFlip(self, root):
        if root == None:
            return []
        output = []
        queue = []
        queue.append(root)
        fromLeft = True
        while len(queue) > 0:
            queueLen = len(queue)
            levelList = []
            for i in range(queueLen):
                current = queue.pop(0)
                levelList.append(current.val)
                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
            if not fromLeft:
                levelList = levelList[::-1]
            output.append(levelList)
            fromLeft = not fromLeft
        return output

if __name__ == "__main__":
    fifth = TreeNode(5)
    forth = TreeNode(4)
    third = TreeNode(3, None, fifth)
    second = TreeNode(2, forth, None)
    first = TreeNode(1, second, third)
    test = Solution()
    print(test.zigzagLevelOrder(first))

