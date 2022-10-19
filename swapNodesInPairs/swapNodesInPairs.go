package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

//Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
func swapPairs(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	//use pointers
	previousNode := &ListNode{}
	firstNode := head
	secondNode := head.Next
	afterSwapStartingNode := head.Next
	for firstNode != nil && secondNode != nil {
		if previousNode != nil {
			previousNode.Next = secondNode
		}
		firstNode.Next = secondNode.Next
		secondNode.Next = firstNode

		previousNode = firstNode
		firstNode = firstNode.Next
		if firstNode != nil && firstNode.Next != nil {
			secondNode = firstNode.Next
		} else {
			secondNode = nil
		}
	}
	return afterSwapStartingNode
}

var (
	first = ListNode{
		Val:  1,
		Next: &second,
	}
	second = ListNode{
		Val:  2,
		Next: &third,
	}
	third = ListNode{
		Val:  3,
		Next: &forth,
	}
	forth = ListNode{
		Val: 4,
	}
)

func printLinkList(node *ListNode) {
	current := node
	for current != nil {
		fmt.Printf("%d, ", current.Val)
		current = current.Next
	}
	fmt.Println()
}

func main() {
	printLinkList(swapPairs(&first))
}
