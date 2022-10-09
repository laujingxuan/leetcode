package main

import (
	"fmt"
)

type intLinkNode struct {
	data int
	next *intLinkNode
}

type intNode struct {
	data      int
	leftNode  *intNode
	rightNode *intNode
}

type graphNode struct {
	name      string
	children  []*graphNode
	isVisited bool
}

func NewGraphNode(name string, children []*graphNode) graphNode {
	return graphNode{
		name, children, false,
	}
}

func visit(node *graphNode, target string) bool {
	return node.name == target
}

func depthFirstSearch(node *graphNode, target string) string {
	fmt.Println("Node path: ", node.name)
	node.isVisited = true
	if visit(node, target) {
		return node.name
	}
	for _, child := range node.children {
		if !child.isVisited {
			returnString := depthFirstSearch(child, target)
			if returnString != "" {
				return returnString
			}
		}
	}
	return ""
}

func breathFirstSearch(node *graphNode, target string) string {
	checkQueue := MyQueue{}
	checkQueue.enqueue(node)
	for !checkQueue.isEmpty() {
		checkNode := checkQueue.dequeue()
		fmt.Println("Node path: ", checkNode.name)
		checkNode.isVisited = true
		if visit(checkNode, target) {
			return checkNode.name
		}
		for _, child := range checkNode.children {
			if !child.isVisited {
				checkQueue.enqueue(child)
			}
		}
	}
	return ""
}

type QueueNode struct {
	data *graphNode
	next *QueueNode
}

type MyQueue struct {
	First *QueueNode
	Last  *QueueNode
}

func (q *MyQueue) enqueue(newNode *graphNode) {
	newQueueNode := QueueNode{data: newNode}
	if newNode != nil {
		if q.First != nil {
			q.Last.next = &newQueueNode
			q.Last = &newQueueNode
			return
		}
		q.First = &newQueueNode
		q.Last = &newQueueNode
	}
}

func (q *MyQueue) dequeue() *graphNode {
	if q.Last != nil {
		//Last == first
		if q.First == q.Last {
			returnNode := q.First.data
			q.First = nil
			q.Last = nil
			return returnNode
		}
		//Last != first
		returnNode := q.First.data
		q.First = q.First.next
		return returnNode
	}
	return nil
}

func (q *MyQueue) isEmpty() bool {
	return q.First == nil
}

// help to print binary search tree of intNode
func printIntNode(node *intNode) {
	if node.leftNode != nil {
		printIntNode(node.leftNode)
	}
	fmt.Println(node.data)
	if node.rightNode != nil {
		printIntNode(node.rightNode)
	}
}

func printIntLinkList(node *intLinkNode) {
	currentNode := node
	for currentNode != nil {
		fmt.Println("Node: ", currentNode.data)
		currentNode = currentNode.next
	}
}
