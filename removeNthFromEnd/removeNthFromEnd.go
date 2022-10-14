package main

import "fmt"

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
		Val:  4,
		Next: &fifth,
	}
	fifth = ListNode{
		Val: 5,
	}
)

func main() {
	printLinkList(removeNthFromEnd(&first, 1))
}

func printLinkList(head *ListNode) {
	current := head
	for current != nil {
		fmt.Printf("%d,", current.Val)
		current = current.Next
	}
	fmt.Println()
}

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	firstNode := head
	secondNode := head
	var previousNode *ListNode
	for n > 1 {
		secondNode = secondNode.Next
		n--
	}
	for secondNode.Next != nil {
		secondNode = secondNode.Next
		previousNode = firstNode
		firstNode = firstNode.Next
	}
	if firstNode == head {
		return head.Next
	}
	previousNode.Next = firstNode.Next
	return head
}
