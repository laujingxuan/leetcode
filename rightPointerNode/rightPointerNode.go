package main

type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

//You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
//Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
//Initially, all next pointers are set to NULL.
func connectBFS(root *Node) *Node {
	if root == nil {
		return nil
	}
	queue := []*Node{}
	queue = append(queue, root)
	var nextNode *Node
	for len(queue) > 0 {
		nextNode = nil
		for i := len(queue); i > 0; i-- {
			currentNode := queue[0]
			queue = queue[1:]
			currentNode.Next = nextNode
			nextNode = currentNode
			if currentNode.Right != nil {
				queue = append(queue, currentNode.Right)
				queue = append(queue, currentNode.Left)
			}
		}
	}
	return root
}

func connectDFS(root *Node) *Node {
	if root == nil {
		return nil
	}

	if root.Left != nil {
		root.Left.Next = root.Right
		if root.Next != nil {
			root.Right.Next = root.Next.Left
		}
	}
	connectDFS(root.Right)
	connectDFS(root.Left)
	return root
}

func connectBFSOptimized(root *Node) *Node {
	head := root
	for head != nil {
		current := head
		for current != nil {
			if current.Left != nil {
				current.Left.Next = current.Right
				if current.Next != nil {
					current.Right.Next = current.Next.Left
				}
			}
			current = current.Next
		}
		head = head.Left
	}

	return root
}
