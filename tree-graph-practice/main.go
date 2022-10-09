package main

import "fmt"

var (
	rootNode = NewGraphNode("1", []*graphNode{
		&secondNode,
		&thirdNode,
		&forthNode,
	})
	secondNode = NewGraphNode("2", []*graphNode{
		&fifthNode,
		&sixthNode})
	thirdNode   = NewGraphNode("3", []*graphNode{&seventhNode})
	forthNode   = NewGraphNode("4", []*graphNode{})
	fifthNode   = NewGraphNode("5", []*graphNode{&eightNode})
	sixthNode   = NewGraphNode("6", []*graphNode{})
	seventhNode = NewGraphNode("7", []*graphNode{})
	eightNode   = NewGraphNode("8", []*graphNode{})
)

func main() {
	// fmt.Println(depthFirstSearch(&rootNode, "9"))
	fmt.Println(breathFirstSearch(&rootNode, "9"))
}
