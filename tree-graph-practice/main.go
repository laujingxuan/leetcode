package main

import (
	"fmt"
	"math"
)

var (
	rootNode = NewGraphNode("1", []*graphNode{
		&secondNode,
		&thirdNode,
		&forthNode,
	})
	secondNode = NewGraphNode("2", []*graphNode{
		&fifthNode,
		&sixthNode})
	thirdNode       = NewGraphNode("3", []*graphNode{&seventhNode})
	forthNode       = NewGraphNode("4", []*graphNode{})
	fifthNode       = NewGraphNode("5", []*graphNode{&eightNode})
	sixthNode       = NewGraphNode("6", []*graphNode{})
	seventhNode     = NewGraphNode("7", []*graphNode{})
	eightNode       = NewGraphNode("8", []*graphNode{})
	sortedIntArray  = []int{1, 2, 3, 4, 5, 6, 7, 8}
	binaryNodeOne   = intNode{data: 5, leftNode: &binaryNodeTwo, rightNode: &binaryNodeThree}
	binaryNodeTwo   = intNode{data: 4, leftNode: &binaryNodeFour, rightNode: &binaryNodeFive}
	binaryNodeThree = intNode{data: 7}
	// binaryNodeFour  = intNode{data: 4}
	binaryNodeFour  = intNode{data: 2, leftNode: &binaryNodeSix, rightNode: &binaryNodeSeven}
	binaryNodeFive  = intNode{data: 6}
	binaryNodeSix   = intNode{data: 1}
	binaryNodeSeven = intNode{data: 3}
)

func main() {
	// fmt.Println(depthFirstSearch(&rootNode, "9"))
	// fmt.Println(breathFirstSearch(&rootNode, "9"))

	// rootNode := createMinimalTree(sortedIntArray)
	// fmt.Println("RootNode: ", rootNode.data)
	// printIntNode(rootNode)
	// listOfLinkList := listOfDepths(rootNode)
	// fmt.Println(len(listOfLinkList))
	// for index, linkList := range listOfLinkList {
	// 	fmt.Println("Depth:", index)
	// 	printIntLinkList(linkList)

	// fmt.Println("Is balance: ", checkBalance(&binaryNodeOne))
	fmt.Println("Is binary search tree: ", validateBST(&binaryNodeOne))
}

// Given a sorted aray with unique integer elements, the function will create a binary search tree with minimal height
func createMinimalTree(sortedArray []int) *intNode {
	if len(sortedArray) == 0 {
		return nil
	}
	centerPosition := len(sortedArray) / 2
	rootNode := intNode{data: sortedArray[centerPosition]}
	leftNode := createMinimalTree(sortedArray[:centerPosition])
	var rightNode *intNode
	if centerPosition+1 < len(sortedArray) {
		rightNode = createMinimalTree(sortedArray[centerPosition+1:])
	}
	rootNode.leftNode = leftNode
	rootNode.rightNode = rightNode
	return &rootNode
}

// Given a binary tree, the function will creates a linked list of all the nodes at each depth
func listOfDepths(binaryTree *intNode) []*intLinkNode {
	startingDepth := 0
	listOfLinkList := []*intLinkNode{}
	listOfLinkList = currentDepthLinkList(binaryTree, startingDepth, listOfLinkList)
	return listOfLinkList
}

func currentDepthLinkList(rootNode *intNode, depth int, listOfLinkList []*intLinkNode) []*intLinkNode {
	if rootNode == nil {
		return listOfLinkList
	}
	if len(listOfLinkList) > depth {
		depthLinkList := listOfLinkList[depth]
		newNode := intLinkNode{data: rootNode.data, next: depthLinkList}
		listOfLinkList[depth] = &newNode
	} else {
		listOfLinkList = append(listOfLinkList, &intLinkNode{data: rootNode.data})
	}
	listOfLinkList = currentDepthLinkList(rootNode.leftNode, depth+1, listOfLinkList)
	listOfLinkList = currentDepthLinkList(rootNode.rightNode, depth+1, listOfLinkList)
	return listOfLinkList
}

// Check if a binary tree is balanced (Heights of the two subtrees of any node never differ by more than one)
func checkBalance(node *intNode) bool {
	return isBalance(node, 0) != -1
}

func isBalance(node *intNode, currentHeight int) int {
	if node == nil {
		return currentHeight
	}
	leftHeight := isBalance(node.leftNode, currentHeight+1)
	if leftHeight == -1 {
		return -1
	}
	rightHeight := isBalance(node.rightNode, currentHeight+1)
	if rightHeight == -1 {
		return -1
	}
	if math.Abs(float64(leftHeight-rightHeight)) > 1 {
		return -1
	}
	if leftHeight > rightHeight {
		return leftHeight
	}
	return rightHeight
}

// Check if a binary tree is a binary search tree
func validateBST(node *intNode) bool {
	minValue, maxValue := checkBST(node)
	return minValue != math.MinInt && maxValue != math.MaxInt
}

func checkBST(node *intNode) (minValue, maxValue int) {
	if node.leftNode == nil && node.rightNode == nil {
		return node.data, node.data
	}
	var leftMinValue, leftMaxValue, rightMaxValue, rightMinValue int
	if node.leftNode != nil {
		leftMinValue, leftMaxValue = checkBST(node.leftNode)
		if leftMinValue == math.MinInt || leftMaxValue > node.data {
			return math.MinInt, math.MinInt
		}
	}
	if node.rightNode != nil {
		rightMinValue, rightMaxValue = checkBST(node.rightNode)
		if rightMinValue == math.MaxInt || rightMinValue <= node.data {
			return math.MinInt, math.MinInt
		}
	}
	return leftMinValue, rightMaxValue
}

// Function will return the "next" node (based on in order successor) of a given node in a binary search tree
// Each node has a link to it's parent
func successor(currentNode *intNode) *intNode {
	return nil
}

//bidrectional search
