# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head == None:
            return head
        depthOfListNode = 1
        lastNode = head
        while lastNode.next != None:
            depthOfListNode += 1
            lastNode = lastNode.next
        
        trueRotationCount = k%depthOfListNode
        if trueRotationCount == 0:
            return head
        startingNodePosition = depthOfListNode - trueRotationCount

        newLastNode = lastNode
        lastNode.next = head
        while newLastNode != None and startingNodePosition > 0:
            startingNodePosition -= 1
            newLastNode = newLastNode.next
        output = newLastNode.next
        newLastNode.next = None
        return output