package main

var (
	first = TreeNode{
		Val:  1,
		Left: &second,
	}
	second = TreeNode{
		Val:  2,
		Left: &third,
	}
	third = TreeNode{
		Val: 3,
	}
	forth = TreeNode{
		Val: 4,
	}
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func flatten(root *TreeNode) {
	if root == nil {
		return
	}

	currentNode := root
	for currentNode != nil {
		if currentNode.Left != nil {
			rightMST := rightmost(currentNode.Left)
			tempRight := currentNode.Right
			currentNode.Right = currentNode.Left
			currentNode.Left = nil
			rightMST.Right = tempRight
		}
		currentNode = currentNode.Right
	}
}

func rightmost(root *TreeNode) *TreeNode {
	if root.Right == nil {
		return root
	}
	return rightmost(root.Right)
}
