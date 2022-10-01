package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

//You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	currentNodel1 := l1
	currentNodel2 := l2
	total := currentNodel1.Val + currentNodel2.Val
	tenthVal := total / 10
	firstListNode := &ListNode{
		Val: total % 10,
	}
	currentNode := firstListNode
	for currentNodel1.Next != nil && currentNodel2.Next != nil {
		currentNodel1 = currentNodel1.Next
		currentNodel2 = currentNodel2.Next
		newListNode := &ListNode{
			Val: (currentNodel1.Val + currentNodel2.Val + tenthVal) % 10,
		}
		currentNode.Next = newListNode
		currentNode = newListNode
		tenthVal = (currentNodel1.Val + currentNodel2.Val + tenthVal) / 10
	}

	for currentNodel1.Next != nil {
		currentNodel1 = currentNodel1.Next
		newListNode := &ListNode{
			Val: (currentNodel1.Val + tenthVal) % 10,
		}
		currentNode.Next = newListNode
		currentNode = newListNode
		tenthVal = (currentNodel1.Val + tenthVal) / 10
	}

	for currentNodel2.Next != nil {
		currentNodel2 = currentNodel2.Next
		newListNode := &ListNode{
			Val: (currentNodel2.Val + tenthVal) % 10,
		}
		currentNode.Next = newListNode
		currentNode = newListNode
		tenthVal = (currentNodel2.Val + tenthVal) / 10
	}
	if tenthVal != 0 {
		currentNode.Next = &ListNode{
			Val: tenthVal,
		}
	}
	return firstListNode
}

func main() {
	l13 := ListNode{
		Val: 3,
	}
	l12 := ListNode{
		Val:  4,
		Next: &l13,
	}
	l11 := ListNode{
		Val:  2,
		Next: &l12,
	}
	l23 := ListNode{
		Val: 4,
	}
	l22 := ListNode{
		Val:  6,
		Next: &l23,
	}
	l21 := ListNode{
		Val:  5,
		Next: &l22,
	}

	fmt.Println(addTwoNumbers(&l11, &l21).Val)
}
