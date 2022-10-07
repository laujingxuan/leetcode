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
func (s MyStack) push(newData int) {
	newNode := StackNode{Data: newData, Next: s.Top}
	s.Top = &newNode
}

func (s MyStack) pop() int {
	if s.Top != nil {
		topData := s.Top.Data
		s.Top = s.Top.Next
		return topData
	}
	return -1
}

//Not using reference to prevent updating of node
func (s MyStack) peek() int {
	if s.Top == nil {
		return -1
	}
	return s.Top.Data
}

func (s MyStack) isEmpty() bool {
	return s.Top == nil
}

// <------------------------------------ Queue ---------------------------------------->
type QueueNode struct {
	Data int
	Next *QueueNode
}

type MyQueue struct {
	Last  *QueueNode
	First *QueueNode
}

func (q MyQueue) add(newData int) {
	newNode := QueueNode{Data: newData}
	if q.Last != nil {
		q.Last.Next = &newNode
	}
	q.Last = &newNode
	if q.First == nil {
		q.First = &newNode
	}
}

func (q MyQueue) remove() int {
	if q.First == nil {
		return -1
	}
	firstData := q.First.Data
	q.First = q.First.Next
	if q.First == nil {
		q.Last = nil
	}
	return firstData
}

func (q MyQueue) peek() int {
	if q.First == nil {
		return -1
	}
	return q.First.Data
}

//isEmpty
func (q MyQueue) isEmpty() bool {
	return q.First == nil
}

// <-------------------------------------- MinStack ----------------------------------------->
//design a stack with min function which returns the minimum element. Push, pop and min should operate in O(1)
type MinStack struct {
	stack       MyStack
	minTracking MyStack
}

func (m MinStack) push(data int) {
	if m.minTracking.peek() == -1 || m.minTracking.peek() >= data {
		m.minTracking.push(data)
	}
	m.stack.push(data)
}

func (m MinStack) pop() int {
	data := m.stack.pop()
	if m.minTracking.peek() == -1 || m.minTracking.peek() == data {
		m.minTracking.pop()
	}
	return data
}

func (m MinStack) min() int {
	return m.minTracking.peek()
}

// <-------------------------------------- SetOfStacks ----------------------------------------->
// Implements a data structure  that composed of several stacks and should create a new stack once the previous one exceeds capacity
// Function like push and pop should behave like normal stack
