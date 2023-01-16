"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # solution with time complexity O(N) and space complexity O(N)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head
        trackMap = {}
        current = head
        previousCopied = Node(0)
        startPrevious = previousCopied
        while current != None:
            currentCopied = Node(current.val)
            trackMap[current] = currentCopied
            previousCopied.next = currentCopied
            previousCopied = currentCopied
            current = current.next
        current = head
        currentCopied = startPrevious.next
        while current != None:
            currentCopied.random = trackMap.get(current.random ,None)
            current = current.next
            currentCopied = currentCopied.next
        return startPrevious.next

    def copyRandomListTidier(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head
        trackMap = {}
        current = head
        while current != None:
            trackMap[current] = Node(current.val)
            current = current.next
        current = head
        while current != None:
            trackMap[current].random = trackMap.get(current.random ,None)
            trackMap[current].next = trackMap.get(current.next, None)
            current = current.next
        return trackMap[head]

    #O(N) time complexity and O(1) space complexity! Without additional space
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head
        current = head
        while current != None:
            newNode = Node(current.val)
            newNode.next = current.next
            current.next = newNode
            current = newNode.next
        # current = head
        # while current != None:
        #     print(current.val)
        #     current = current.next
        current = head
        while current != None:
            if current.random != None:
                current.next.random = current.random.next
            current = current.next.next
        
        current = head
        copiedHead = head.next
        copy = copiedHead
        while copy.next != None:
            current.next = current.next.next
            current = current.next

            copy.next = copy.next.next
            copy = copy.next
        return copiedHead