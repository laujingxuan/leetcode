package main

import "fmt"

type ListNode struct {
	Data int
	Next *ListNode
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
