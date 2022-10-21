package main

// <----------------------------------- Stack --------------------------------------->
type StackNode struct {
	//assume int can only be positive, negative means error
	Data int
	Next *StackNode
}

type MyStack struct {
	Top *StackNode
}

//Not using reference to prevent updating of node
func (s *MyStack) push(newData int) {
	newNode := StackNode{Data: newData, Next: s.Top}
	s.Top = &newNode
}

func (s *MyStack) pop() int {
	if s.Top != nil {
		topData := s.Top.Data
		s.Top = s.Top.Next
		return topData
	}
	return -1
}

//Not using reference to prevent updating of node
func (s *MyStack) peek() int {
	if s.Top == nil {
		return -1
	}
	return s.Top.Data
}

func (s *MyStack) isEmpty() bool {
	return s.Top == nil
}

// <-------------------------------------- MinStack ----------------------------------------->
//design a stack with min function which returns the minimum element. Push, pop and min should operate in O(1)
type MinStack struct {
	stack       MyStack
	minTracking MyStack
}

func (m *MinStack) push(data int) {
	if m.minTracking.peek() == -1 || m.minTracking.peek() >= data {
		m.minTracking.push(data)
	}
	m.stack.push(data)
}

func (m *MinStack) pop() int {
	data := m.stack.pop()
	if m.minTracking.peek() == -1 || m.minTracking.peek() == data {
		m.minTracking.pop()
	}
	return data
}

func (m *MinStack) min() int {
	return m.minTracking.peek()
}

// <-------------------------------------- SetOfStacks ----------------------------------------->
// Implements a data structure  that composed of several stacks and should create a new stack once the previous one exceeds capacity
// Function like push and pop should behave like normal stack
type SetOfStacks struct {
	maxStackCapacity int
	stackList        []*StackWithCapacity
}

func (s *SetOfStacks) lastStack() *StackWithCapacity {
	if len(s.stackList) == 0 {
		newStack := StackWithCapacity{stackCapacity: s.maxStackCapacity}
		s.stackList = append(s.stackList, &newStack)
		return &newStack
	}
	currentStack := s.stackList[len(s.stackList)-1]
	return currentStack
}
func (s *SetOfStacks) push(newData int) {
	currentStack := s.lastStack()
	if currentStack.isFull() {
		newStack := StackWithCapacity{stackCapacity: s.maxStackCapacity}
		s.stackList = append(s.stackList, &newStack)
		currentStack = &newStack
	}
	currentStack.push(newData)
}

func (s *SetOfStacks) pop() int {
	currentStack := s.lastStack()
	data := currentStack.pop()
	if currentStack.stackCapacity == s.maxStackCapacity {
		//means currentStack is empty, remove the stack
		s.stackList = s.stackList[:len(s.stackList)-1]
	}
	return data
}

func (s *SetOfStacks) peek() int {
	if len(s.stackList) == 0 {
		return -1
	}
	currentStack := s.lastStack()
	return currentStack.peek()
}

func (s *SetOfStacks) isEmpty() bool {
	return len(s.stackList) == 0
}

// <----------------------------------- Stack With Capacity --------------------------------------->
type StackWithCapacity struct {
	Top           *StackNode
	stackCapacity int
}

func (s *StackWithCapacity) isFull() bool {
	return s.stackCapacity <= 0
}

//Not using reference to prevent updating of node
func (s *StackWithCapacity) push(newData int) bool {
	if s.stackCapacity <= 0 {
		return false
	}
	newNode := StackNode{Data: newData, Next: s.Top}
	s.Top = &newNode
	s.stackCapacity -= 1
	return true
}

func (s *StackWithCapacity) pop() int {
	if s.Top != nil {
		topData := s.Top.Data
		s.Top = s.Top.Next
		s.stackCapacity += 1
		return topData
	}
	return -1
}

//Not using reference to prevent updating of node
func (s *StackWithCapacity) peek() int {
	if s.Top == nil {
		return -1
	}
	return s.Top.Data
}

func (s *StackWithCapacity) isEmpty() bool {
	return s.Top == nil
}

// <----------------------------------- Other functions --------------------------------------->
//Sort a stack such that the smallest items are on the top, can use additional temporary stack but cannot copy the elements into any other data structure
func sortStack(unsorted *MyStack) *MyStack {
	sortedStack := MyStack{}
	for !unsorted.isEmpty() {
		temp := unsorted.pop()
		for !sortedStack.isEmpty() && sortedStack.peek() <= temp {
			unsorted.push(sortedStack.pop())
		}
		sortedStack.push(temp)

	}
	return &sortedStack
}

// <----------------------------------- Implementing queue with stack  --------------------------------------->
type MyStack1 struct {
	queue []int
}

func Constructor() MyStack1 {
	return MyStack1{[]int{}}
}

func (this *MyStack1) Push(x int) {
	this.queue = append(this.queue, x)
	for i := 0; i < len(this.queue)-1; i++ {
		this.queue = append(this.queue, this.queue[0])
		this.queue = this.queue[1:]
	}
}

func (this *MyStack1) Pop() int {
	if len(this.queue) == 0 {
		return -1
	}
	lastNumber := this.queue[0]
	this.queue = this.queue[1:]
	return lastNumber
}

func (this *MyStack1) Top() int {
	if len(this.queue) == 0 {
		return -1
	}
	return this.queue[0]
}

func (this *MyStack1) Empty() bool {
	return len(this.queue) == 0
}
