# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        firstPointer = head
        secondPointer = head
        while (secondPointer.next != None and secondPointer.next.next != None):
            secondPointer = secondPointer.next.next
            firstPointer = firstPointer.next
        rightSide = firstPointer.next
        firstPointer.next = None
        sortedLeft = self.sortList(head)
        sortedRight = self.sortList(rightSide)

        # print("left:")
        # self.printListNode(sortedLeft)
        # print("right:")
        # self.printListNode(sortedRight)
        returnHead = sortedLeft
        if sortedLeft.val > sortedRight.val:
            returnHead = sortedRight
            sortedRight = sortedRight.next
        else:
            sortedLeft = sortedLeft.next
        
        current = returnHead
        while sortedLeft != None and sortedRight != None:
            if sortedLeft.val > sortedRight.val:
                current.next = sortedRight
                sortedRight = sortedRight.next
            else:
                current.next = sortedLeft
                sortedLeft = sortedLeft.next
            current = current.next
        
        if sortedLeft != None:
            current.next = sortedLeft
        
        if sortedRight != None:
            current.next = sortedRight
        return returnHead

    def printListNode(self, head):
        current = head
        print("ListNode")
        while current != None:
            print(current.val)
            current = current.next
        print("End")

        
if __name__ == "__main__":
    test = Solution()
    forth = ListNode(3)
    third = ListNode(1, forth)
    second = ListNode(2, third)
    first = ListNode(4, second)
    output = test.sortList(first)
    test.printListNode(output)