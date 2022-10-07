package main

import "fmt"

var ()

func main() {
	// test := SetOfStacks{maxStackCapacity: 3}
	// test.push(1)
	// test.push(2)
	// test.push(3)
	// test.push(4)
	// fmt.Println(test.peek())
	// fmt.Println(test.pop())
	// fmt.Println(test.peek())

	// queueTest := QueueWithStacks{}
	// queueTest.init()
	// queueTest.add(1)
	// queueTest.add(2)
	// queueTest.add(3)
	// fmt.Println(queueTest.peek())
	// queueTest.remove()
	// queueTest.add(4)
	// fmt.Println(queueTest.peek())

	// unsorted := MyStack{}
	// unsorted.push(4)
	// unsorted.push(6)
	// unsorted.push(2)
	// unsorted.push(5)
	// sorted := sortStack(&unsorted)
	// for !sorted.isEmpty() {
	// 	fmt.Println(sorted.pop())
	// }

	animalShel := animalShelter{}
	animalShel.enqueue(true, "doggy1")
	animalShel.enqueue(false, "kitty1")
	animalShel.enqueue(false, "kitty2")
	animalShel.enqueue(true, "doggy2")
	// fmt.Println(animalShel.dequeueAny())
	// fmt.Println(animalShel.dequeueAny())
	// fmt.Println(animalShel.dequeueAny())
	fmt.Println(animalShel.dequeueDogOrCat(false))
	fmt.Println(animalShel.dequeueDogOrCat(false))
	fmt.Println(animalShel.dequeueDogOrCat(true))
	fmt.Println(animalShel.dequeueDogOrCat(true))
}
