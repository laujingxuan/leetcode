package main

// <------------------------------------ Queue ---------------------------------------->
type QueueNode struct {
	Data int
	Next *QueueNode
}

type MyQueue struct {
	Last  *QueueNode
	First *QueueNode
}

func (q *MyQueue) add(newData int) {
	newNode := QueueNode{Data: newData}
	if q.Last != nil {
		q.Last.Next = &newNode
	}
	q.Last = &newNode
	if q.First == nil {
		q.First = &newNode
	}
}

func (q *MyQueue) remove() int {
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

func (q *MyQueue) peek() int {
	if q.First == nil {
		return -1
	}
	return q.First.Data
}

//isEmpty
func (q *MyQueue) isEmpty() bool {
	return q.First == nil
}

// <------------------------------------ Queue implementation with two stacks ---------------------------------------->
type QueueWithStacks struct {
	StackOldest *MyStack
	StackNewest *MyStack
}

func (q *QueueWithStacks) init() {
	q.StackNewest = &MyStack{}
	q.StackOldest = &MyStack{}
}

func (q *QueueWithStacks) add(data int) {
	q.StackNewest.push(data)
}

func (q *QueueWithStacks) remove() int {
	q.moveValueIfNeeded()
	//if both oldest and newest are empty, then -1 will be returned
	return q.StackOldest.pop()
}

func (q *QueueWithStacks) peek() int {
	q.moveValueIfNeeded()
	return q.StackOldest.peek()
}

func (q *QueueWithStacks) isEmpty() bool {
	return q.StackOldest.isEmpty() && q.StackNewest.isEmpty()
}

func (q *QueueWithStacks) moveValueIfNeeded() {
	if q.StackOldest.isEmpty() {
		//move all the nodes from newest to oldest
		for !q.StackNewest.isEmpty() {
			q.StackOldest.push(q.StackNewest.pop())
		}
	}
}
