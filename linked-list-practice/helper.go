package main

import "fmt"

type ListNode struct {
	Data int
	Next *ListNode
}

type StringListNode struct {
	Data string
	Next *StringListNode
}

//Remove duplicates from an unsorted linked list without using temporary buffer
func removeDupsWithoutBuffer(node *ListNode) {
	firstCurrentNode := node
	for firstCurrentNode != nil {
		previousNode := firstCurrentNode
		for previousNode.Next != nil {
			if firstCurrentNode.Data == previousNode.Next.Data {
				previousNode.Next = previousNode.Next.Next
			} else {
				previousNode = previousNode.Next
			}
		}

		firstCurrentNode = firstCurrentNode.Next
	}
}

//Remove duplicates with temporary buffer
func removeDups(node *ListNode) {
	trackMap := map[int]bool{}
	trackMap[node.Data] = true
	currentNode := node
	for currentNode.Next != nil {
		if trackMap[currentNode.Next.Data] {
			currentNode.Next = currentNode.Next.Next
		} else {
			trackMap[currentNode.Next.Data] = true
		}
		currentNode = currentNode.Next
	}
}

func printLinkedList(node *ListNode) {
	currentNode := node
	fmt.Printf("value=%d; ", currentNode.Data)
	for currentNode.Next != nil {
		fmt.Printf("value=%d; ", currentNode.Next.Data)
		currentNode = currentNode.Next
	}
	fmt.Println()
}

//Find every elements from kth to last
func findEveryKthToLastElements(node *ListNode, k int) []int {
	currentNode := node
	returnArray := []int{}
	for currentNode != nil {
		k -= 1
		if k <= 0 {
			returnArray = append(returnArray, currentNode.Data)
		}
		currentNode = currentNode.Next
	}
	return returnArray
}

//Find the kth to last element of a singly linked list
func findKthToLastElement(node *ListNode, k int) int {
	//two pointers with kth apart
	p1Node := node
	p2Node := node
	for k > 0 {
		k -= 1
		p2Node = p2Node.Next
		if p2Node == nil {
			return -1
		}
	}
	for p2Node.Next != nil {
		p1Node = p1Node.Next
		p2Node = p2Node.Next
	}
	return p1Node.Next.Data
}

//Delete one of the nodes in a linked list when you are given access to that node
func deleteMiddleNode(middleNode *ListNode) {
	//copy the next node to the current node
	currentNode := middleNode
	for currentNode.Next != nil {
		currentNode.Data = currentNode.Next.Data
		if currentNode.Next.Next == nil {
			currentNode.Next = nil
			break
		}
		currentNode = currentNode.Next
	}
}

//Two numbers represented by a linked list where each node contains a single digit. The digits are stored in reverse order. Return sum of the linked list
//7 -> 1 -> 6 + 5 -> 9 -> 2 = 617+ 295
func sumList(first, second *ListNode) *ListNode {
	returnListNode := &ListNode{
		Data: (first.Data + second.Data) % 10,
	}
	tenthDigit := (first.Data + second.Data) / 10
	currentFirst := first
	currentSecond := second
	currentReturn := returnListNode
	for currentFirst.Next != nil && currentSecond.Next != nil {
		currentReturn.Next = &ListNode{
			Data: (currentFirst.Next.Data + currentSecond.Next.Data + tenthDigit) % 10,
		}
		tenthDigit = (currentFirst.Next.Data + currentSecond.Next.Data + tenthDigit) / 10
		currentReturn = currentReturn.Next
		currentFirst = currentFirst.Next
		currentSecond = currentSecond.Next
	}
	for currentFirst.Next != nil {
		currentReturn.Next = &ListNode{
			Data: (currentFirst.Next.Data + tenthDigit) % 10,
		}
		tenthDigit = (currentFirst.Next.Data + tenthDigit) / 10
		currentReturn = currentReturn.Next
		currentFirst = currentFirst.Next
	}

	for currentSecond.Next != nil {
		currentReturn.Next = &ListNode{
			Data: (currentSecond.Next.Data + tenthDigit) % 10,
		}
		tenthDigit = (currentSecond.Next.Data + tenthDigit) / 10
		currentReturn = currentReturn.Next
		currentSecond = currentSecond.Next
	}

	if tenthDigit != 0 {
		currentReturn.Next = &ListNode{
			Data: currentSecond.Next.Data,
		}
	}

	return returnListNode
}

