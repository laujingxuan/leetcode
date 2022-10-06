package main

import "fmt"

var (
	l13 = ListNode{
		Data: 1,
	}
	l12 = ListNode{
		Data: 2,
		Next: &l13,
	}
	l11 = ListNode{
		Data: 3,
		Next: &l12,
	}
	l23 = ListNode{
		Data: 4,
		Next: &l11,
	}
	l22 = ListNode{
		Data: 5,
		Next: &l23,
	}
	l21 = ListNode{
		Data: 6,
		Next: &l22,
	}
)

func main() {
	// removeDups(&l21)
	// removeDupsWithoutBuffer(&l21)
	// printLinkedList(&l21)
	// fmt.Println(findEveryKthToLastElements(&l21, 3))
	fmt.Println(findKthToLastElement(&l21, 3))
}
