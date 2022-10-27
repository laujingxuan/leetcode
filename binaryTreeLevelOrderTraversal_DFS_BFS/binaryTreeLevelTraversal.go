package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrderBFS(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	output := [][]int{}
	queue := []*TreeNode{root}
	for len(queue) != 0 {
		levelOutput := []int{}
		for i := len(queue) - 1; i >= 0; i-- {
			currentNode := queue[0]
			queue = queue[1:]
			levelOutput = append(levelOutput, currentNode.Val)
			if currentNode.Left != nil {
				queue = append(queue, currentNode.Left)
			}
			if currentNode.Right != nil {
				queue = append(queue, currentNode.Right)
			}
		}
		output = append(output, levelOutput)
	}
	return output
}

func levelOrderDFS(root *TreeNode) [][]int {
	output := [][]int{}
	output = levelOrderDFSHelper(root, output, 0)
	return output
}

func levelOrderDFSHelper(root *TreeNode, store [][]int, height int) [][]int {
	if root == nil {
		return store
	}
	if height >= len(store) {
		store = append(store, []int{})
	}
	desiredStore := store[height]
	desiredStore = append(desiredStore, root.Val)
	store[height] = desiredStore
	store = levelOrderDFSHelper(root.Left, store, height+1)
	store = levelOrderDFSHelper(root.Right, store, height+1)

	return store
}
