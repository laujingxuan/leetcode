package main

import "fmt"

var ()

func main() {
	test := SetOfStacks{maxStackCapacity: 3}
	test.push(1)
	test.push(2)
	test.push(3)
	test.push(4)
	fmt.Println(len(test.stackList))
	fmt.Println(test.peek())
	fmt.Println(test.pop())
	fmt.Println(len(test.stackList))
	fmt.Println(test.peek())
}
