# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find the mid pointer
        mid = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            mid = mid.next
        
        #reverse the second part of the listNode
        latestNode = None
        current = mid.next
        while current is not None:
            temp = current.next
            current.next = latestNode
            latestNode = current
            current = temp
        
        #use latestNode and headNode to compile the final list
        #since mid will be the last node, need to set mid.next=None
        mid.next = None
        current = head
        while latestNode is not None and current is not None:
            temp = current.next
            temp2 = latestNode.next
            current.next = latestNode
            latestNode.next = temp
            latestNode = temp2
            current = temp
        return head

    #using stack
    def reorderListWorstTimeComplexity(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find the mid pointer
        mid = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            mid = mid.next
        
        #push nodes after mid to stack
        stack = []
        start = mid.next
        while start is not None:
            stack.append(start)
            start = start.next
        #mid will be the last node after reordering
        mid.next = None
        
        current = head
        while len(stack) > 0:
            node = stack.pop()

            temp = current.next
            current.next = node
            node.next = temp
            current = node.next
        return head