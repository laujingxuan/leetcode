package main

import (
	"fmt"
	"math"
)

var wg = sync.WaitGroup{}

func main() {
	go logger()
	logCh <- "log message"
	logCh <- "shutdown"
	time.Sleep(100 * time.Milisecond)
	doneCh <- struct{}{}
}

func logger(){
	for {
		select {
		case entry := <-logCh:
			fmt.Printf("%v\n", entry)
		case <- doneCh:
			break
		}
	}
}

func maxProfit(prices []int) int {
	min := math.MaxInt
	max := math.MinInt
	currentMaxDifference := 0
	for i := 0; i < len(prices)-1; i++ {
		if prices[i+1] > prices[i] {
			if prices[i] < min {
				min = prices[i]
				max = 0
			}
			if prices[i+1] > max {
				max = prices[i+1]
			}
			if min != math.MaxInt && max-min > currentMaxDifference {
				currentMaxDifference = max - min
			}
		}
	}
	if min != math.MaxInt {
		return currentMaxDifference
	}
	return 0
}
