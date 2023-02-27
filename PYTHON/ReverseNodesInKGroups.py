# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #cleaner regression solution (without stack)
    def reverseKGroup(self, head, k):
        #check depth first
        count = 0
        current = head
        while current is not None and count != k:
            count += 1
            current = current.next
        if count == k:
            nextHead = self.reverseKGroup(current, k)
            current = head
            while k > 0:
                temp = current.next
                current.next = nextHead
                nextHead = current
                current = temp
                k -= 1
            head = nextHead
        return head

    #O(N) time complexity due to stack used. Can be improved to O(1)
    def reverseKGroup(self, head, k: int):
        current = head
        outputHead = None
        stack = []
        while current is not None:
            tracking = k
            #check depth
            checkNode = current
            # print(current)
            while tracking > 0 and checkNode is not None:
                tracking -= 1
                checkNode = checkNode.next
            if tracking > 0:
                stack.append([current, None])
                break
            #reverse the next k nodes
            reverseTrack = k
            prevNode = None
            lastNode = current
            while reverseTrack > 0 and current is not None:
                temp = current.next
                current.next = prevNode
                prevNode = current
                current = temp
                reverseTrack -= 1
            if outputHead is None:
                outputHead = prevNode
            stack.append([prevNode, lastNode])
        # print(stack)
        nextNodeHead = stack.pop()[0]
        # print(nextNodeHead)
        while len(stack) > 0:
            array = stack.pop()
            array[1].next = nextNodeHead
            nextNodeHead = array[0]
        return outputHead