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
