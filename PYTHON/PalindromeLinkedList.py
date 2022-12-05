# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # time complexity O(N) and space complexity O(N)
    def isPalindrome(self, head):
        #send the pointer to center of the linked list first
        firstPointer = head
        secondPointer = head
        while secondPointer.next != None and secondPointer.next.next != None:
            firstPointer = firstPointer.next
            secondPointer = secondPointer.next.next
        secondHalfList = []
        while firstPointer.next != None:
            secondHalfList.append(firstPointer.next.val)
            firstPointer = firstPointer.next
        thirdPointer = head
        for i in range(len(secondHalfList) - 1, -1 , -1):
            if secondHalfList[i] != thirdPointer.val:
                return False
            thirdPointer = thirdPointer.next
        return True
        
        # time complexity O(N) and space complexity O(1) but edited the input
    def isPalindromeReversedListMethod(self, head: Optional[ListNode]) -> bool:
        #send the pointer to center of the linked list first
        firstPointer = head
        secondPointer = head
        while secondPointer != None and secondPointer.next != None:
            firstPointer = firstPointer.next
            secondPointer = secondPointer.next.next
        reversedHead = self.reverseList(firstPointer)
        firstPointer = head
        secondPointer = reversedHead
        while reversedHead != firstPointer and secondPointer != None:
            if firstPointer.val != secondPointer.val:
                return False
            firstPointer = firstPointer.next
            secondPointer = secondPointer.next
        return True

    def reverseList(self, head):
        reversedHead = None
        while head != None:
            temp = head.next
            head.next = reversedHead
            reversedHead = head
            head = temp
        return reversedHead