package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

//Question 230
func kthSmallest(root *TreeNode, k int) int {
	foundInt := getNodeValues(root, []int{}, k)
	return foundInt[k-1]
}

func getNodeValues(root *TreeNode, foundInt []int, k int) []int {
	if root == nil {
		return foundInt
	}

	foundInt = getNodeValues(root.Left, foundInt, k)
	if len(foundInt) == k {
		return foundInt
	}
	foundInt = append(foundInt, root.Val)
	if len(foundInt) == k {
		return foundInt
	}
	foundInt = getNodeValues(root.Right, foundInt, k)
	if len(foundInt) == k {
		return foundInt
	}

	return foundInt
}

var (
	thirdNode = TreeNode{
		Val:   3,
		Left:  &firstNode,
		Right: &forthNode,
	}
	forthNode = TreeNode{
		Val: 4,
	}
	firstNode = TreeNode{
		Val:   1,
		Right: &secondNode,
	}
	secondNode = TreeNode{
		Val: 2,
	}
)

func main() {
	fmt.Println(kthSmallest(&thirdNode, 2))
}
