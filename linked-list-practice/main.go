package main

import "fmt"

var (
	l13 = ListNode{
		Data: 6,
	}
	l12 = ListNode{
		Data: 5,
		Next: &l13,
	}
	l11 = ListNode{
		Data: 4,
		Next: &l12,
	}
	l23 = ListNode{
		Data: 3,
		Next: &l11,
	}
	l22 = ListNode{
		Data: 2,
		Next: &l23,
	}
	l21 = ListNode{
		Data: 1,
		Next: &l22,
	}

	p23 = ListNode{
		Data: 6,
		// Next: &l11,
	}
	p22 = ListNode{
		Data: 5,
		Next: &p23,
	}
	p21 = ListNode{
		Data: 6,
		Next: &p22,
	}
)

func main() {
	// removeDups(&l21)
	// removeDupsWithoutBuffer(&l21)
	// printLinkedList(&l21)
	// fmt.Println(findEveryKthToLastElements(&l21, 3))
	// fmt.Println(findKthToLastElement(&l21, 3))
	// printLinkedList(&l21)
	// deleteMiddleNode(&l23)
	// printLinkedList(&l21)
	// sumList := sumList(&p21, &l21)
	// sumList := sumListWithRecurse(&p21, &l21, 0)
	// printLinkedList(sumList)
	// fmt.Println(isPalindrome(&p21))
	// fmt.Println(isPalindromeWithRecurse(&p21))
	// node := intersection(&p21, &l21)
	// if node != nil {
	// 	fmt.Println(node.Data)
	// } else {
	// 	fmt.Println("No intersection")
	// }
	ConvertSinglyToCircular(&l21)
	node := loopDetection(&l21)
	if node != nil {
		fmt.Println(node.Data)
	} else {
		fmt.Println("No circle")
	}
}