func sumListWithRecurse(first, second *ListNode, carry int) *ListNode {
	if first == nil && second == nil && carry == 0 {
		return nil
	}

	result := &ListNode{}
	value := carry
	if first != nil {
		value += first.Data
	}
	if second != nil {
		value += second.Data
	}
	result.Data = value % 10
	carry = value / 10
	if first != nil || second != nil {
		var more *ListNode
		if first != nil && second != nil {
			more = sumListWithRecurse(first.Next, second.Next, carry)
		} else if first == nil {
			more = sumListWithRecurse(first, second.Next, carry)
		} else {
			more = sumListWithRecurse(first.Next, second, carry)
		}
		result.Next = more
	}

	return result
}

//To check if a linked list is a palindrome
//Palindrome: a word, phrase, or sequence that reads the same backwards as forwards
func isPalindrome(node *ListNode) bool {
	fastNode := node
	slowNode := node
	firstHalf := []int{node.Data}
	//slow runner fast runner
	for fastNode.Next != nil && fastNode.Next.Next != nil {
		slowNode = slowNode.Next
		fastNode = fastNode.Next.Next
		firstHalf = append(firstHalf, slowNode.Data)
	}
	fmt.Println("firstHalf: ", firstHalf)
	//odd number of nodes (compare first node up to before slowNode with slowNode.Next)
	if fastNode.Next == nil {
		//remove the last one as last one is the center
		firstHalf = firstHalf[:len(firstHalf)-1]
	}
	//even number of nodes (compare first node up to slowNode with slowNode.Next)
	for x := len(firstHalf) - 1; x >= 0; x-- {
		if firstHalf[x] != slowNode.Next.Data {
			return false
		}
		slowNode = slowNode.Next
	}
	return true
}

//Alternate solution
func isPalindromeWithRecurse(node *ListNode) bool {
	length := lengthOfList(node)
	output := isPalindromeRecurse(node, length)
	return output.result
}

type Result struct {
	node   *ListNode
	result bool
}

func isPalindromeRecurse(node *ListNode, length int) Result {
	if node == nil || length <= 0 {
		//Even number of nodes
		return Result{node, true}
	} else if length == 1 {
		//Odd number of nodes
		return Result{node.Next, true}
	}

	//Recursive on subList
	res := isPalindromeRecurse(node.Next, length-2)

	//if child calls are not a palindrome, pass back the failed result up
	if !res.result || res.node == nil {
		return res
	}

	//Check if matches corresponding node on other side
	res.result = node.Data == res.node.Data

	//return corresponding node
	res.node = res.node.Next

	return res
}

func lengthOfList(node *ListNode) int {
	size := 0
	for node != nil {
		size++
		node = node.Next
	}
	return size
}

//Check if two linked lists intesect. Return the intersecting node
func intersection(first, second *ListNode) *ListNode {
	checkMap := map[int][]*ListNode{}
	currentFirstNode := first
	for currentFirstNode != nil {
		if elem, ok := checkMap[currentFirstNode.Data]; ok {
			elem = append(elem, currentFirstNode)
			checkMap[currentFirstNode.Data] = elem
		} else {
			checkMap[currentFirstNode.Data] = []*ListNode{currentFirstNode}
		}
		currentFirstNode = currentFirstNode.Next
	}
	currentSecondNode := second
	intersectingNodes := []*ListNode{}
	for currentSecondNode != nil {
		if elem, ok := checkMap[currentSecondNode.Data]; ok {
			for _, node := range elem {
				if node == currentSecondNode {
					intersectingNodes = append(intersectingNodes, node)
				}
			}
		}
		currentSecondNode = currentSecondNode.Next
	}
	for _, node := range intersectingNodes {
		currentNode := node
		isIntersectNode := true
		for x := 0; x < len(intersectingNodes)-1; x++ {
			if currentNode.Next == nil {
				isIntersectNode = false
				break
			}
		}
		if isIntersectNode {
			return node
		}
	}
	return nil
}
