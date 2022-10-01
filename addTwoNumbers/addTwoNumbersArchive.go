package main

import (
	"fmt"
	"math"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

//NOT ABLE TO HANDLE CASES WHERE INTEGERS > 64bits
//You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
func addTwoNumbersArchive(l1 *ListNode, l2 *ListNode) *ListNode {
	var num1, num2 []int
	currentNodel1 := l1
	num1 = append(num1, currentNodel1.Val)
	for currentNodel1.Next != nil {
		currentNodel1 = currentNodel1.Next
		num1 = append(num1, currentNodel1.Val)
	}
	var number1, number2 int
	for x := 0; x < len(num1); x++ {
		number1 += num1[x] * int(math.Pow(10, float64(x)))
	}
	currentNodel2 := l2
	num2 = append(num2, currentNodel2.Val)
	for currentNodel2.Next != nil {
		currentNodel2 = currentNodel2.Next
		num2 = append(num2, currentNodel2.Val)
	}
	for x := 0; x < len(num2); x++ {
		number2 += num2[x] * int(math.Pow(10, float64(x)))
	}
	totalNumber := number1 + number2
	lastDigit := totalNumber % 10
	firstListNode := &ListNode{
		Val: lastDigit,
	}
	currentListNode := firstListNode
	for totalNumber > 9 {
		totalNumber = totalNumber / 10
		newListNode := &ListNode{
			Val: totalNumber % 10,
		}
		currentListNode.Next = newListNode
		currentListNode = newListNode
	}

	return firstListNode
}

func Pow(i1, i2 int) {
	panic("unimplemented")
}

func mainArchive() {
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

	fmt.Println(addTwoNumbersArchive(&l11, &l21).Val)
}
