# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #recursive approach
    def reverseList(self, head):
        return self.reverseListHelper(head, None)

    def reverseListHelper(self, head, preHead):
        if head == None:
            return preHead
        deepest = self.reverseListHelper(head.next, head)
        head.next = preHead
        return deepest

    #iterative approach
    def reverseList(self, head):
        current = head
        pre = None
        while current != None:
            temp = current.next
            current.next = pre
            pre = current
            current = temp
        return pre

    #ReverseLinkedList II
    #Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
    def reverseBetween(self, head, left: int, right: int):
        track = 0
        current = head
        pre = None
        while current != None:
            track += 1
            temp = current.next
            if track >= left:
                reversedFirst, postNode = self.reverseBetweenHelper(current, right, track)
                current.next = postNode
                if left == 1:
                    return reversedFirst
                pre.next = reversedFirst
                return head
            pre = current
            current = temp

    def reverseBetweenHelper(self, head, right, track):
        pre = None
        current = head
        while current != None and track <= right:
            temp = current.next
            current.next = pre
            pre = current
            current = temp
            track += 1
        return pre, current

    #tidier solution for reverse linked list II
    def reverseBetween(self, head, m, n):
        if not head or m == n: return head
        p = dummy = ListNode(None)
        dummy.next = head
        for i in range(m-1): p = p.next
        tail = p.next

        for i in range(n-m):
            tmp = p.next       
            p.next = tail.next       
            tail.next = tail.next.next   
            p.next.next = tmp           
        return dummy.next